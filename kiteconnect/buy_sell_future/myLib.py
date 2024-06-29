from nsepython import *
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
from pynse import *
from pyautogui import *
import pandas as pd
from heapq import nlargest
from heapq import nsmallest
from datetime import datetime, timedelta
from pynput import keyboard
from dateutil.relativedelta import relativedelta
from threading import Thread, Lock
import concurrent.futures
    

def get_fno_list():
    lst=fnolist()
    lst.remove("NIFTYIT")
    lst.remove("NIFTY")
    lst.remove("BANKNIFTY")
    lst.remove("IDEA")
    lst.remove("MCX")
    #lst[0] = "NIFTY 50"
    #lst[1] = "NIFTY BANK"
    #print(lst)
    return lst

def get_fno_list_with_nse():
    lst=get_fno_list()
    modified_list = ["NSE:" + s for s in lst]
    return modified_list

def get_instrument_to_token(symbol_list):
    itt = {}
    ltpdic=kite.ltp(symbol_list)
    for symbol in ltpdic:
        itt[symbol]=ltpdic[symbol]["instrument_token"]
    return itt

def get_token_to_instrument(symbol_list):
    tti = {}
    ltpdic=kite.ltp(symbol_list)
    for symbol in ltpdic:
        tti[ltpdic[symbol]["instrument_token"]]=symbol
    return tti


def change_timeframe_min5():
    pyautogui.click(694, 129)
    time.sleep(1)
    pyautogui.click(689, 280)
    time.sleep(2)

def change_timeframe_day():
    pyautogui.click(694, 129)
    time.sleep(1)
    pyautogui.click(686, 547)
    time.sleep(2)

def get_ltp_dict():
    ltp_dict = {}
    tmp_dict=kite.ltp(["NSE:" + symbol for symbol in get_fno_list()])
    for i in tmp_dict:
        #print(i)
        #print(tmp_dict[i]["last_price"])
        ltp_dict[i] = tmp_dict[i]["last_price"]
    #print(ltp_dict)
    return ltp_dict

def get_ltp_dict(lst):
    ltp_dict = {}
    tmp_dict=kite.ltp(lst)
    for i in tmp_dict:
        #print(i)
        #print(tmp_dict[i]["last_price"])
        ltp_dict[i] = tmp_dict[i]["last_price"]
    #print(ltp_dict)
    return ltp_dict

def get_ohlc_dict():
    ohlc_dict = {}
    tmp_dict=kite.ohlc(["NSE:" + symbol for symbol in get_fno_list()])
    #print(tmp_dict)
    for i in tmp_dict:
        o=tmp_dict[i]["ohlc"]["open"]
        h=tmp_dict[i]["ohlc"]["high"]
        l=tmp_dict[i]["ohlc"]["low"]
        c=tmp_dict[i]["ohlc"]["close"]
        ohlc_dict[i]={"open":o,"high":h,"low":l,"close":c}
    return ohlc_dict

def get_symbol_to_token():
    token = {}
    tmp_dict=kite.ltp(["NSE:" + symbol for symbol in get_fno_list()])
    for i in tmp_dict:
        token[i] = tmp_dict[i]["instrument_token"]
    #print(token)
    return token 

symbol_to_token=get_symbol_to_token()


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

def get_ohlc_min5_nCandle_ago(candle,n):
    o=candle[-n]["open"]
    h=candle[-n]["high"]
    l=candle[-n]["low"]
    c=candle[-n]["close"]
    return o,h,l,c

def get_current_ohlc_min5(symbol):
    symbol="NSE:"+symbol.upper()
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:30:00"
    from_date=get_n_day_ago_date("5minute")
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
    #print(candle)
    o,h,l,c = get_ohlc_min5_nCandle_ago(candle,1)
    return o,h,l,c

def get_current_ohlc_day(symbol):
    symbol="NSE:"+symbol.upper()
    ohlc_dict = get_ohlc_dict()
    o=ohlc_dict[symbol]["open"]
    h=ohlc_dict[symbol]["high"]
    l=ohlc_dict[symbol]["low"]
    c=ohlc_dict[symbol]["close"]
    #print(ohlc_dict)
    
    return o,h,l,c

def get_ma(symbol,timeframe):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date(timeframe)
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200:])/200
    sma40 = sum(sma_list[-40:])/40
    sma20 = sum(sma_list[-20:])/20
    return sma20,sma40,sma200

def get_200ma_5minute(symbol):
    if symbol.startswith("NSE:"):
        sma20,sma40,sma200 = get_ma(symbol.upper() , "5minute" )
    else:
        sma20,sma40,sma200 = get_ma("NSE:"+symbol.upper() , "5minute" )
    return sma200

def get_20ma_5minute(symbol):
    if symbol.startswith("NSE:"):
        sma20,sma40,sma200 = get_ma(symbol.upper() , "5minute" )
    else:
        sma20,sma40,sma200 = get_ma("NSE:"+symbol.upper() , "5minute" )
    return sma20

def get_200ma_day(symbol):
    sma20,sma40,sma200 = get_ma("NSE:"+symbol.upper() , "day" )
    return sma200

def get_20ma_day(symbol):
    sma20,sma40,sma200 = get_ma("NSE:"+symbol.upper() , "day" )
    return sma20

def get_symbols_from_file(filename):
    symbols = []
    with open(filename) as file:
        tmp_symbols = [line.rstrip() for line in file]
        for symbol in tmp_symbols:
            if len(symbol)  > 0 and symbol[0] != "#" :
                symbols.append(symbol)
        return symbols

def save_screenshot(fnolst,path):
    for stock in fnolst:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(1)
        pyautogui.click(167,206)
        time.sleep(1)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite(path+stock+".png", image)

def get_symbols_from_file(filename):
    symbols = []
    with open(filename) as file:
        tmp_symbols = [line.rstrip() for line in file]
        for symbol in tmp_symbols:
            if symbol[0] != "#" :
                symbols.append(symbol)
        return symbols

#print(get_200ma_day("zyduslife"))
#print(get_20ma_day("zyduslife"))
#print(get_ohlc_dict())
#print(get_symbols_from_file("ma200_stocks.txt"))
#print(get_current_ohlc_day("zeel"))


