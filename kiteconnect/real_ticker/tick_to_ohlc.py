from set_token import *
from myLib import *
import threading
import pandas as pd
import time
import os
import time

df = pd.DataFrame(columns=['Timestamp', 'Instrument', 'LTP' ])
dtime = datetime.now()
old_m=dtime.minute
first_m=dtime.minute

NIFTY_FNO=get_fno_list_new()
instrument_tokens=list(get_token_to_instrument(NIFTY_FNO).keys())
instrument_tokens_dic=get_token_to_instrument(NIFTY_FNO)

file_name = "tick.csv"

#instrument_tokens=[109123079]
# Callback functions
def on_ticks(ws, ticks):
    global old_m
    global df
    global file_name
    dtime = datetime.now()
    new_m=dtime.minute
    #if new_m%5==0 and new_m!=old_m and len(df)>1:
    if new_m!=old_m and len(df)>1:
        if os.path.exists(file_name):
            base_df = pd.read_csv(file_name)
            combined_df = base_df.append(df, ignore_index=True)
            combined_df.to_csv(file_name, index=False)
            print("append")
            old_m=new_m
        else:
            df.to_csv(file_name, index=False)
            old_m=new_m
        df = df.drop(df.index)
        '''
        lst=df["LTP"].tolist()
        o=lst[0]
        h=max(lst)
        l=min(lst)
        c=lst[-1]
        print("==============ohlc=============")
        print(o)
        print(h)
        print(l)
        print(c)
        df.drop(df.index, inplace=True)
        old_m=new_m
        '''
    df = pd.DataFrame(ticks, columns=columns)
    print(df)
    for tick in ticks:
        #print(tick["instrument_token"])
        #print(tick["last_trade_time"])
        #print(tick["last_price"])
        it=instrument_tokens_dic[tick["instrument_token"]]
        #it=tick["instrument_token"]
        ltt=tick["last_trade_time"].time()
        ltp=tick["last_price"]
        df.loc[len(df)] = [ltt, it, ltp]
    #print(df)

def on_connect(ws, response):
    # Subscribe to instrument
    ws.subscribe(instrument_tokens)
    ws.set_mode(kws.MODE_FULL,instrument_tokens)

def on_close(ws, code, reason):
    print("WebSocket closed:", code, reason)

def on_error(ws, code, reason):
    print("WebSocket error:", code, reason)

# Assign callback functions
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.on_error = on_error

# Connect to WebSocket
time.sleep(wait_for_5min()+1)
connection_successful=kws.connect(threaded=True)
if connection_successful:
    print("WebSocket connection successful!")
else:
    print("Failed to connect to WebSocket server.")
count=0
while True:
    count = count+1
    if (count%2 == 0):
        if kws.is_connected():
            kws.set_mode(kws.MODE_FULL,instrument_tokens)
        else:
            if kws.is_connected():
                kws.set_mode(kws.MODE_FULL,instrument_tokens)
        time.sleep(0.1)