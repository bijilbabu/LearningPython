#Name: Nijil K Babu
#PGID: 71721084

#Question 2

#First Method
def power(x,y):
    if x==1:
        return True
        
    p=1
    
    while(p<y):
        p*=x
    if p == y:
        return True
    else:
        return False
        

#Test Cases    
print (power(1,7)) #True
print (power(2,7)) #False
print (power(10,1001)) #False
print (power(2,128)) #True

#Second Method
def power1(x,y):
    if x==1:
        return True
        
    val=y
    
    while(val>x):
        val/=x
    if val == x :
        return True
    else:
        return False

#Test Case
print (power1(1,7)) #True
print (power1(2,7)) #False
print (power1(10,1001)) #False
print (power1(2,128)) #True