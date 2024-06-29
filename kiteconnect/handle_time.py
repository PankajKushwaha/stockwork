import time
from datetime import datetime

def current_milli_time():
    return round(time.time() * 1000)

def handle_max_request():
    time = datetime.now()
    lSecondNow=time.second
    global gSecondNow
    global gNumOfCall
    if gNumOfCall>3 and lSecondNow == gSecondNow:
        while lSecondNow == gSecondNow:
            time = datetime.now()
            lSecondNow=time.second
            time.sleep(0.1)
        time = datetime.now()
        gSecondNow=time.second
        gNumOfCall=0
    else if gNumOfCall<3: 
        if lSecondNow != gSecondNow:
            gNumOfCall = 0
        else:
            gNumOfCall=gNumOfCall+1

while True:
    print(current_milli_time())
    time.sleep(0.1)
