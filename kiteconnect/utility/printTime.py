from datetime import datetime, timedelta

def printTime():
    time = datetime.now()
    h=str(time.hour)
    s=str(time.second)
    m=str(time.minute)
    t=h+":"+m+":"+s
    print(t)

def isTLthan(t):
    ts=t.split(":")
    time = datetime.now()
    h=time.hour
    s=time.second
    m=time.minute
    print(int(ts[0]))
    print(int(ts[1]))
    print(int(h))
    print(int(m))
    if int(h)<=int(ts[0]) and int(m) < int(ts[1]) :
        return True
    else:
        return False

printTime()





