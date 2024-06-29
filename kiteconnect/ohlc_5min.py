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

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

ltp_dic = {}
low_dic = {}
high_dic = {}

time = datetime.now()
old_m=time.minute


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


def fill_ltp_dic():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict["NSE:"+symbol]["ohlc"]["open"]
        h=ohlc_dict["NSE:"+symbol]["ohlc"]["high"]
        l=ohlc_dict["NSE:"+symbol]["ohlc"]["low"]
        c=ohlc_dict["NSE:"+symbol]["ohlc"]["close"]
        ltp_dic[symbol].append(c)

    for symbol in NIFTYFNO:
        low_dic[symbol]=min(ltp_dic[symbol])
    for symbol in NIFTYFNO:
        low_dic[symbol]=max(ltp_dic[symbol])

    time = datetime.now()
    m=time.minute

    if m%5 == 0 and m != old_m:
        ltp_dic.clear()
        low_dic.clear()
        high_dic.clear()
        old_m = m


