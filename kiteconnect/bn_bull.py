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
from datetime import datetime, timedelta,date
from pynput import keyboard
from dateutil.relativedelta import relativedelta,TH

expirty_date=0
number_of_lot=1
lot_size=25
call_price_symbol=""
put_price_symbol=""
banknifty_token = 260105
time_to_wait=1

def get_candle():
    week_ago_2 = datetime.today() - relativedelta(days=14)
    from_date = week_ago_2.strftime('%Y-%m-%d') + " 00:00:00"
    date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:25:00"
    candle = kite.historical_data(banknifty_token, from_date, to_date,"5minute", continuous=False, oi=False)
    return candle

def get_sma(candle):
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200:])/200
    sma40 = sum(sma_list[-40:])/40
    sma20 = sum(sma_list[-20:])/20
    '''
    print("sma20")
    print(sma20)
    print("sma40")
    print(sma40)
    print("sma200")
    print(sma200)
    '''
    return sma20,sma40,sma200

def get_expiry_date():
    todayDate = date.today()
    nextThursday = todayDate + relativedelta(weekday=TH(1))
    print("The Next Thursday date:", nextThursday)
    print("The Next Thursday date:", str(nextThursday).split("-")[-1])
    nextThursday=str(nextThursday).split("-")[-1]
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    cy=str(currentYear)[-2:]
    print(currentMonth)
    ed=nextThursday+str(currentMonth)+cy
    ed=cy+str(currentMonth)+nextThursday
    print(ed)
    return ed

def get_call_put_option_symbol():
    global call_price_symbol
    global put_price_symbol
    if len(call_price_symbol) == 0:
        ed=get_expiry_date()
        ltp=kite.ltp("NSE:NIFTY BANK")["NSE:NIFTY BANK"]["last_price"]
        ltp=int(ltp)
        while True:
            ltp=ltp+1
            if ltp%100 == 0:
                call_price=ltp
                break
        while True:
            ltp=ltp-1
            if ltp%100 == 0:
                put_price=ltp
                break
        call_price_symbol="BANKNIFTY"+str(ed)+str(call_price)+"CE"
        put_price_symbol="BANKNIFTY"+str(ed)+str(put_price)+"PE"
        return call_price_symbol,put_price_symbol
    else:
        return call_price_symbol,put_price_symbol

def get_last_5min_ohlc(candle):
    #print(candle)
    o=candle[-2]["open"]
    h=candle[-2]["high"]
    l=candle[-2]["low"]
    c=candle[-2]["close"]
    return o,h,l,c

def buy_fno_symbol(symbol):
    quantity=lot_size*number_of_lot
    print(symbol)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

def bull_buy_ma20(sma20,o,h,l,c,ltp,call_symbol):
    if o>sma20 and l<sma20 and c>o and ltp >sma20:
        buy_fno_symbol(call_symbol)
        print(call_symbol)
        print(l)
        exit()

def bear_buy_ma20(sma20,o,h,l,c,ltp,put_symbol):
    if o<sma20 and h>sma20 and c<o and ltp <sma20:
        buy_fno_symbol(put_symbol)
        print(put_symbol)
        print(h)
        exit()

def bull_buy_ma40(sma40,o,h,l,c,ltp,call_symbol):
    if o>sma40 and l<sma40 and c>o and ltp >sma40:
        buy_fno_symbol(call_symbol)
        print(call_symbol)
        print(l)
        exit()

def bear_buy_ma40(sma40,o,h,l,c,ltp,put_symbol):
    if o<sma40 and h>sma40 and c<o and ltp <sma40:
        buy_fno_symbol(put_symbol)
        print(put_symbol)
        print(h)
        exit()

def bull_buy_ma200(sma200,o,h,l,c,ltp,call_symbol):
    if o>sma200 and l<sma200 and c>o and ltp >sma200:
        buy_fno_symbol(call_symbol)
        print(call_symbol)
        print(l)
        exit()

def bear_buy_ma200(sma200,o,h,l,c,ltp,put_symbol):
    if o<sma200 and h>sma200 and c<o and ltp <sma200:
        buy_fno_symbol(put_symbol)
        print(put_symbol)
        print(h)
        exit()

def buy_option(o,h,l,c,call_symbol,put_symbol):
    if c>o:
        buy_fno_symbol(call_symbol)
    if c<o:
        buy_fno_symbol(put_symbol)
    exit()

#print(get_sma(get_candle()))
#get_expiry_date()
#get_call_put_option_symbol()
#get_last_5min_ohlc(get_candle())

def main_function():
    candle=get_candle()
    ltp=kite.ltp("NSE:NIFTY BANK")["NSE:NIFTY BANK"]["last_price"]
    call_symbol,put_symbol=get_call_put_option_symbol()
    #sma20,sma40,sma200=get_sma(candle)
    o,h,l,c=get_last_5min_ohlc(candle)
    if ltp>h:
        buy_fno_symbol(call_symbol)
        exit()

    '''
    bull_buy_ma20(sma20,o,h,l,c,ltp,call_symbol)
    #bear_buy_ma20(sma20,o,h,l,c,ltp,put_symbol)
    bull_buy_ma40(sma40,o,h,l,c,ltp,call_symbol)
    #bear_buy_ma40(sma40,o,h,l,c,ltp,put_symbol)
    bull_buy_ma200(sma200,o,h,l,c,ltp,call_symbol)
    #bear_buy_ma200(sma200,o,h,l,c,ltp,put_symbol)
    #buy_option(o,h,l,c,call_symbol,put_symbol)
    '''
while True:
    time.sleep(time_to_wait)
    main_function()
