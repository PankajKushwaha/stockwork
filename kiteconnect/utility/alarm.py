from datetime import datetime, timedelta
import time
import os

def wait_for_5min():
    time = datetime.now()
    s=time.second
    m=time.minute
    curm=m
    if m%5==0:
        m=m+1
    while m%5 != 0:
        m=m+1
    m=(m-curm)-1
    sleft = 60-s
    mleft = m*60
    tleft = sleft+mleft
    print(tleft)
    return tleft

while True:
    t=wait_for_5min()
    gap=5
    wt=t-gap
    time.sleep(wt)
    os.system('spd-say "five minute completed"')
    time.sleep(wt+gap+2)
