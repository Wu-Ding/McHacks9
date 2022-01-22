from random import randrange

def find_neighbours(n, o_list): #has to be bigger by at least 3
    "return a list of n lists with new random times based on the original list of times passed to the function"
    r_list = []
    rand = 11
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
                    n_list.append(o_list[i]+random_num)
                    continue

                while o_list[i]-random_num <= n_list[i-1]+3: 
                    random_num = randrange(rand) 
                n_list.append(o_list[i]-random_num)  
                
            if operation == 1:
                n_list.append(o_list[i]+random_num)
        n_list.append(o_list[15])
        r_list.append(n_list)
        loop_count += 1

    return r_list

def format(l):
    "formats times which are represented by numbers from 0 to 180 back to numbers from 7:00 to 10:00"
    formatted_list = []
    for t in l:
        hour = str(7+(t // 60))
        minutes = str(t%60)
        if int(minutes)<10:
            minutes="0"+minutes
        formatted_list.append(hour + ":" + minutes)
    return formatted_list 

#usages:
#print(find_neighbours(5,[0, 8, 18, 27, 35, 38, 48, 57, 67, 78, 88, 98, 108, 128, 155, 178]))
#print(format([0, 8, 18, 27, 35, 38, 48, 57, 67, 78, 88, 98, 108, 128, 155, 178]))
    
    

