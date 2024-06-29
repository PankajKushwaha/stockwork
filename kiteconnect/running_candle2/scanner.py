import pandas as pd
from myLib import *
import datetime
import time


NIFTY_FNO = get_fno_list_with_nse()

already_seen = []

while True:
    df = pd.read_csv("ohlc.csv")
#    print(df)
    for symbol in NIFTY_FNO:
        print(symbol)
        ma20  = df[symbol+'_close'].rolling( 20).mean()
        ma200 = df[symbol+'_close'].rolling(200).mean()
        df[symbol+"_ma20"] = ma20
        df[symbol+"_ma200"] = ma200

    lst = []
    for symbol in NIFTY_FNO:
        if symbol in already_seen:
            continue
        n = -9
#        print(symbol)
        while n < 0:
            #print(n)
            #print(df[symbol+"_high"].iloc[n])
            #print(df[symbol+"_ma20"].iloc[n])
            if n==-1:
                if df[symbol+"_high"].iloc[n] >= df[symbol+"_ma20"].iloc[n]:
                    print(symbol)
                    print(df[symbol+"_high"].iloc[-1])
                    print(df[symbol+"_low"].iloc[-1])
                    print(df[symbol+"_open"].iloc[-1])
                    print(df[symbol+"_close"].iloc[-1])
                    print(df[symbol+"_ma20"].iloc[-1])
                    lst.append(symbol)
            if df[symbol+"_high"].iloc[n] < df[symbol+"_ma20"].iloc[n]:
                n=n+1
                continue
            else:
                break
            n=n+1

    for symbol in NIFTY_FNO:
        if symbol in already_seen:
            continue
        n = -9
        while n < 0:
            #print(n)
            if n==-1:
                if df[symbol+"_low"].iloc[n] <= df[symbol+"_ma20"].iloc[n]:
                    #print(symbol)
                    print(df[symbol+"_high"].iloc[-1])
                    print(df[symbol+"_low"].iloc[-1])
                    print(df[symbol+"_open"].iloc[-1])
                    print(df[symbol+"_close"].iloc[-1])
                    print(df[symbol+"_ma20"].iloc[-1])
                    lst.append(symbol)
            if df[symbol+"_low"].iloc[n] > df[symbol+"_ma20"].iloc[n]:
                n=n+1
                continue
            else:
                break
            n=n+1

    already_seen.extend(lst)
    save_screenshot(lst)

    s=datetime.datetime.now().second
    time.sleep((60-s)+30)


#print(df)
