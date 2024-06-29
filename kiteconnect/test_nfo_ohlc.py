from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np

fnolist =  ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BIOCON', 'BRITANNIA', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'BANKBARODA', 'CANBK', 'COFORGE', 'COLPAL', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'LTTS', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'SHREECEM', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'GUJGASLTD', 'MARICO', 'LICHSGFIN', 'NATIONALUM', 'MUTHOOTFIN', 'NMDC', 'RAMCOCEM', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'TORNTPHARM', 'TVSMOTOR', 'BOSCHLTD', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI', 'ZEEL', 'PEL', 'PNB', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'TORNTPOWER', 'VEDL', 'GMRINFRA', 'PFC', 'VOLTAS', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']

fnolistnse = []

def kite_get_ohlc(symbol):
    #symbol="NSE:"+symbol
    o=kite_ohlc_dict[symbol]["ohlc"]["open"]
    h=kite_ohlc_dict[symbol]["ohlc"]["high"]
    l=kite_ohlc_dict[symbol]["ohlc"]["low"]
    c=kite_ohlc_dict[symbol]["last_price"]

    return o,h,l,c

def print_all_ohlc(fnolist):
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        print(symbol)
        print(o)
        print(h)
        print(l)
        print(c)
        
def green_hammer(fnolist):
    gHammer = []
    for symbol in fnolist:
        print(symbol)
        o,h,l,c = kite_get_ohlc(symbol)
        print(c)
        if c>o and c> (h - ((h-l)/0.5)) and o > (h-((h-l)/2)): 
            gHammer.append(symbol)
    print("gHammer")
    print(gHammer)
    save_screenshot(gHammer,"green_hammer")

def inverted_red_hammer(fnolist):
    iHammer = []
    for symbol in fnolist:
        print(symbol)
        o,h,l,c = kite_get_ohlc(symbol)
        fraction = (h-l)/10
        print(c)
        if c<o and c<l+(l+fraction) and o< (l + (fraction*3)) :
            iHammer.append(symbol)
    print("iHammer")
    print(iHammer)
    save_screenshot(iHammer,"inverted_red_hammer")

def strong_bull(fnolist):
    sbull = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        if c>o and ((c-o)/(h-l)) > 0.6: 
            sbull.append(symbol)
    print("bull")
    print(sbull)
    save_screenshot(sbull,"strong_bull")

def strong_bear(fnolist):
    sbear = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        if o>c and ((o-c)/(h-l)) > 0.8:
            sbear.append(symbol)
    print("bear")
    print(sbear)
    save_screenshot(sbear,"strong_bear")


def get_key(my_dict,val):
    for key, value in my_dict.items():
         if val == value:
             return key

def minimum_candle(fnolist):
    m_candle = []
    candle_dict = {}
    factor_list=[]
    symbol_list=[]
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        factor = (((h-l)/l)*1000)
        candle_dict[symbol]=factor
        factor_list.append(factor)
        print(symbol)
        print(factor)

    factor_list=sorted(factor_list)
    factor_list = factor_list[:10]
    print(factor_list)
    for i in factor_list:
        k=get_key(candle_dict,i)
        symbol_list.append(k)
    save_screenshot(symbol_list,"min_candle")


def get_ohlc_dict(fnolist):
    for i in fnolist:
        tmp_symbol="NFO:"+i
        fnolistnse.append(tmp_symbol)
    ohlc_dict=kite.ohlc(fnolistnse)
    print(ohlc_dict)
    return ohlc_dict

def save_screenshot(stock_list,dir_name):
    full_dir_path = "/home/pankaj/Pictures/"+dir_name
    if os.path.isdir(full_dir_path):
        shutil.rmtree(full_dir_path)
    os.mkdir(full_dir_path)

    for stock in stock_list:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(1)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite(full_dir_path+"/"+stock+".png", image)



kite = set_token()

kite_ohlc_dict = get_ohlc_dict(fnolist)
print_all_ohlc(fnolistnse)
#green_hammer(fnolistnse)
#strong_bull(fnolistnse)
#strong_bear(fnolistnse)
#inverted_red_hammer(fnolistnse)
minimum_candle(fnolistnse)

#print(kite.ohlc(fnolistnse))
#ohlc_dict=kite.ohlc(fnolistnse)
#print_all_ohlc(fnolist)
#print(ohlc_dict["NSE:ZEEL"]["ohlc"]["open"])

#print(kite_get_ohlc(ohlc_dict,"HCLTECH"))
