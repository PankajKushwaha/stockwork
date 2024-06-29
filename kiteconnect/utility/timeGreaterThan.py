from datetime import datetime, timedelta

def isTGthan(t):
    ts=t.split(":")
    time = datetime.now()
    h=time.hour
    s=time.second
    m=time.minute
    print(h)
    print(ts[0])
    print(m)
    print(ts[1])
    if int(h) >= int(ts[0]) and int(m) >= int(ts[1]):
        return True 
    else:
        return False


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

print(isTGthan("09:08"))





