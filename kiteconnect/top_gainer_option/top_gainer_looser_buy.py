from kiteconnect import KiteConnect
#from get_list_to_monitor import *
from set_token import *
import datetime
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
import click
import pickle
import time
import logging
from heapq import nlargest
from heapq import nsmallest

already_top_gainer = []
already_top_looser = []


#NIFTYFNO = list_to_monitor()

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:IDEA','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:NBCC','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:MCX','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

#NIFTYFNO=['ABB', 'HONAUT', 'DALBHARAT', 'GODREJCP', 'BAJFINANCE', 'BAJAJFINSV', 'BRITANNIA', 'AUBANK', 'TRENT', 'GUJGASLTD', 'INTELLECT', 'HINDUNILVR', 'ESCORTS', 'DIXON', 'BATAINDIA', 'ICICIGI', 'CONCOR', 'APOLLOTYRE', 'WHIRLPOOL', 'EICHERMOT', 'RAMCOCEM', 'HINDPETRO', 'M&MFIN', 'SIEMENS', 'HEROMOTOCO', 'SBICARD', 'IDEA', 'ASIANPAINT', 'IEX', 'GODREJPROP', 'ZEEL', 'HAVELLS', 'CUMMINSIND', 'TITAN', 'MARUTI', 'UBL', 'COROMANDEL', 'ABBOTINDIA', 'BERGEPAINT', 'PERSISTENT', 'JKCEMENT', 'ABCAPITAL', 'LTTS', 'DELTACORP', 'AARTIIND', 'MRF', 'KOTAKBANK', 'BOSCHLTD', 'INDIACEM', 'TATACONSUM', 'LICHSGFIN', 'COLPAL', 'SHREECEM', 'BPCL', 'PAGEIND', 'SUNTV', 'RBLBANK', 'FSL', 'BAJAJ-AUTO', 'PIIND', 'GLENMARK', 'BIOCON', 'NAUKRI', 'M&M', 'ADANIPORTS', 'MGL', 'HDFCAMC', 'DLF', 'VOLTAS', 'OBEROIRLTY', 'IBULHSGFIN', 'L&TFH', 'MCDOWELL-N', 'NESTLEIND', 'INDUSTOWER', 'PIDILITIND', 'DABUR', 'MPHASIS', 'GMRINFRA', 'IPCALAB', 'MFSL', 'CANBK', 'OFSS', 'APOLLOHOSP', 'PETRONET', 'COFORGE', 'POLYCAB', 'ICICIPRULI', 'GRASIM', 'SBIN', 'BHEL', 'MINDTREE', 'LTI', 'TVSMOTOR', 'CROMPTON', 'AUROPHARMA', 'INDUSINDBK', 'BANDHANBNK', 'MARICO', 'ULTRACEMCO', 'IDFCFIRSTB', 'MOTHERSON', 'INDIGO', 'AMARAJABAT', 'TORNTPOWER', 'ALKEM', 'TCS', 'INDIAMART', 'LAURUSLABS', 'ACC', 'ASHOKLEY', 'METROPOLIS', 'IRCTC', 'HDFCBANK', 'NBCC', 'DEEPAKNTR', 'DIVISLAB', 'TATACOMM', 'HINDCOPPER', 'AXISBANK', 'NATIONALUM', 'JUBLFOOD', 'BHARTIARTL', 'IGL', 'TATAMOTORS', 'IDFC', 'ABFRL', 'ZYDUSLIFE', 'ICICIBANK', 'TATACHEM', 'INFY', 'BANKBARODA', 'RECLTD', 'UPL', 'ADANIENT', 'HDFC', 'BEL', 'TECHM', 'JINDALSTEL', 'GNFC', 'BALKRISIND', 'PEL', 'CIPLA', 'NAM-INDIA', 'NAVINFLUOR', 'FEDERALBNK', 'ITC', 'PNB', 'CANFINHOME', 'MANAPPURAM', 'WIPRO', 'EXIDEIND', 'MCX', 'TATAPOWER', 'CHAMBLFERT', 'HCLTECH', 'JSWSTEEL', 'SBILIFE', 'ASTRAL', 'AMBUJACEM', 'INDHOTEL', 'SUNPHARMA', 'SRF', 'TORNTPHARM', 'GSPL', 'LALPATHLAB', 'CUB', 'SRTRANSFIN', 'CHOLAFIN', 'GAIL', 'SAIL', 'LUPIN', 'RAIN', 'DRREDDY', 'PFC', 'TATASTEEL', 'MUTHOOTFIN', 'PVR', 'BHARATFORG', 'LT', 'SYNGENE', 'COALINDIA', 'GRANULES', 'HAL', 'ATUL', 'RELIANCE', 'NTPC', 'HDFCLIFE', 'HINDALCO', 'VEDL', 'BSOFT', 'IOC', 'POWERGRID', 'NMDC', 'BALRAMCHIN', 'ONGC']

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
    trading_near_day_high=new_list[:10]
    trading_near_day_low=new_list[-10:]
    return trading_near_day_high,trading_near_day_low

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
    top_day_moribozu=new_list[0:10]
    print(top_day_moribozu)
    return top_day_moribozu

def get_per_change_dic(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        #print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change

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

def save_screenshot(top_list):
    for stock in top_list:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(2)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)

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

def main_function():
    #final_list=get_list_top_day_moribozu()
    #day_high,day_low=get_list_trading_near_day_xxx()
    #print(day_high)
    #print(day_low)
    #final_list=day_high+day_low+top_gainer()+top_looser()
    final_list=top_gainer()+top_looser()
    #final_list=day_high+day_low
    #final_set=set(final_list)
    #final_list=list(final_set)
    shutil.rmtree("/home/pankaj/Pictures")
    os.mkdir("/home/pankaj/Pictures")
    save_screenshot(final_list[:5])
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
    main_function()
    time.sleep(2)

