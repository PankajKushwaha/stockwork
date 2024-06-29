from myLib import *
from set_token import *
import pandas as pd
import time
import datetime
import threading

NIFTY_FNO = get_fno_list_with_nse()
ltp_df = pd.DataFrame()
base_df = pd.DataFrame()
ohlc_df = pd.DataFrame()
isBaseDfReady = False
isOhlcDfUpdated = False
isAddToDf = False
isALineAdded = False

def update_ltf_df():
    #time.sleep(wait_for_5min())
    global ltp_df
    ohlc_dic = {}
    old_min=datetime.datetime.now().minute
    while True:
        cs=datetime.datetime.now().second
        new_min=datetime.datetime.now().minute
        if old_min != new_min and not ltp_df.empty:
            update_ohlc_df(ltp_df)
            old_min=new_min
            if new_min % 5 == 0 or new_min == 0:
                del ltp_df
                ltp_df = pd.DataFrame()
        
        ltpdic=get_ltp_dict()
        new_df = pd.DataFrame([ltpdic])
        ltp_df = pd.concat([ltp_df, new_df], ignore_index=True)
        
        print(datetime.datetime.now().second)
        current_time = datetime.datetime.now()
        microseconds = current_time.microsecond // 1000
        milliseconds_left = 1000 - microseconds
        seconds = milliseconds_left / 1000.0 
        time.sleep(seconds)
        #print(ltp_df)
        #print(ohlc_dic)

def update_ohlc_df(ltp_df):
    global isBaseDfReady
    global isOhlcDfUpdated
    global ohlc_df
    global isALineAdded 
    ohlc_dic={}
    curr_min=datetime.datetime.now().minute
    print("#######in update ohlc##########")
    for column_name in ltp_df.columns:
        column_values = ltp_df[column_name]
        #print(column_name)
        #print(column_values.tolist())
        lst=column_values.tolist()
        o=lst[0]
        h=max(lst)
        l=min(lst)
        c=lst[-1]
        ohlc_dic[column_name+"_open"]=o
        ohlc_dic[column_name+"_high"]=h
        ohlc_dic[column_name+"_low"]=l
        ohlc_dic[column_name+"_close"]=c
    tmp_ohlc_df = pd.DataFrame([ohlc_dic])
    print("isBaseDfReady")
    print(isBaseDfReady)
    print("isOhlcDfUpdated")
    print(isOhlcDfUpdated)
    print("isALineAdded")
    print(isALineAdded)
    if isBaseDfReady == True:
        print("add first time")
        ohlc_df = pd.concat([base_df, ohlc_df], ignore_index=True)
        isBaseDfReady = False
        isOhlcDfUpdated = True
    if ((curr_min - 1 )%5 == 0 or curr_min == 1) and isOhlcDfUpdated == True:
        ohlc_df = pd.concat([ohlc_df, tmp_ohlc_df], ignore_index=True)
        ohlc_df.to_csv('ohlc.csv', index=False)
        print("write to csv in if")
    elif isOhlcDfUpdated == True:
        ohlc_df = ohlc_df.drop(ohlc_df.index[-1])
        ohlc_df = pd.concat([ohlc_df, tmp_ohlc_df], ignore_index=True)
        ohlc_df.to_csv('ohlc.csv', index=False)
        print("write to csv in else")
    '''
    if isAdd == True and isOhlcDfUpdated == True:
        print("add row")
        ohlc_df = pd.concat([ohlc_df, tmp_ohlc_df], ignore_index=True)
        isALineAdded = True
    elif isAdd == False and isALineAdded == True:
        print("delete old row")
        ohlc_df = ohlc_df.drop(ohlc_df.index[-1])
        ohlc_df = pd.concat([ohlc_df, tmp_ohlc_df], ignore_index=True)
    if isOhlcDfUpdated == True and isALineAdded == True:
        ohlc_df.to_csv('ohlc.csv', index=False)
        print("write to csv")
    '''

def create_base_df():
    global base_df
    global isBaseDfReady 
    for symbol in NIFTY_FNO:
        hist_df=pd.DataFrame(get_candle(symbol,"5minute"))
        hist_df=hist_df[-500:]
        hist_df = hist_df.drop(['date','volume'], axis=1)
        hist_df = hist_df.rename(columns={'open': symbol+'_open'})
        hist_df = hist_df.rename(columns={'high': symbol+'_high'})
        hist_df = hist_df.rename(columns={'low': symbol+'_low'})
        hist_df = hist_df.rename(columns={'close': symbol+'_close'})
        #print(hist_df)
        base_df = pd.concat([base_df, hist_df], axis=1)
        #print(base_df)
        print("thread running")
    isBaseDfReady=True 
    print("############thread complete##########")

time.sleep(wait_for_5min())

my_thread = threading.Thread(target=create_base_df)
my_thread.start()

update_ltf_df()
