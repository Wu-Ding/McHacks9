import heapq

passengers = ((25,50,75,100,125,150,125,100,75,50,45,40,35,30,25,20,15,10,5),
              (50,75,100,125,150,175,150,125,100,100,75,75,50,45,35,25,20,15,10),
              (50,100,150,200,250,200,175,150,150,125,100,75,50,50,45,40,35,30,25))

tentative_schedule = (0,8,18,27,35,38,48,57,67,78,88,98,108,128,155,178)
tentative_capacities = (400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 400, 200, 200, 400, 200, 200)

def one_train(start, capacity, pass_a, pass_b, pass_c):
    """
    (int, int,, int list, int list, int list) -> int
    
    Returns the total wait time of the passengers boarding the train
    
    Assumes that pass_a, pass_b, pass_c are priority queues
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
            board = n - capacity
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
            board = n - capacity
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
            board = n - capacity
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
    (int tuple, int tuple, (int tuple) tuple) -> int

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
            raise Exception("Not all passengers made it to Union Station!")
        
    return total_waittime
        
    