#Name: Nijil K Babu
#PGID: 71721084

#Question 3

def hcf(a, b, c):
    if b > a < c :
        lowest=a
    elif a > b < c:
        lowest=b
    else:
        lowest=c
        
    for i in range(1,lowest+1):
        if (a%i==0) and (b%i==0) and (c%i==0):
            gcd=i
            
    return gcd
    
#test Case
print ("The Greatest Common Divisor between the given input is", hcf(36,24,12)) #12
print ("The Greatest Common Divisor between the given input is", hcf(36,27,12)) #3
print ("The Greatest Common Divisor between the given input is", hcf(36,13,12)) #1
print ("The Greatest Common Divisor between the given input is", hcf(36,11,12)) #1
            