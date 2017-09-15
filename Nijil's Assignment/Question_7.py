#Name: Nijil K Babu
#PGID: 71721084

#Question 7

def cumulative_sum(lst):
    tot=0
    new_list=[]
    for i, element in enumerate(lst):
        tot += element      
        new_list.append(tot)
    
    return new_list
    

a=[1,2,3]
b=cumulative_sum(a)
print (b)
