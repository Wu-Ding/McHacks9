import csv
from random import randrange
import random
import heapq
#import numpy as np

def find_neighbours(n, rand, o_list): 
    "return a list of n lists with new random times based on the original list of times passed to the function"
    "rand is the range that we want to modify each of the original list's element by"
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
                        n_list.append(n_list[i]+3)
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
    "return a list of n lists with new random times based on the original list of times passed to the function"
    "rand is the range that we want to modify each of the original list's element by"
    r_list = []
    loop_count = 0
    while loop_count < n:
        n_list = [0]
        for i in range(1,15):
            if i == 14:
                if n_list[i-1] + 3 >= o_list[15]:
                    #don't increment loop_count
                    break #list is not valid, regenerate

            random_num = np.random.normal(0, rand)
            operation = 1
            if random_num < 0:
                operation = 0

            if operation == 0: 
                if o_list[i] <= n_list [i-1]+3:
                    if o_list[i] + rand - 1 <= n_list[i-1]+3:
                        n_list.append(n_list[i]+3)
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

def format(t):
    hour = str(7+(t // 60))
    minutes = str(t%60)
    if int(minutes)<10:
        minutes="0"+minutes
    return (hour + ":" + minutes)

def format_l(l):
    "formats times which are represented by numbers from 0 to 180 back to numbers from 7:00 to 10:00"
    formatted_list = []
    for t in l:
        formatted_list.append(format(t))
    return formatted_list 

def get_info(start, capacity, pass_a, pass_b, pass_c):
    """
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
    info.append(format(start))
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
            board = n - capacity
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
    info.append(format(start+11))
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
            board = n - capacity
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
    info.append(format(start+23))
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
            board = n - capacity
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
    info.append(format(start+37))
    #U_AvailCap 
    info.append(str(capacity))
    #U_Offloading
    info.append(init_cap-capacity)

    return info



def write_csv(starts, capacities, passengers):
    """
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
        my_writer.writerow(['TrainNum', 'TrainType', 'A_ArrivalTime', 'A_AvailCap', 'A_Boarding', 'B_ArrivalTime', 'B_AvailCap', 'B_Boarding', 'C_ArrivalTime', 'C_AvailCap', 'C_Boarding', 'U_Arrival', 'U_AvailCap', 'U_Offloading'])
        for s in range(len(starts)):
            info = get_info(starts[s], capacities[s], stations[0], stations[1], stations[2])
            info.insert(0, s+1) #insert train number at start of line
            my_writer.writerow(info)
    
        
    
#usages:
print(find_neighbours(5, 11, [0, 8, 18, 27, 35, 38, 48, 57, 67, 78, 88, 98, 108, 128, 155, 178]))
#print(format_l([0, 8, 18, 27, 35, 38, 48, 57, 67, 78, 88, 98, 108, 128, 155, 178]))

#====write_csv====
# passengers = ((25,50,75,100,125,150,125,100,75,50,45,40,35,30,25,20,15,10,5),
#             (50,75,100,125,150,175,150,125,100,100,75,75,50,45,35,25,20,15,10),
#             (50,100,150,200,250,200,175,150,150,125,100,75,50,50,45,40,35,30,25))

# tentative_schedule = (0,8,18,27,35,38,48,57,67,78,88,98,108,128,155,178)
# tentative_capacities = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 200)
    
# write_csv(tentative_schedule, tentative_capacities, passengers)
