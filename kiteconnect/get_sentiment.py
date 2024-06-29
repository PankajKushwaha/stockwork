from kiteconnect import KiteConnect
#from get_list_to_monitor import *
from set_token import *
import datetime
import os
import sys
import shutil
import pyautogui
import cv2
import time
import numpy as np
import click
import pickle
import time
import logging
from nsepython import *
from pynse import *
import pandas as pd
from heapq import nlargest
from heapq import nsmallest
from datetime import datetime, timedelta

sys.tracebacklimit = None
already_top_gainer = []
already_top_looser = []
new_day_high_dic={}
new_day_low_dic={}
global_high_low = []
global_high_low_flag = 0

nse = Nse()
pd.set_option('display.max_columns', None)

def save_list_to_file(list_name):
    with open("watchlist", 'wb') as handle:
        pickle.dump(list_name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_list_from_file(watchlist):
    with open(watchlist, 'rb') as handle:
        lst = pickle.load(handle)
        return lst

def get_strike_price_put(symbol,expiry_date):
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,str(expiry_date),"full")
        a = int(oi_data.iloc[oi_data["PUTS_Volume"].idxmax()]["Strike Price"])
    except:
        a=None
    return a

def get_strike_price_call(symbol,expiry_date):
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,str(expiry_date),"full")
        a = int(oi_data.iloc[oi_data["CALLS_Volume"].idxmax()]["Strike Price"])
    except:
        a=None
    return a

def get_call_put_option(symbol,expiry_date,expiry_month,current_year):
    #get_call_put_option("ZEEL","25-Aug-2022","AUG","22")
    sp_call = get_strike_price_call(symbol,expiry_date)
    sp_put = get_strike_price_put(symbol,expiry_date)
    #print(symbol+current_year+expiry_month+str(sp_call)+"CE")
    #print(symbol+current_year+expiry_month+str(sp_put)+"PE")
    call_symbol=symbol+current_year+expiry_month+str(sp_call)+"CE"
    put_symbol=symbol+current_year+expiry_month+str(sp_put)+"PE"
    return call_symbol,put_symbol

old_day_low = {}
old_day_high = {}

#NIFTYFNO=load_list_from_file("listtomonitor")
#print(len(NIFTYFNO))

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

#NIFTYFNO=['ABB', 'HONAUT', 'DALBHARAT', 'GODREJCP', 'BAJFINANCE', 'BAJAJFINSV', 'BRITANNIA', 'AUBANK', 'TRENT', 'GUJGASLTD', 'INTELLECT', 'HINDUNILVR', 'ESCORTS', 'DIXON', 'BATAINDIA', 'ICICIGI', 'CONCOR', 'APOLLOTYRE', 'WHIRLPOOL', 'EICHERMOT', 'RAMCOCEM', 'HINDPETRO', 'M&MFIN', 'SIEMENS', 'HEROMOTOCO', 'SBICARD', 'IDEA', 'ASIANPAINT', 'IEX', 'GODREJPROP', 'ZEEL', 'HAVELLS', 'CUMMINSIND', 'TITAN', 'MARUTI', 'UBL', 'COROMANDEL', 'ABBOTINDIA', 'BERGEPAINT', 'PERSISTENT', 'JKCEMENT', 'ABCAPITAL', 'LTTS', 'DELTACORP', 'AARTIIND', 'MRF', 'KOTAKBANK', 'BOSCHLTD', 'INDIACEM', 'TATACONSUM', 'LICHSGFIN', 'COLPAL', 'SHREECEM', 'BPCL', 'PAGEIND', 'SUNTV', 'RBLBANK', 'FSL', 'BAJAJ-AUTO', 'PIIND', 'GLENMARK', 'BIOCON', 'NAUKRI', 'M&M', 'ADANIPORTS', 'MGL', 'HDFCAMC', 'DLF', 'VOLTAS', 'OBEROIRLTY', 'IBULHSGFIN', 'L&TFH', 'MCDOWELL-N', 'NESTLEIND', 'INDUSTOWER', 'PIDILITIND', 'DABUR', 'MPHASIS', 'GMRINFRA', 'IPCALAB', 'MFSL', 'CANBK', 'OFSS', 'APOLLOHOSP', 'PETRONET', 'COFORGE', 'POLYCAB', 'ICICIPRULI', 'GRASIM', 'SBIN', 'BHEL', 'MINDTREE', 'LTI', 'TVSMOTOR', 'CROMPTON', 'AUROPHARMA', 'INDUSINDBK', 'BANDHANBNK', 'MARICO', 'ULTRACEMCO', 'IDFCFIRSTB', 'MOTHERSON', 'INDIGO', 'AMARAJABAT', 'TORNTPOWER', 'ALKEM', 'TCS', 'INDIAMART', 'LAURUSLABS', 'ACC', 'ASHOKLEY', 'METROPOLIS', 'IRCTC', 'HDFCBANK', 'NBCC', 'DEEPAKNTR', 'DIVISLAB', 'TATACOMM', 'HINDCOPPER', 'AXISBANK', 'NATIONALUM', 'JUBLFOOD', 'BHARTIARTL', 'IGL', 'TATAMOTORS', 'IDFC', 'ABFRL', 'ZYDUSLIFE', 'ICICIBANK', 'TATACHEM', 'INFY', 'BANKBARODA', 'RECLTD', 'UPL', 'ADANIENT', 'HDFC', 'BEL', 'TECHM', 'JINDALSTEL', 'GNFC', 'BALKRISIND', 'PEL', 'CIPLA', 'NAM-INDIA', 'NAVINFLUOR', 'FEDERALBNK', 'ITC', 'PNB', 'CANFINHOME', 'MANAPPURAM', 'WIPRO', 'EXIDEIND', 'MCX', 'TATAPOWER', 'CHAMBLFERT', 'HCLTECH', 'JSWSTEEL', 'SBILIFE', 'ASTRAL', 'AMBUJACEM', 'INDHOTEL', 'SUNPHARMA', 'SRF', 'TORNTPHARM', 'GSPL', 'LALPATHLAB', 'CUB', 'SRTRANSFIN', 'CHOLAFIN', 'GAIL', 'SAIL', 'LUPIN', 'RAIN', 'DRREDDY', 'PFC', 'TATASTEEL', 'MUTHOOTFIN', 'PVR', 'BHARATFORG', 'LT', 'SYNGENE', 'COALINDIA', 'GRANULES', 'HAL', 'ATUL', 'RELIANCE', 'NTPC', 'HDFCLIFE', 'HINDALCO', 'VEDL', 'BSOFT', 'IOC', 'POWERGRID', 'NMDC', 'BALRAMCHIN', 'ONGC']

def custom_sleep(n):
    while n:
        custom_sleep_1sec()
        n=n-1

def custom_sleep_1sec():
    i=10
    while i:
        pyautogui.click(400,120)
        time.sleep(0.1)
        i=i-1

def get_ohlc_dict(fnolist):
    '''
    fnolistnse = []
    for i in fnolist:
        tmp_symbol="NSE:"+i
        fnolistnse.append(tmp_symbol)
    #print(fnolistnse)
    '''
    ohlc_dict=kite.ohlc(fnolist)
    #print(ohlc_dict)
    return ohlc_dict

def get_ltp_dict(fnolist):
    '''
    fnolistnse = []
    for i in fnolist:
        tmp_symbol="NSE:"+i
        fnolistnse.append(tmp_symbol)
    #print(fnolistnse)
    '''
    ltp_dict=kite.ltp(fnolist)
    #print(ohlc_dict)
    return ltp_dict

def sentiment():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    total=len(NIFTYFNO)
    cnt=0
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #print(c)
        #print(o)
        if c>o:
            #print(symbol)
            cnt=cnt+1
            #print(cnt)
    fraction=cnt/total
    fraction=(int(fraction*100)/100)
    print("sentiment")
    print(fraction)
    return fraction

def is_trading_near_day_low(symbol):
    ohlc_dict = get_ohlc_dict(list(symbol))
    o=ohlc_dict[symbol]["ohlc"]["open"]
    l=ohlc_dict[symbol]["ohlc"]["low"]
    c=ohlc_dict[symbol]["last_price"]

    if c<(l-(l/10)):
        return True

def get_list_trading_near_day_xxx():
    trading_near={}
    trading_near_day_high=[]
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        trading_near[symbol]=(c/h)
    x=sorted(trading_near.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    trading_near_day_high=new_list[:5]
    trading_near_day_low=new_list[-5:]
    return trading_near_day_high,trading_near_day_low

def change_timeframe():
    time.sleep(1)
    pyautogui.click(760,127)
    time.sleep(1)
    pyautogui.click(750,280)
    time.sleep(3)
    pyautogui.click(760,127)
    time.sleep(3)
    pyautogui.click(760,410)
    time.sleep(3)

def get_list_trading_near_day_low():
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict["NSE:"+symbol]["ohlc"]["open"]
        h=ohlc_dict["NSE:"+symbol]["ohlc"]["high"]
        l=ohlc_dict["NSE:"+symbol]["ohlc"]["low"]
        c=ohlc_dict["NSE:"+symbol]["ohlc"]["close"]
        if c<l+(l/10):
            trading_near_day_low.append(symbol)
        return trading_near_day_low

    '''
    ohlc_dict = get_ohlc_dict(list(symbol))
    o=ohlc_dict[symbol]["ohlc"]["open"]
    l=ohlc_dict[symbol]["ohlc"]["low"]
    c=ohlc_dict[symbol]["last_price"]

    if c>(h-(h/10)):
        return True
    '''

'''
def stock_trading_near_day_low():
def stock_trading_near_day_high():
'''

def close_eq_low():
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if c==l:
            trading_near_day_low.append(symbol)
        return trading_near_day_low

def close_eq_high():
    trading_near_day_high=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if c==h:
            trading_near_day_high.append(symbol)
        return trading_near_day_high

def stock_after_correction():
    new_day_high(NIFTYFNO)
    new_day_low(NIFTYFNO)
    time.sleep(60)
    first_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    time.sleep(60)
    second_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    new_fno_list = list(set(first_list) - set(second_list))
    time.sleep(60)
    second_list=new_day_high(new_fno_list)+new_day_low(new_fno_list)
    print(second_list)

def new_day_high(NIFTYFNO):
    new_day_high_list=[]
    new_day_high_per_change={}
    global golbal_high_low
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    if bool(new_day_high_dic) == False:
        for symbol in NIFTYFNO:
            new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
    else:
        for symbol in NIFTYFNO:
            print(symbol)
            print(new_day_high_dic[symbol])
            print(ohlc_dict[symbol]["ohlc"]["high"])
            if new_day_high_dic[symbol]<ohlc_dict[symbol]["ohlc"]["high"] and symbol not in global_high_low:
                new_day_high_list.append(symbol)
                new_day_high_per_change[symbol]= ((ohlc_dict[symbol]["ohlc"]["close"] - new_day_high_dic[symbol])/new_day_high_dic[symbol])
                new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
    
    x=sorted(new_day_high_per_change.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    new_list.reverse()
    top_day_high_by_change=new_list[0:5]
    print(new_day_high_list)
    return top_day_high_by_change
    #return new_day_high_list

def new_day_low(NIFTYFNO):
    new_day_low_list=[]
    new_day_low_per_change={}
    global golbal_high_low
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    if bool(new_day_low_dic) == False:
        for symbol in NIFTYFNO:
            new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
    else:
        for symbol in NIFTYFNO:
            if new_day_low_dic[symbol]>ohlc_dict[symbol]["ohlc"]["low"] and symbol not in global_high_low:
                new_day_low_list.append(symbol)
                new_day_low_per_change[symbol]= ((ohlc_dict[symbol]["ohlc"]["close"] - new_day_low_dic[symbol])/new_day_low_dic[symbol])
                new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
   
    x=sorted(new_day_low_per_change.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    #new_list.reverse()
    top_day_low_by_change=new_list[0:5]
    
    return top_day_low_by_change
    #return new_day_low_list


def get_list_top_day_moribozu():
    day_moribozu_dict={}
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        day_moribozu_dict[symbol]=(abs(c-o)/(h-l))
    x=sorted(day_moribozu_dict.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    new_list.reverse()
    top_day_moribozu=new_list[0:4]
    print(top_day_moribozu)
    return top_day_moribozu

def get_list_top_day_moribozu_by_thersold():
    day_moribozu_dict={}
    day_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        factor=(abs(c-o)/(h-l))
        if factor > 0.97 and factor < 0.99:
            day_moribozu_list.append(symbol)
    return day_moribozu_list

def bull_side_moribozu():
    bull_moribozu_dict={}
    bull_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    top_g=top_gainer()
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #if c>o  and ((c-o)/(h-o))>0.9 and ((c-o)/(h-o))<0.99 and symbol in top_g:
        if c>o  and ((c-o)/(h-o))>0.97 and ((c-o)/(h-o))<0.998 and symbol not in global_high_low:
            bull_moribozu_list.append(symbol)
    return bull_moribozu_list

def bear_side_moribozu():
    bear_moribozu_dict={}
    bear_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    top_l=top_looser()
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #if o>c  and ((o-c)/(o-l))>0.9 and ((o-c)/(o-l))<0.99 and symbol in top_l:
        if o>c  and ((o-c)/(o-l))>0.97 and ((o-c)/(o-l))<0.998 and symbol not in global_high_low :
            bear_moribozu_list.append(symbol)
    return bear_moribozu_list


def get_per_change_dic(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change

def get_per_change_dic_morning(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            if per>1 or per<1:
                per=0
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change

def momentum_gainer():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    top_plus=[]
    top_minus=[]
    old_price={}
    momentum_dic={}
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        old_price[symbol]=c

    time.sleep(5)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        if old_price[symbol]/c > 1.002:
            top_plus.append(symbol)            		
        if old_price[symbol]/c < 0.008:
            top_plus.append(symbol)            		
    
    return top_plus+top_minus

def top_momentum():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    old_price={}
    momentum_dic={}
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        old_price[symbol]=c

    time.sleep(5)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        momentum_dic[symbol]= (old_price[symbol]/c)
   
    x=sorted(momentum_dic.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    top_plus=new_list[:2]
    top_minus=new_list[-2:]

    print(top_plus)
    print(top_minus)

        #print(ohlc_dict[symbol])
    return top_plus+top_minus

def top_gainer():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(20, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res

def top_looser():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    #print(per_change)
    res = nsmallest(20, per_change, key = per_change.get)
    #res.reverse()
    return res

def top_gainer_morning():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic_morning(kite_ohlc_dict)
    res = nlargest(10, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res

def top_looser_morning():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic_morning(kite_ohlc_dict)
    #print(per_change)
    res = nsmallest(5, per_change, key = per_change.get)
    #res.reverse()
    return res


def monitor_top_gainer():
    global already_top_gainer
    if len(already_top_gainer) == 0:
        already_top_gainer = top_gainer()
    new_top_gainer = top_gainer()
    new_element_enter = list(set(new_top_gainer) - set(already_top_gainer))
    print(new_element_enter)
    if len(new_element_enter) > 0:
        already_top_gainer.clear()
        already_top_gainer = new_top_gainer[:]
        print('buy signal...')
        print(datetime.datetime.now().time())
        print(new_element_enter[-1])
        return True
    return False

def monitor_top_looser():
    global already_top_looser
    if len(already_top_looser) == 0:
        already_top_looser = top_looser()
    new_top_looser = top_looser()
    new_element_enter = list(set(new_top_looser) - set(already_top_looser))
    print('already top looser...')
    print(already_top_looser)
    print('new top looser...')
    print(new_top_looser)
    print(new_element_enter)
    if len(new_element_enter) > 0:
        already_top_looser.clear()
        already_top_looser = new_top_looser[:]
        if is_trading_near_day_low(new_element_enter[-1]):
            print('sell signal...')
            print(datetime.datetime.now().time())
            print(new_element_enter[-1])
            return True
    return False

def save_screenshot_stock(stock):
    pyautogui.click(166,122)
    if "HDFC" in stock:
        stock = stock.replace('NSE:','')
        #time.sleep(2)
        print(stock)
        #custom_sleep(2)
    if "ICICIGI" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        time.sleep(2)
        #custom_sleep(2)
    if "CUB" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        #time.sleep(2)
        custom_sleep(2)
    if "RAIN" in stock:
        stock = stock.replace('NSE:','')
        #time.sleep(2)
        print(stock)
        custom_sleep(2)
    if ":LT" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        custom_sleep(2)
    if ":INDIGO" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        custom_sleep(2)
        #time.sleep(2)
    print(stock)
    time.sleep(1)
    pyautogui.typewrite(stock)
    #custom_sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(167,206)
    #pyautogui.typewrite(["enter"])
    time.sleep(1)
    time.sleep(2)
    #play_sound()
    #custom_sleep(1)
    #call_option,put_option=get_call_put_option(stock.replace('NSE:',''),"25-Aug-2022","AUG","22")
    #print(call_option)
    #print(put_option)
    #image = pyautogui.screenshot()
    #image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    #cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)
    #change_timeframe()

def save_screenshot(top_list):
    for stock in top_list:
        save_screenshot_stock(stock)
        '''
        time.sleep(2)
        pyautogui.click(470,45)
        save_screenshot_stock(stock)
        time.sleep(2)
        pyautogui.click(295,40)
        pyautogui.click(166,122)
        if "HDFC" in stock:
            stock = stock.replace('NSE:','')
            #time.sleep(2)
            print(stock)
            #custom_sleep(2)
        if "ICICIGI" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            time.sleep(2)
            #custom_sleep(2)
        if "CUB" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            #time.sleep(2)
            custom_sleep(2)
        if "RAIN" in stock:
            stock = stock.replace('NSE:','')
            #time.sleep(2)
            print(stock)
            custom_sleep(2)
        if ":LT" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            custom_sleep(2)
            #time.sleep(2)
        print(stock)
        time.sleep(1)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #custom_sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(1)
        #custom_sleep(1)
        #call_option,put_option=get_call_put_option(stock.replace('NSE:',''),"25-Aug-2022","AUG","22")
        #print(call_option)
        #print(put_option)
        #image = pyautogui.screenshot()
        #image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        #cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)
        #change_timeframe()
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

def save_screenshot_zebro(stock_list):
    for stock in stock_list:
        pyautogui.click(1450,93)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(1470,180)
        #pyautogui.typewrite(["enter"])
        time.sleep(2)

def is_nifty_green():
    nifty_dict = kite.ohlc('NSE:NIFTY 50')
    print(nifty_dict)
    o=nifty_dict['NSE:NIFTY 50']["ohlc"]["open"]
    h=nifty_dict['NSE:NIFTY 50']["ohlc"]["high"]
    l=nifty_dict['NSE:NIFTY 50']["ohlc"]["low"]
    c=kite.ltp('NSE:NIFTY 50')['NSE:NIFTY 50']["last_price"]

    if c>o:
        return True
    else:
        return False

def play_sound():
    duration = 0.2  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    time.sleep(3)

def clear_global_list():
    time = datetime.now()
    global global_high_low_flag
    m=time.minute

    if m%3 == 0 and global_high_low_flag == 0:
        global_high_low.clear()
        global_high_low_flag = 1
    if m%3 != 0 and global_high_low_flag == 1:
        global_high_low_flag = 0

def new_high_low():
    bull_trend=sentiment()
    if sentiment>0.6:
        return new_day_high(NIFTYFNO)
    elif sentiment<0.4:
        return new_day_low(NIFTYFNO)
    else:
        print("#### DONT TRADE RANGING MARKET ####")
        return None

def main_function(watchlist):
    #final_list=get_list_top_day_moribozu()+top_gainer()+top_looser()+watchlist
    #final_list=top_gainer()+top_looser()+watchlist
    #final_list=top_gainer()+top_looser()
    #print(top_gainer())
    #print(top_looser())
    #final_list=momentum_gainer()
    #final_list=close_eq_low()+close_eq_high()
    #final_list=close_eq_low()
    #final_list=top_looser()
    #final_list=get_list_top_day_moribozu()
    #final_list=get_list_top_day_moribozu_by_thersold()
    #final_list=top_momentum()
    #final_list=bull_side_moribozu()+bear_side_moribozu()
    #final_list=list(set(final_list))
    #day_high,day_low=get_list_trading_near_day_xxx()
    #print(day_high)
    #print(day_low)
    #final_list=day_high+day_low
    #final_list=top_gainer_morning()+top_looser_morning()
    #final_list=top_gainer()+top_looser()
    #print(final_list)
    #final_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    #final_list=new_high_low()
    #if len(final_list) > 0:
    #    play_sound()
    sentiment()
    #global_high_low.extend(final_list)
    #clear_global_list()
    #final_list=top_looser()
    #final_list=top_gainer()
    #final_list=day_high+day_low
    #final_set=set(final_list)
    #final_list=list(final_set)
    #shutil.rmtree("/home/pankaj/Pictures")
    #os.mkdir("/home/pankaj/Pictures")
    #print(final_list)
    try:
        #save_screenshot(final_list)
        print("")
    except:
        exit()
    #save_list_to_file(final_list)
    #save_screenshot(top_looser())
    #while monitor_top_gainer() == False:
    #print(top_looser())
    #print(top_gainer())
    #save_screenshot(top_looser())
    #save_screenshot(top_gainer())
    '''
    while monitor_top_looser() == False:
        print("... NO SIGNAL...")
        time.sleep(60)
     '''
while True:
    wl=[]
    if os.path.getsize("watchlist") > 0:
        wl=load_list_from_file("watchlist")
    main_function(wl)
    #t=get_time_to_wait()
    #time.sleep(10)
    time.sleep(5)
    #custom_sleep(2)
    #break

