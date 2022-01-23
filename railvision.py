## Collaborators

## Wu Ding
## Jessica Li
## Anton Otaner
## Ryan Sadri

import heapq
import numpy as np
import csv

from random import randrange
import random

# Tuple of int tuples
# The outer tuple contains information about each station (A, B & C)
# The inner tuple indicates the number of people arriving at station "i" at each 10-minute mark (index 0 means 7:00am)
passengers = ((25,50,75,100,125,150,125,100,75,50,45,40,35,30,25,20,15,10,5),
              (50,75,100,125,150,175,150,125,100,100,75,75,50,45,35,25,20,15,10),
              (50,100,150,200,250,200,175,150,150,125,100,75,50,50,45,40,35,30,25))

# List of start times (in minutes) for each train
# Note that 7:00am is time=0
tentative_schedule = (0,8,18,27,35,38,48,57,67,78,88,98,108,128,155,178)
# List of capacities for each train
tentative_capacities = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 200)

# A few different capacity distributions
c0 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 200)
c1 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 200, 200)
c2 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 400, 200, 200)
c3 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 400, 200, 400, 200, 200)
c4 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 400, 200)
c5 = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 400, 200, 200, 200)

# The best schedules we found 
best0 = [0, 8, 18, 27, 35, 39, 48, 58, 68, 78, 88, 98, 108, 128, 148, 178] #10335, c0
best2 = [0, 8, 18, 27, 35, 39, 48, 58, 68, 78, 88, 98, 108, 128, 148, 178] #10335, c2
best3 = [0, 8, 18, 27, 35, 39, 48, 58, 68, 78, 88, 98, 108, 128, 148, 178] #10335, c3


"------------------------------------------------------------------------------------------------------------------------------------"
### Calculating the passenger wait times ###

def one_train(start, capacity, pass_a, pass_b, pass_c):
    """
    (int, int, int list, int list, int list) -> int
    
    Returns the total wait time of the passengers boarding the train
    
    Assumes that pass_a, pass_b, pass_c are priority queues
    pass_a, pass_b, pass_c are modified with each calling of the function
    Each element of the priority queue has form (t, n) where
        t: passenger arrival time at station
        n: number of passengers at the station that arrived at that time
    """
    total_waittime = 0
    
    #Getting the wait times for passengers from A
    while(len(pass_a) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_a)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 2):
            heapq.heappush(pass_a, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_a, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        capacity -= board
        
        #Calculate the waiting time of a passenger
        if (t < start + 3 and t >= start):
            wait = 0
        else:
            wait = start - t
            
        total_waittime += board * wait
        
    
    #Getting the wait times for passengers from B
    while(len(pass_b) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_b)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 13):
            heapq.heappush(pass_b, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_b, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        capacity -= board
        
        #Calculate the waiting time of a passenger
        if (t < start + 14 and t >= start + 11):
            wait = 0
        else:
            wait = start + 11 - t
            
        total_waittime += board * wait
        
    
    #Getting the wait times for passengers from C
    while(len(pass_c) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_c)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 25):
            heapq.heappush(pass_c, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_c, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        capacity -= board
        
        #Calculate the waiting time of a passenger
        if (t < start + 26 and t >= start + 23):
            wait = 0
        else:
            wait = start + 23 - t
            
        total_waittime += board * wait
            
    return total_waittime



def all_trains(starts, capacities, passengers):
    """
    (int list, int list, (int tuple) tuple) -> int

    Returns the total wait time of the passengers
    
    The inner tuple in the third argument represents the number of passengers arriving at station "i" with 10 minute intervals.
    Assumes len(starts) == len(capacities)
    The function raises an exception if stations contains non-empty lists before returning a value.
    """
    
    stations = [[],[],[]]
    total_waittime = 0
    
    #Creating the pass_i priority queues used in one_train
    for i in range(3):
        for j in range(len(passengers[i])):
            t = j * 10
            n = passengers[i][j]
            stations[i].append((t,n))
    
    #Calculating the total wait time across all passengers
    for s in range(len(starts)):
        train_wait = one_train(starts[s], capacities[s], stations[0], stations[1], stations[2])
        total_waittime += train_wait
        
    #Raise an error if there are people remaining in the stations after the last train has passed    
    for station in stations:
        if len(station) > 0:
            total_waittime = 100000000
            #raise Exception("Not all passengers made it to Union Station!")
        
    return total_waittime



def avg_waittime(starts, capacities, passengers):
    """
    (int list, int list, (int tuple) tuple) -> str
    
    Returns the average wait time of a passenger in the minutes:seconds format
    """
    
    total_wait = all_trains(starts, capacities, passengers)
    avg_wait = total_wait / 4600
    minutes = int(avg_wait)
    seconds = round((avg_wait - minutes) * 60)
    return str(minutes)+":"+str(seconds)
    
    

"------------------------------------------------------------------------------------------------------------------------------------"
### Use search algorithms to find a schedule that minimizes the passenger wait time ###

def find_neighbours(n, rand, o_list):
    """
    (int, int, int list) -> int list

    Returns a list of n lists with new random times based on the original list of times passed to the function.
    rand is the range that we want to modify each of the original lists' element by"""
    r_list = []
    loop_count = 0
    while loop_count < n:
        n_list = [0]
        for i in range(1,15):
            if i == 14:
                if n_list[i-1] + 3 >= o_list[15]:
                    #don't increment loop_count
                    break #list is not valid, regenerate

            random_num = randrange(rand)
            operation = randrange(0,2) #add if 1, substr if 0

            if operation == 0: 
                if o_list[i] <= n_list [i-1]+3:
                    if o_list[i] + rand - 1 <= n_list[i-1]+3:
                        n_list.append(n_list[i-1]+3)
                        continue
                    while o_list[i]+random_num <= n_list[i-1]+3: 
                        random_num = randrange(rand) 
                    n_list.append(o_list[i]+random_num)
                    continue

                while o_list[i]-random_num <= n_list[i-1]+3: 
                    random_num = randrange(rand) 
                n_list.append(o_list[i]-random_num)  
                
            if operation == 1:
                if o_list[i] + rand - 1 <= n_list[i-1]+3:
                        n_list.append(n_list[i-1]+3)
                        continue
                while o_list[i]+random_num <= n_list[i-1]+3: 
                        random_num = randrange(rand)
                n_list.append(o_list[i]+random_num)

        n_list.append(o_list[15])
        r_list.append(n_list)
        loop_count += 1

    return r_list



def find_neighbours_normal(n, rand, o_list):
    """
    (int, int, int list) -> int list

    Returns a list of n lists with new random times based on the original list of times passed to the function.
    rand is the range that we want to modify each of the original lists' element by"""
    r_list = []
    loop_count = 0
    while loop_count < n:
        n_list = [0]
        for i in range(1,15):
            if i == 14:
                if n_list[i-1] + 3 >= o_list[15]:
                    #don't increment loop_count
                    break #list is not valid, regenerate

            random_num = round(np.random.normal(0, rand))
            operation = 1
            if random_num < 0:
                operation = 0

            if operation == 0: 
                if o_list[i] <= n_list [i-1]+3:
                    if o_list[i] + rand - 1 <= n_list[i-1]+3:
                        n_list.append(n_list[i-1]+3)
                        continue
                    while o_list[i]+random_num <= n_list[i-1]+3: 
                        random_num = round(randrange(rand))
                    n_list.append(o_list[i]+random_num)
                    continue

                while o_list[i]-random_num <= n_list[i-1]+3: 
                    random_num = round(randrange(rand)) 
                n_list.append(o_list[i]-random_num)  
                
            if operation == 1:
                if o_list[i] + rand - 1 <= n_list[i-1]+3:
                        n_list.append(n_list[i-1]+3)
                        continue
                while o_list[i]+random_num <= n_list[i-1]+3: 
                        random_num = round(randrange(rand))
                n_list.append(o_list[i]+random_num)

        n_list.append(o_list[15])
        r_list.append(n_list)
        loop_count += 1

    return r_list



def best_n(schedules_and_scores, capacities, n):
    """
    ((int, int list) list, int list, int) -> int list

    Randomly modify each schedule n times from the given list and keep the best generated ones.
    In this case, best means with minimal passenger waiting time.
    """
    
    new_list = []
    
    # Generate n * len(schedules_and_scores) schedules and calculate the resulting wait times
    for score, schedule in schedules_and_scores:
        heapq.heappush(new_list, (score, schedule))
        #The neighbours generated typically do not difer from the original by many dimensions
        neighbours = find_neighbours(n-1, 2, schedule)
        for starts in neighbours:
            new_score = all_trains(starts, capacities, passengers)
            heapq.heappush(new_list,(new_score, starts))
         
    new_list.sort()
    
    # Return the best performing len(schedules_and_scores) schedules
    return new_list[0:len(schedules_and_scores)]
    
    

def find_min(x0, capacities):
    """
    (int list, int list) --> (int list, int)

    Find the schedule that minimizes the passenger wait time with the given capacity distribution
    Uses a mixture of Local beam search and Genetic Algorithm
    Returns the min result
    """
    scores_and_schedules = []
    
    # Generate 199 neighbouring schedules using the input schedule x0
    init_neighbours = find_neighbours(199, 10, x0)
    
    min_score = all_trains(x0, capacities, passengers)
    min_sched = x0
    heapq.heappush(scores_and_schedules,(min_score, x0))
    
    # Add them all to the list, as well as the input schedule
    for i in init_neighbours:
        score = all_trains(i, capacities, passengers)
        heapq.heappush(scores_and_schedules,(score, i))
        if score < min_score:
            min_score, min_sched = score, i
            
    local_min_counter = 0
    
    # Perform the genetic algorithm for optimization
    while local_min_counter < 500:
        scores_and_schedules = best_n(scores_and_schedules, capacities, 5)
        if scores_and_schedules[0][0] < min_score:
            min_score, min_sched = scores_and_schedules[0]
            local_min_counter = 0
        else:
            local_min_counter += 1
            
    return min_sched, min_score



"------------------------------------------------------------------------------------------------------------------------------------"
### Formatting and writing the csv file ###
  
def format_t(t):
    """
    (int) -> str
    
    Formats an integer into its corresponding time
    """
    hour = str(7+(t // 60))
    minutes = str(t%60)
    if int(minutes)<10:
        minutes="0"+minutes
    return (hour + ":" + minutes)



def format_l(l):
    """
    (int list) -> str list
    
    formats times which are represented by numbers from 0 to 180 back to numbers from 7:00 to 10:00
    """
    formatted_list = []
    for t in l:
        formatted_list.append(format_t(t))
    return formatted_list 



def get_info(start, capacity, pass_a, pass_b, pass_c):
    """
    (int, int, int list, int list, int list) -> list

    Puts all the information for one train into a list to be written to a csv file later. 
    """
    total_waittime = 0
    info = []
    init_cap = capacity
    board_tot = 0

    #TrainType
    if capacity == 200:
        info.append("L4")
    else: 
        info.append("L8")
    #A_ArrivalTime
    info.append(format_t(start))
    #A_AvailCap
    info.append(str(capacity))

    #Getting the wait times for passengers from A
    while(len(pass_a) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_a)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 2):
            heapq.heappush(pass_a, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_a, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        
        board_tot += board
        capacity -= board

        #Calculate the waiting time of a passenger
        if (t < start + 3 and t >= start):
            wait = 0
        else:
            wait = start - t
            
        total_waittime += board * wait
    #A_Boarding
    info.append(str(board_tot))
    board_tot = 0
    #B_ArrivalTime
    info.append(format_t(start+11))
    #B_AvailCap
    info.append(str(capacity))

    #Getting the wait times for passengers from B
    while(len(pass_b) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_b)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 13):
            heapq.heappush(pass_b, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_b, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        board_tot += board
        capacity -= board
        
        #Calculate the waiting time of a passenger
        if (t < start + 14 and t >= start + 11):
            wait = 0
        else:
            wait = start + 11 - t
            
        total_waittime += board * wait

    #B_Boarding
    info.append(str(board_tot))
    board_tot = 0

    #Getting the wait times for passengers from C
    #C_ArrivalTime
    info.append(format_t(start+23))
    #C_AvailCap
    info.append(str(capacity))

    while(len(pass_c) > 0 and capacity > 0):
        t,n = heapq.heappop(pass_c)
        
        #Break out of loop if the passengers are not there yet
        if (t > start + 25):
            heapq.heappush(pass_c, (t, n))
            break
        
        #Calculate number people boarding the train
        if n > capacity:
            board = capacity
            heapq.heappush(pass_c, (t, n - board))
        else:
            board = n
        
        #Update the train capacity
        board_tot += board
        capacity -= board
        
        #Calculate the waiting time of a passenger
        if (t < start + 26 and t >= start + 23):
            wait = 0
        else:
            wait = start + 23 - t
            
        total_waittime += board * wait

    #C_Boarding
    info.append(str(board_tot))
    #U_Arrival 
    info.append(format_t(start+37))
    #U_AvailCap 
    info.append(str(capacity))
    #U_Offloading
    info.append(init_cap-capacity)

    return info



def write_csv(starts, capacities, passengers):
    """
    (int list, int list, (int list) list) -> None
    
    Writes the required info of all trains to a csv file.
    """
    
    stations = [[],[],[]]
    
    #Creating the pass_i priority queues used in one_train
    for i in range(3):
        for j in range(len(passengers[i])):
            t = j * 10
            n = passengers[i][j]
            stations[i].append((t,n))
            
    with open('results.csv', mode='w', newline='') as out_file:
        my_writer = csv.writer(out_file, delimiter=',')
        my_writer.writerow(['TrainNum', 'TrainType', 'A_ArrivalTime', 'A_AvailCap', 'A_Boarding',
                            'B_ArrivalTime', 'B_AvailCap', 'B_Boarding', 'C_ArrivalTime', 'C_AvailCap', 'C_Boarding',
                            'U_Arrival', 'U_AvailCap', 'U_Offloading'])
        for s in range(len(starts)):
            info = get_info(starts[s], capacities[s], stations[0], stations[1], stations[2])
            info.insert(0, s+1) #insert train number at start of line
            my_writer.writerow(info)
    
    return
        
    
    

    