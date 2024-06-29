from datetime import datetime, timedelta
import time

def round_by_five(time):
    if time.second == 0 and time.microsecond == 0 and time.minute % 5 == 0:
        return time
    minutes_by_five = time.minute // 5
    # get the difference in times
    diff = (minutes_by_five + 1) * 5 - time.minute
    time = (time + timedelta(minutes=diff)).replace(second=0, microsecond=0)
    return time
'''
time = datetime.now()
print(time)
print(time.minute)
print(int(time.second))
print(round_by_five(time))
'''

def get_time_to_wait():
    time = datetime.now()
    s=time.second
    m=time.minute
    r=0

    while m%5 != 0:
        m=m+1

    if time.minute>=m-1 and time.minute<m:
        print("in first case")
        r=(60-time.second) + 240 
        return r
    else:
        print("in second case")
        r=(((m-time.minute)-2)*60 + (60-time.second))
        return r

while True:
    r=get_time_to_wait()
    print(r)
    print(datetime.now())
    time.sleep(r)
    print("pankaj")


