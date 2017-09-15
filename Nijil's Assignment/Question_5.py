#Name: Nijil K Babu
#PGID: 71721084

#Question 5

def triangle(a,b,c):
    if ((a + b > c ) and (a + c > b) and (b + c > a)):
        return "Yes"
    else:
        return "No"
        
        
#test cases
print("Triangle can be created!!!",triangle(7,10,5)) # yes
print("Triangle can be created!!!",triangle(5,3,8)) # No