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
from pynput import keyboard
from dateutil.relativedelta import relativedelta
from threading import Thread, Lock
import concurrent.futures

NIFTYFNO=['NSE:ABCAPITAL', 'NSE:APOLLOHOSP', 'NSE:ABFRL', 'NSE:ASIANPAINT', 'NSE:ACC', 'NSE:ASHOKLEY', 'NSE:BHARTIARTL', 'NSE:BAJAJ-AUTO', 'NSE:APOLLOTYRE', 'NSE:BALKRISIND', 'NSE:ASTRAL', 'NSE:ATUL', 'NSE:AXISBANK', 'NSE:BAJFINANCE', 'NSE:BIOCON', 'NSE:BRITANNIA', 'NSE:BALRAMCHIN', 'NSE:BANDHANBNK', 'NSE:BANKBARODA', 'NSE:BATAINDIA', 'NSE:BERGEPAINT', 'NSE:BHARATFORG', 'NSE:CANBK', 'NSE:RBLBANK', 'NSE:BHEL', 'NSE:CIPLA', 'NSE:COLPAL', 'NSE:BOSCHLTD', 'NSE:BPCL', 'NSE:BSOFT', 'NSE:CUMMINSIND', 'NSE:CANFINHOME', 'NSE:COALINDIA', 'NSE:CONCOR', 'NSE:COROMANDEL', 'NSE:FEDERALBNK', 'NSE:CUB', 'NSE:DIVISLAB', 'NSE:DLF', 'NSE:GODREJCP', 'NSE:ESCORTS', 'NSE:HAL', 'NSE:EXIDEIND', 'NSE:FSL', 'NSE:HDFC', 'NSE:GAIL', 'NSE:GLENMARK', 'NSE:GMRINFRA', 'NSE:HDFCBANK', 'NSE:HDFCLIFE', 'NSE:GODREJPROP', 'NSE:GRANULES', 'NSE:GRASIM', 'NSE:HEROMOTOCO', 'NSE:IDFC', 'NSE:HDFCAMC', 'NSE:INFY', 'NSE:HINDPETRO', 'NSE:IBULHSGFIN', 'NSE:ICICIBANK', 'NSE:IOC', 'NSE:ICICIPRULI', 'NSE:IDFCFIRSTB', 'NSE:IEX', 'NSE:IGL', 'NSE:INDIACEM', 'NSE:INDIAMART', 'NSE:JKCEMENT', 'NSE:INTELLECT', 'NSE:LT', 'NSE:LUPIN', 'NSE:IPCALAB', 'NSE:MANAPPURAM', 'NSE:JUBLFOOD', 'NSE:KOTAKBANK', 'NSE:MPHASIS', 'NSE:L&TFH', 'NSE:LALPATHLAB', 'NSE:LAURUSLABS', 'NSE:LICHSGFIN', 'NSE:NAUKRI', 'NSE:NESTLEIND', 'NSE:M&MFIN', 'NSE:MARICO', 'NSE:MCDOWELL-N', 'NSE:OFSS', 'NSE:MFSL', 'NSE:MGL', 'NSE:ONGC', 'NSE:ABBOTINDIA', 'NSE:MOTHERSON', 'NSE:MRF', 'NSE:NAVINFLUOR', 'NSE:OBEROIRLTY', 'NSE:PAGEIND', 'NSE:PEL', 'NSE:PFC', 'NSE:PIDILITIND', 'NSE:PNB', 'NSE:PETRONET', 'NSE:RECLTD', 'NSE:SBIN', 'NSE:SRF', 'NSE:TATAPOWER', 'NSE:TECHM', 'NSE:ZYDUSLIFE', 'NSE:POLYCAB',  'NSE:RAIN', 'NSE:ADANIENT', 'NSE:CHAMBLFERT', 'NSE:RELIANCE', 'NSE:SBICARD', 'NSE:SUNPHARMA', 'NSE:SUNTV', 'NSE:TATACHEM', 'NSE:TATACOMM', 'NSE:TATAMOTORS', 'NSE:TITAN', 'NSE:TORNTPOWER', 'NSE:TRENT', 'NSE:TVSMOTOR', 'NSE:UPL', 'NSE:WHIRLPOOL', 'NSE:WIPRO', 'NSE:ZEEL', 'NSE:ADANIPORTS', 'NSE:HINDALCO', 'NSE:AARTIIND', 'NSE:AMBUJACEM', 'NSE:INDIGO', 'NSE:AUROPHARMA', 'NSE:BAJAJFINSV', 'NSE:JSWSTEEL', 'NSE:AUBANK',  'NSE:COFORGE', 'NSE:CROMPTON', 'NSE:DABUR', 'NSE:DALBHARAT', 'NSE:DELTACORP', 'NSE:DIXON', 'NSE:EICHERMOT', 'NSE:GUJGASLTD', 'NSE:HAVELLS', 'NSE:HCLTECH', 'NSE:NATIONALUM', 'NSE:PERSISTENT', 'NSE:HINDUNILVR', 'NSE:HONAUT', 'NSE:INDHOTEL', 'NSE:SAIL', 'NSE:INDUSINDBK', 'NSE:TATASTEEL', 'NSE:IRCTC', 'NSE:JINDALSTEL', 'NSE:TORNTPHARM', 'NSE:LTTS', 'NSE:UBL', 'NSE:METROPOLIS', 'NSE:ALKEM', 'NSE:MUTHOOTFIN', 'NSE:DEEPAKNTR', 'NSE:POWERGRID', 'NSE:GNFC', 'NSE:SBILIFE', 'NSE:SHREECEM', 'NSE:SIEMENS', 'NSE:ICICIGI', 'NSE:SYNGENE', 'NSE:TATACONSUM', 'NSE:VOLTAS', 'NSE:INDUSTOWER', 'NSE:ITC', 'NSE:PIIND', 'NSE:ABB', 'NSE:BEL', 'NSE:CHOLAFIN', 'NSE:DRREDDY', 'NSE:MARUTI', 'NSE:HINDCOPPER', 'NSE:M&M', 'NSE:RAMCOCEM', 'NSE:NTPC', 'NSE:ULTRACEMCO', 'NSE:VEDL', 'NSE:NMDC', 'NSE:TCS']

symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}

ma19 = {}
ma199 = {}
redCandle = {}
greenCandle = {}
previousDayData = {}

def save_ma19(name):
    with open("ma19", 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_ma199(name):
    with open("ma199", 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_pdd(name):
    with open("pdd", 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_redCandle(name):
    with open("redCandle", 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_greenCandle(name):
    with open("greenCandle", 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_ma_from_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'rb') as handle:
            lst = pickle.load(handle)
            return lst
    else:
        return []

def get_n_day_ago_date(timeframe):
    if timeframe == "5minute":
        week_ago_2 = datetime.today() - relativedelta(days=14)
        from_date = week_ago_2.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "day":
        day_ago_400 = datetime.today() - relativedelta(days=400)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "hour":
        day_ago_400 = datetime.today() - relativedelta(days=400)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "month":
        day_ago_400 = datetime.today() - relativedelta(months=4)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date

def get_ma(symbol,timeframe):
    global redCandle
    global greenCandle
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date(timeframe)
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
    sma_list=[]
    print(symbol)
    for i in candle:
        c=i["close"]
        #print(c)
        sma_list.append(c)
    #sma199 = sum(sma_list[-200:-1])/199
    sma199 = sum(sma_list[-199:])/199
    #sma19 = sum(sma_list[-20:-1])/19
    sma19 = sum(sma_list[-19:])/19
    redC=get_num_of_red_candle(candle,7)
    greenC=7-redC
    print(symbol)
    print("red candle")
    print(redC)
    print(sma_list[-20:])
    #print((sma19*19+candle[-1]["close"])/20)
    pdd=getPreviousDayData(candle)
    previousDayData[symbol] = pdd
    return sma19,sma199,redC,greenC

def getPreviousDayData(candle):
    index=0
    data=[]
    for i in reversed(candle):
        c=i["close"]
        o=i["open"]
        h=i["high"]
        l=i["low"]
        index=index+1
        data.append((o,h,l,c))
        if index == 6:
            break
    return data

def preConditionBull(symbol):
    pdd=load_ma_from_file("pdd")
    o1=pdd[symbol][0][0]
    h1=pdd[symbol][0][1]
    l1=pdd[symbol][0][2]
    c1=pdd[symbol][0][3]
    o2=pdd[symbol][1][0]
    h2=pdd[symbol][1][1]
    l2=pdd[symbol][1][2]
    c2=pdd[symbol][1][3]
    if l1>l2 and h1>h2 and c1>o1 and c2>o2:
        return True

def preConditionBull(symbol):
    pdd=load_ma_from_file("pdd")
    o1=pdd[symbol][0][0]
    h1=pdd[symbol][0][1]
    l1=pdd[symbol][0][2]
    c1=pdd[symbol][0][3]
    o2=pdd[symbol][1][0]
    h2=pdd[symbol][1][1]
    l2=pdd[symbol][1][2]
    c2=pdd[symbol][1][3]
    if l1<l2 and h1<h2 and c1<o1 and c2<o2:
        return True

def get_num_of_red_candle(candle,n):
    index=0
    count=0
    for i in reversed(candle):
        c=i["close"]
        o=i["open"]
        index=index+1
        if c<o:
            count=count+1
        if index == 7:
            break
    return count

def get_ohlc_dict(fnolist):
    ohlc_dict=kite.ohlc(fnolist)
    return ohlc_dict

def get_ltp_dict(fnolist):
    ltp_dict=kite.ltp(fnolist)
    return ltp_dict

def validate_ma():
    ltp_dict=get_ltp_dict(NIFTYFNO)

    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    sma19=load_ma_from_file("ma19")
    sma199=load_ma_from_file("ma199")
    for symbol in NIFTYFNO:
        #c=ohlc_dict[symbol]["ohlc"]["close"]
        c=ltp_dict[symbol]["last_price"]
        ma20 = ((sma19[symbol]*19)+c)/20
        ma200 = ((sma199[symbol]*199)+c)/200
        print(symbol)
        print(ma20)
        print(ma200)

def validate_pdd():
    ltp_dict=get_ltp_dict(NIFTYFNO)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    pdd=load_ma_from_file("pdd")
    for symbol in NIFTYFNO:
        if preConditionBull(symbol)==True:
            print(symbol)
        #c=ohlc_dict[symbol]["ohlc"]["close"]

def main_func():
    for symbol in NIFTYFNO:
        print(symbol)
        sma19,sma199,redC,greenC=get_ma(symbol,"day")
        ma19[symbol]=sma19
        ma199[symbol]=sma199
        redCandle[symbol]=redC
        greenCandle[symbol]=greenC

    save_ma19(ma19)
    save_ma199(ma199)
    save_pdd(previousDayData)
    save_redCandle(redCandle)
    save_greenCandle(greenCandle)
    os.system("rm global_cross_ma*")

main_func()
#validate_pdd()
#validate_ma()
