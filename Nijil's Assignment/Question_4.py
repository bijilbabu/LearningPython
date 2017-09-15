#Name: Nijil K Babu
#PGID: 71721084

#Question 4

import datetime as dt
import time 

#Reading the current time
current_time = time.strftime("%H:%M:%S")

#Considering the epoch is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), 

#Method 1 to find the number of days from epoch
# 1 day = 86400 seconds

now=dt.datetime.now()
second=now.strftime("%s")
days=int(int(second)/86400)

#Method 2 to find the number of days from epoch
days2=(dt.datetime.utcnow() - dt.datetime(1970,1,1)).days

print ("The Current time (HH:MM:SS) is",current_time,"\n")

print ("Considering the epoch is the number of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT)\n")
print ("The number of days since the epoch is ",days,". Using method 1")
print ("The number of days since the epoch is ",days2,". Using method 2\n")