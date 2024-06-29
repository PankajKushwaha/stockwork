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

lot_size = {'BANKNIFTY': 25, 'NIFTY': 50, 'FINNIFTY': 40, 'ASTRAL': 275, 'AARTIIND': 850, 'ABBOTINDIA': 25, 'ACC': 250, 'ADANIENT': 500, 'ALKEM': 200, 'AMARAJABAT': 1000, 'AMBUJACEM': 1500, 'APLLTD': 550, 'APOLLOHOSP': 125, 'ASHOKLEY': 4500, 'AUBANK': 500, 'ATUL': 75, 'AUROPHARMA': 650, 'ADANIPORTS': 1250, 'BAJAJFINSV': 75, 'BAJFINANCE': 125, 'BALKRISIND': 200, 'BANDHANBNK': 1800, 'BATAINDIA': 550, 'BEL': 3800, 'BHARTIARTL': 1886, 'BHEL': 10500, 'BIOCON': 2300, 'AXISBANK': 1200, 'BPCL': 1800, 'CADILAHC': 1100, 'CANFINHOME': 975, 'CHOLAFIN': 1250, 'CIPLA': 650, 'COFORGE': 100, 'CUB': 3100, 'ASIANPAINT': 150, 'DABUR': 1250, 'DEEPAKNTR': 250, 'DIVISLAB': 100, 'DRREDDY': 125, 'GLENMARK': 1150, 'GODREJCP': 500, 'GODREJPROP': 325, 'GRANULES': 1550, 'GRASIM': 475, 'BSOFT': 1300, 'CANBK': 5400, 'HAL': 475, 'HAVELLS': 500, 'HCLTECH': 700, 'HDFCAMC': 200, 'HDFCBANK': 550, 'HINDALCO': 1075, 'CHAMBLFERT': 1500, 'HINDUNILVR': 300, 'BHARATFORG': 750, 'ICICIGI': 425, 'ICICIPRULI': 750, 'IDFCFIRSTB': 9500, 'BOSCHLTD': 50, 'IEX': 1250, 'INDHOTEL': 4022, 'EICHERMOT': 350, 'BRITANNIA': 200, 'FSL': 2600, 'INDIGO': 250, 'INFY': 300, 'IPCALAB': 225, 'GSPL': 1700, 'IRCTC': 1625, 'JSWSTEEL': 1350, 'JUBLFOOD': 125, 'KOTAKBANK': 400, 'COALINDIA': 4200, 'L&TFH': 8924, 'LALPATHLAB': 125, 'LT': 575, 'LTI': 150, 'LTTS': 200, 'CROMPTON': 1100, 'MANAPPURAM': 3000, 'MARICO': 1000, 'CUMMINSIND': 600, 'MCDOWELL-N': 1250, 'METROPOLIS': 200, 'MGL': 600, 'DELTACORP': 2300, 'MINDTREE': 200, 'MPHASIS': 325, 'MRF': 10, 'MUTHOOTFIN': 375, 'NATIONALUM': 8500, 'ITC': 3200, 'DIXON': 125, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'NESTLEIND': 25, 'OFSS': 125, 'ONGC': 7700, 'PAGEIND': 30, 'PFC': 6200, 'PIIND': 250, 'LAURUSLABS': 900, 'POLYCAB': 300, 'POWERGRID': 5333, 'GAIL': 6100, 'PVR': 407, 'RAMCOCEM': 850, 'RECLTD': 6000, 'RELIANCE': 250, 'SAIL': 4750, 'GMRINFRA': 22500, 'SBILIFE': 750, 'SHREECEM': 25, 'GUJGASLTD': 1250, 'SRF': 625, 'SRTRANSFIN': 400, 'STAR': 675, 'SUNPHARMA': 700, 'TATAMOTORS': 2850, 'TATAPOWER': 6750, 'TCS': 150, 'HDFC': 300, 'TORNTPHARM': 250, 'TORNTPOWER': 1500, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 3100, 'VOLTAS': 500, 'HDFCLIFE': 1100, 'IBULHSGFIN': 3100, 'ICICIBANK': 1375, 'ABFRL': 2600, 'JKCEMENT': 175, 'RBLBANK': 2900, 'LUPIN': 850, 'M&MFIN': 4000, 'SBICARD': 500, 'MARUTI': 100, 'NAM-INDIA': 1600, 'TVSMOTOR': 1400, 'WHIRLPOOL': 250, 'OBEROIRLTY': 700, 'PEL': 275, 'PERSISTENT': 150, 'PFIZER': 125, 'BANKBARODA': 11700, 'BERGEPAINT': 1100, 'TATACONSUM': 675, 'TRENT': 725, 'COLPAL': 350, 'CONCOR': 1563, 'COROMANDEL': 625, 'DLF': 1650, 'ESCORTS': 550, 'EXIDEIND': 3600, 'FEDERALBNK': 10000, 'HEROMOTOCO': 300, 'HINDPETRO': 2700, 'APOLLOTYRE': 2500, 'IGL': 1375, 'INDIAMART': 75, 'IOC': 6500, 'JINDALSTEL': 2500, 'LICHSGFIN': 2000, 'DALBHARAT': 250, 'M&M': 700, 'MCX': 350, 'MFSL': 650, 'MOTHERSUMI': 3500, 'SUNTV': 1500, 'NMDC': 6700, 'NTPC': 5700, 'PETRONET': 3000, 'PIDILITIND': 250, 'PNB': 16000, 'SBIN': 1500, 'SIEMENS': 275, 'INDIACEM': 2900, 'SYNGENE': 850, 'TATASTEEL': 425, 'TECHM': 600, 'TITAN': 375, 'UBL': 350, 'ZEEL': 3000, 'TATACHEM': 1000, 'BAJAJ-AUTO': 250, 'INDUSTOWER': 2800, 'IDEA': 70000, 'WIPRO': 800, 'INDUSINDBK': 900}

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

def get_quantity(stock):
    stock_name = stock.split('22')[0]
    for symbol in lot_size:
        if (stock_name == symbol):
            return lot_size[symbol]

def get_open_position_price_dic():
    open_position_list = []
    open_position_price_dic = {}
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        open_position_list.append("NFO:"+dic['tradingsymbol'])
    ltp_list=kite.ltp(open_position_list)
    #print(kite.ltp(open_position_list))
    for symbol in ltp_list:
        open_position_price_dic[symbol.replace("NFO:","")]=ltp_list[symbol]['last_price']

    return open_position_price_dic

def track_sl():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        #print(dic['tradingsymbol'])
        #print(dic['quantity'])
        #print(int(dic['pnl']))
        #pnl=int(dic['pnl'])

        if dic['quantity']>0:
            ltp_dic=get_open_position_price_dic()
            
            pnl=(ltp_dic[dic['tradingsymbol']]*dic['quantity']) - (dic['quantity']*dic['average_price'])
            #print(pnl)
            if pnl < -1000 or pnl > 10000:
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
                time.sleep(5)

def get_ltp_dict(NIFTYFNO):
    ltp_dict=kite.ltp(NIFTYFNO)
    #print(ohlc_dict)
    return ltp_dict

def ltp_fno_symbo(symbol):
    ltp_dict=kite.ltp(["NFO:"+symbol])
    c=ltp_dict["NFO:"+symbol]["last_price"]
    return c

def buy_fno_symbol(symbol):
    c=ltp_fno_symbo(symbol)
    quantity = get_quantity(symbol)
    print(c)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+5, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

def sell_fno_symbol(symbol,c):
    #c=ltp_fno_symbo(symbol)
    quantity = get_quantity(symbol)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='SELL', quantity=quantity, product='NRML', order_type='LIMIT', price=c-5, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

def list_of_open_position():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        if dic['quantity'] > 0:
            open_position_list.append(dic['tradingsymbol'])
    return open_position_list

def order(symbol,condition,price,action,fno_symbol,ltp_dict):
    #ltp_dict=get_ltp_dict(NIFTYFNO)
    c=ltp_dict[symbol]["last_price"]

    if fno_symbol in list_of_open_position():
        return None

    if condition == "g":
        if c>price and action == "b":
            buy_fno_symbol(fno_symbol)
            update_self(fno_symbol)
        if c>price and action == "s":
            sell_fno_symbol(fno_symbol)

    if condition == 'l':
        if c<price and action == "b":
            buy_fno_symbol(fno_symbol)
            update_self(fno_symbol)
        if c<price and action == "s":
            sell_fno_symbol(fno_symbol)

def update_self(symbol):
    with open('order_book.py') as oldfile, open('order_new.py', 'w') as newfile:
        for line in oldfile:
            #print(line)
            if symbol not in line:
                newfile.write(line)
        newfile.close()
    os.system("cp order_new.py order_book.py")
    os.execv(sys.executable, ['python3'] + sys.argv)
    #os.execv(sys.argv[0], sys.argv)

while True:
    time.sleep(4)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    track_sl()
    #order("NSE:FEDERALBNK","g",124.4,"b","FEDERALBNK22SEP120CE",ltp_dict)
    order("NSE:CIPLA","l",1028.5,"b","CIPLA22SEP1020PE",ltp_dict)
    order("NSE:CIPLA","g",1036.5,"b","CIPLA22SEP1040CE",ltp_dict)
    order("NSE:JINDALSTEL","l",447.5,"b","JINDALSTEL22SEP440PE",ltp_dict)
    order("NSE:BANDHANBNK","l",306,"b","BANDHANBNK22SEP305PE",ltp_dict)
    order("NSE:MANAPPURAM","l",102.1,"b","MANAPPURAM22SEP100PE",ltp_dict)
