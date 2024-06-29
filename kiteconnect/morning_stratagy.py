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



lot_size={'ABB': 250, 'HONAUT': 15, 'DALBHARAT': 500, 'GODREJCP': 1000, 'BAJFINANCE': 125, 'BAJAJFINSV': 500, 'BRITANNIA': 200, 'AUBANK': 1000, 'TRENT': 725, 'GUJGASLTD': 1250, 'INTELLECT': 750, 'HINDUNILVR': 300, 'ESCORTS': 550, 'DIXON': 125, 'BATAINDIA': 275, 'ICICIGI': 425, 'CONCOR': 1000, 'APOLLOTYRE': 3500, 'WHIRLPOOL': 350, 'EICHERMOT': 350, 'RAMCOCEM': 850, 'HINDPETRO': 2700, 'M&MFIN': 4000, 'SIEMENS': 275, 'HEROMOTOCO': 300, 'SBICARD': 800, 'ASIANPAINT': 200, 'IEX': 3750, 'GODREJPROP': 325, 'ZEEL': 3000, 'HAVELLS': 500, 'CUMMINSIND': 600, 'TITAN': 375, 'MARUTI': 100, 'UBL': 400, 'COROMANDEL': 700, 'ABBOTINDIA': 40, 'BERGEPAINT': 1100, 'PERSISTENT': 150, 'JKCEMENT': 250, 'ABCAPITAL': 5400, 'LTTS': 200, 'DELTACORP': 2300, 'AARTIIND': 850, 'MRF': 10, 'KOTAKBANK': 400, 'BOSCHLTD': 50, 'INDIACEM': 2900, 'TATACONSUM': 900, 'LICHSGFIN': 2000, 'COLPAL': 350, 'SHREECEM': 25, 'BPCL': 1800, 'PAGEIND': 15, 'SUNTV': 1500, 'RBLBANK': 5000, 'FSL': 5200, 'BAJAJ-AUTO': 250, 'PIIND': 250, 'GLENMARK': 1150, 'BIOCON': 2300, 'NAUKRI': 125, 'M&M': 700, 'ADANIPORTS': 1250, 'MGL': 800, 'HDFCAMC': 300, 'DLF': 1650, 'VOLTAS': 500, 'OBEROIRLTY': 700, 'IBULHSGFIN': 4000, 'L&TFH': 8924, 'MCDOWELL-N': 625, 'NESTLEIND': 40, 'INDUSTOWER': 2800, 'PIDILITIND': 250, 'DABUR': 1250, 'MPHASIS': 175, 'GMRINFRA': 22500, 'IPCALAB': 650, 'MFSL': 650, 'CANBK': 2700, 'OFSS': 200, 'APOLLOHOSP': 125, 'PETRONET': 3000, 'COFORGE': 150, 'POLYCAB': 300, 'ICICIPRULI': 1500, 'GRASIM': 475, 'SBIN': 1500, 'BHEL': 10500, 'MINDTREE': 200, 'LTI': 150, 'TVSMOTOR': 1400, 'CROMPTON': 1500, 'AUROPHARMA': 1000, 'INDUSINDBK': 900, 'BANDHANBNK': 1800, 'MARICO': 1200, 'ULTRACEMCO': 100, 'IDFCFIRSTB': 15000, 'MOTHERSON': 4500, 'INDIGO': 300, 'AMARAJABAT': 1000, 'TORNTPOWER': 1500, 'ALKEM': 200, 'TCS': 150, 'INDIAMART': 150, 'LAURUSLABS': 900, 'ACC': 250, 'ASHOKLEY': 5000, 'METROPOLIS': 300, 'IRCTC': 875, 'HDFCBANK': 550, 'DEEPAKNTR': 250, 'DIVISLAB': 150, 'TATACOMM': 500, 'HINDCOPPER': 4300, 'AXISBANK': 1200, 'NATIONALUM': 4250, 'JUBLFOOD': 1250, 'BHARTIARTL': 950, 'IGL': 1375, 'TATAMOTORS': 1425, 'IDFC': 10000, 'ABFRL': 2600, 'ZYDUSLIFE': 1800, 'ICICIBANK': 1375, 'TATACHEM': 1000, 'INFY': 300, 'BANKBARODA': 5850, 'RECLTD': 8000, 'UPL': 1300, 'ADANIENT': 500, 'HDFC': 300, 'BEL': 11400, 'TECHM': 600, 'JINDALSTEL': 1250, 'GNFC': 1300, 'BALKRISIND': 300, 'PEL': 275, 'CIPLA': 650, 'NAVINFLUOR': 225, 'FEDERALBNK': 10000, 'ITC': 3200, 'PNB': 16000, 'CANFINHOME': 975, 'MANAPPURAM': 6000, 'WIPRO': 1000, 'EXIDEIND': 3600, 'TATAPOWER': 3375, 'CHAMBLFERT': 1500, 'HCLTECH': 700, 'JSWSTEEL': 1350, 'SBILIFE': 750, 'ASTRAL': 275, 'AMBUJACEM': 1800, 'INDHOTEL': 4022, 'SUNPHARMA': 700, 'SRF': 375, 'TORNTPHARM': 500, 'GSPL': 2500, 'LALPATHLAB': 250, 'CUB': 5000, 'SRTRANSFIN': 600, 'CHOLAFIN': 1250, 'GAIL': 9150, 'SAIL': 6000, 'LUPIN': 850, 'RAIN': 3500, 'DRREDDY': 125, 'PFC': 6200, 'TATASTEEL': 4250, 'MUTHOOTFIN': 375, 'PVR': 407, 'BHARATFORG': 1000, 'LT': 300, 'SYNGENE': 1000, 'COALINDIA': 4200, 'GRANULES': 2000, 'HAL': 475, 'ATUL': 75, 'RELIANCE': 250, 'NTPC': 5700, 'HDFCLIFE': 1100, 'HINDALCO': 1075, 'VEDL': 1550, 'BSOFT': 1300, 'IOC': 9750, 'POWERGRID': 2700, 'NMDC': 3350, 'BALRAMCHIN': 1600, 'ONGC': 3850}

#lot_size = {'BANKNIFTY': 25, 'NIFTY': 50,'BALRAMCHIN': 1600, 'FINNIFTY': 40, 'ASTRAL': 275, 'AARTIIND': 850, 'ABBOTINDIA': 25, 'ACC': 250, 'ADANIENT': 500, 'ALKEM': 200, 'AMARAJABAT': 1000, 'AMBUJACEM': 1500, 'APLLTD': 550, 'APOLLOHOSP': 125, 'ASHOKLEY': 4500, 'AUBANK': 500, 'ATUL': 75, 'AUROPHARMA': 650, 'ADANIPORTS': 1250, 'BAJAJFINSV': 75, 'BAJFINANCE': 125, 'BALKRISIND': 300, 'BANDHANBNK': 1800, 'BATAINDIA': 550, 'BEL': 3800, 'BHARTIARTL': 1886, 'BHEL': 10500, 'BIOCON': 2300, 'AXISBANK': 1200, 'BPCL': 1800, 'CADILAHC': 1100, 'CANFINHOME': 975, 'CHOLAFIN': 1250, 'CIPLA': 650, 'COFORGE': 100, 'CUB': 3100, 'ASIANPAINT': 200, 'DABUR': 1250, 'DEEPAKNTR': 250, 'DIVISLAB': 100, 'DRREDDY': 125, 'GLENMARK': 1150, 'GODREJCP': 500, 'GODREJPROP': 325, 'GRANULES': 1550, 'GRASIM': 475, 'BSOFT': 1300, 'CANBK': 5400, 'HAL': 475, 'HAVELLS': 500, 'HCLTECH': 700, 'HDFCAMC': 300, 'HDFCBANK': 550, 'HINDALCO': 1075, 'CHAMBLFERT': 1500, 'HINDUNILVR': 300, 'BHARATFORG': 750, 'ICICIGI': 425, 'ICICIPRULI': 750, 'IDFCFIRSTB': 9500, 'BOSCHLTD': 50, 'IEX': 1250, 'INDHOTEL': 4022, 'EICHERMOT': 350, 'BRITANNIA': 200, 'FSL': 2600, 'INDIGO': 250, 'INFY': 300, 'IPCALAB': 225, 'GSPL': 1700, 'IRCTC': 1625, 'JSWSTEEL': 1350, 'JUBLFOOD': 1250, 'KOTAKBANK': 400, 'COALINDIA': 4200, 'L&TFH': 8924, 'LALPATHLAB': 125, 'LT': 575, 'LTI': 150, 'LTTS': 200, 'CROMPTON': 1100, 'MANAPPURAM': 3000, 'MARICO': 1000, 'CUMMINSIND': 600, 'MCDOWELL-N': 1250, 'METROPOLIS': 200, 'MGL': 600, 'DELTACORP': 2300, 'MINDTREE': 200, 'MPHASIS': 175, 'MRF': 10, 'MUTHOOTFIN': 375, 'NATIONALUM': 8500, 'ITC': 3200, 'DIXON': 125, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'NESTLEIND': 25, 'OFSS': 125, 'ONGC': 7700, 'PAGEIND': 30, 'PFC': 6200, 'PIIND': 250, 'LAURUSLABS': 900, 'POLYCAB': 300, 'POWERGRID': 5333, 'GAIL': 6100, 'PVR': 407, 'RAMCOCEM': 850, 'RECLTD': 6000, 'RELIANCE': 250, 'SAIL': 4750, 'GMRINFRA': 22500, 'SBILIFE': 750, 'SHREECEM': 25, 'GUJGASLTD': 1250, 'SRF': 625, 'SRTRANSFIN': 400, 'STAR': 675, 'SUNPHARMA': 700, 'TATAMOTORS': 2850, 'TATAPOWER': 6750, 'TCS': 150, 'HDFC': 300, 'TORNTPHARM': 250, 'TORNTPOWER': 1500, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 3100, 'VOLTAS': 500, 'HDFCLIFE': 1100, 'IBULHSGFIN': 3100, 'ICICIBANK': 1375, 'ABFRL': 2600, 'JKCEMENT': 250, 'RBLBANK': 2900, 'LUPIN': 850, 'M&MFIN': 4000, 'SBICARD': 500, 'MARUTI': 100,'TVSMOTOR': 1400, 'WHIRLPOOL': 250, 'OBEROIRLTY': 700, 'PEL': 275, 'PERSISTENT': 150, 'PFIZER': 125, 'BANKBARODA': 11700, 'BERGEPAINT': 1100, 'TATACONSUM': 675, 'TRENT': 725, 'COLPAL': 350, 'CONCOR': 1563, 'COROMANDEL': 625, 'DLF': 1650, 'ESCORTS': 550, 'EXIDEIND': 3600, 'FEDERALBNK': 10000, 'HEROMOTOCO': 300, 'HINDPETRO': 2700, 'APOLLOTYRE': 2500, 'IGL': 1375, 'INDIAMART': 75, 'IOC': 6500, 'JINDALSTEL': 2500, 'LICHSGFIN': 2000, 'DALBHARAT': 250, 'M&M': 700, 'MCX': 350, 'MFSL': 650, 'MOTHERSUMI': 3500, 'SUNTV': 1500, 'NMDC': 6700, 'NTPC': 5700, 'PETRONET': 3000, 'PIDILITIND': 250, 'PNB': 16000, 'SBIN': 1500, 'SIEMENS': 275, 'INDIACEM': 2900, 'SYNGENE': 850, 'TATASTEEL': 425, 'TECHM': 600, 'TITAN': 375, 'UBL': 350, 'ZEEL': 3000, 'TATACHEM': 1000, 'BAJAJ-AUTO': 250, 'INDUSTOWER': 2800, 'IDEA': 70000, 'WIPRO': 800, 'INDUSINDBK': 900}

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']


yesterday_top_gainer=['NSE:INDIACEM', 'NSE:BHARATFORG', 'NSE:PERSISTENT', 'NSE:IBULHSGFIN', 'NSE:HAL', 'NSE:JSWSTEEL', 'NSE:COALINDIA', 'NSE:VEDL', 'NSE:COFORGE', 'NSE:MOTHERSON', 'NSE:TVSMOTOR', 'NSE:SAIL', 'NSE:BALRAMCHIN', 'NSE:DEEPAKNTR', 'NSE:HINDALCO', 'NSE:ABB', 'NSE:JINDALSTEL', 'NSE:GNFC', 'NSE:PVR', 'NSE:DELTACORP']

yesterday_top_looser=['NSE:AUBANK', 'NSE:INDIGO', 'NSE:LUPIN', 'NSE:ONGC', 'NSE:BHARTIARTL', 'NSE:GRANULES', 'NSE:HINDUNILVR', 'NSE:BIOCON', 'NSE:CHOLAFIN', 'NSE:COLPAL', 'NSE:ICICIPRULI', 'NSE:GODREJCP', 'NSE:IGL', 'NSE:IPCALAB', 'NSE:DABUR', 'NSE:INDUSINDBK', 'NSE:BAJFINANCE', 'NSE:PIDILITIND', 'NSE:BRITANNIA', 'NSE:DIVISLAB']



max_pnl = {}

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

def convert_symbol_to_fut():
    lst=[]
    for symbol in NIFTYFNO:
        s=symbol.replace("NSE:","NFO:")+"22OCTFUT"
        #print(s)
        lst.append(s)
    return lst

def convert_fut_symbol_to_nse(lst):
    lst1=[]
    for symbol in lst:
        s=symbol.replace("NFO:","NSE:")
        s=s.replace("22OCTFUT","")
        lst1.append(s)
    return lst1

def top_gainer_future():
    NIFTYFNOFUT=convert_symbol_to_fut()
    print(NIFTYFNOFUT)
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNOFUT)
    #print(kite_ohlc_dict)
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(5, per_change, key = per_change.get)
    res = convert_fut_symbol_to_nse(res)
    #res.reverse()
    #print(res)
    return res

def top_looser_future():
    NIFTYFNOFUT=convert_symbol_to_fut()
    print(NIFTYFNOFUT)
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNOFUT)
    print(kite_ohlc_dict)
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nsmallest(5, per_change, key = per_change.get)
    res = convert_fut_symbol_to_nse(res)
    #res.reverse()
    #print(res)
    return res

def top_gainer():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(10, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res

def top_looser():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    #print(per_change)
    res = nsmallest(10, per_change, key = per_change.get)
    #res.reverse()
    return res

def morning_stratagy1():
    topg=top_gainer()
    topl=top_looser()
    remove_item=[]

    for stock in topg:
        if stock in yesterday_top_looser and stock in top_gainer_future() and stock.replace("NSE:","") not in list_of_open_position():
            symbol=stock.replace("NSE:","")+"22OCTFUT"
            print(stock)
            kite.place_order(variety='regular', exchange='NSE', tradingsymbol=stock.replace("NSE:",""),
            transaction_type='BUY', quantity=1, product='MIS', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

            #time.sleep(3)
            remove_item.append(stock)
            #if len(list_of_open_position()) > 0:
            #    exit()

            #buy
    for stock in topl:
        if stock in yesterday_top_gainer and stock in top_looser_future() and stock.replace("NSE:","") not in list_of_open_position():
            symbol=stock.replace("NSE:","")+"22OCTFUT"
            kite.place_order(variety='regular', exchange='NSE', tradingsymbol=stock.replace("NSE:",""),
            transaction_type='SELL', quantity=1, product='MIS', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
            #time.sleep(3)
            remove_item.append(stock)
            # if len(list_of_open_position()) > 0:
            #    exit()
            #sell

    for stock in remove_item:
        if stock in yesterday_top_gainer:
            yesterday_top_gainer.remove(stock)
    for stock in remove_item:
        if stock in yesterday_top_looser:
            yesterday_top_looser.remove(stock)

def morning_stratagy2():
    topg=top_gainer()
    topl=top_looser()
    remove_item=[]

    for stock in topg:
        if stock in yesterday_top_gainer:
            symbol=stock.replace("NSE:","")+"22OCTFUT"
            kite.place_order(variety='regular', exchange='NSE', tradingsymbol=stock.replace("NSE:",""),
            transaction_type='SELL', quantity=1, product='MIS', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

            #time.sleep(3)
            remove_item.append(stock)
            #if len(list_of_open_position()) > 0:
            #    exit()

            #buy
    for stock in topl:
        if stock in yesterday_top_looser:
            symbol=stock.replace("NSE:","")+"22OCTFUT"
            kite.place_order(variety='regular', exchange='NSE', tradingsymbol=stock.replace("NSE:",""),
            transaction_type='BUY', quantity=1, product='MIS', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
            #time.sleep(3)
            remove_item.append(stock)
            # if len(list_of_open_position()) > 0:
            #    exit()
            #sell

    for stock in remove_item:
        if stock in yesterday_top_gainer:
            yesterday_top_gainer.remove(stock)
    for stock in remove_item:
        if stock in yesterday_top_looser:
            yesterday_top_looser.remove(stock)


def get_quantity(stock):
    stock_name = stock.split('22')[0]
    for symbol in lot_size:
        if (stock_name == symbol):
            return lot_size[symbol]

def future_margin():
    ltp=kite.ltp("NFO:POLYCAB22OCTFUT")
    print(kite.ltp("NFO:POLYCAB22OCTFUT")["NFO:POLYCAB22OCTFUT"]["last_price"] * lot_size["POLYCAB"])

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
            global max_pnl
            if dic['tradingsymbol'] not in max_pnl:
                max_pnl[dic['tradingsymbol']] =  pnl
            
            if pnl > max_pnl[dic['tradingsymbol']]:
                max_pnl[dic['tradingsymbol']] = pnl
            
            if max_pnl[dic['tradingsymbol']] > 1000 and pnl < 500 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 1500 and pnl < 800 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 2000 and pnl < 1000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 5000 and pnl < 2000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 7000 and pnl < 5000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 10000 and pnl < 7000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 15000 and pnl < 12000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])


            if pnl < -500 or pnl > 10000:
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
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+2, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

def sell_fno_symbol(symbol,c):
    #c=ltp_fno_symbo(symbol)
    quantity = get_quantity(symbol)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='SELL', quantity=quantity, product='NRML', order_type='LIMIT', price=c-2, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    update_self(symbol)

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

    #if fno_symbol in list_of_open_position():
    #    return None

    if condition == "g":
        if c>price and action == "b":
            buy_fno_symbol(fno_symbol)
            update_self(fno_symbol)
        if c>price and action == "s":
            ltp_dic=get_open_position_price_dic()
            sell_fno_symbol(fno_symbol,ltp_dic[fno_symbol])

    if condition == 'l':
        if c<price and action == "b":
            buy_fno_symbol(fno_symbol)
            update_self(fno_symbol)
        if c<price and action == "s":
            ltp_dic=get_open_position_price_dic()
            sell_fno_symbol(fno_symbol,ltp_dic[fno_symbol])

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

def gen_lot_size_dic():
    lot_dic={}
    for stock in NIFTYFNO:
        ls=nse_get_fno_lot_sizes(stock.replace("NSE:",""))
        print(ls)
        lot_dic[stock]=ls
    print(lot_dic)

def read_order():
    if os.path.isfile("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt"):
        selffile = open("/home/pankaj/Documents/stocks/kiteconnect/order_book.py", "a")
        orderfile = open("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt", "r")
        selffile.write(orderfile.read())
        selffile.close()
        orderfile.close()
        os.system("rm readorder.txt")
        os.execv(sys.executable, ['python3'] + sys.argv)

while True:
    time.sleep(2)
    morning_stratagy1()
    #morning_stratagy2()
    print("pankaj")
    #read_order()
    #ltp_dict=get_ltp_dict(NIFTYFNO)
    #future_margin()
    #track_sl()
    #order("NSE:FEDERALBNK","g",124.4,"b","FEDERALBNK22SEP120CE",ltp_dict)
    #print(nse_get_fno_lot_sizes("mphasis"))
