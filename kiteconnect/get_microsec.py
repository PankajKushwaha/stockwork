import time

def current_milli_time():
    i=round(time.time() * 1000)
    j=i
    while True:
        j=j+1
        if j%1000 == 0:
            return (j-i)/1000


while True:
    print(current_milli_time())
    time.sleep(current_milli_time())
