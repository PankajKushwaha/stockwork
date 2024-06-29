from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
from heapq import nlargest
import click

fnolist = ['AUROPHARMA21NOV670PE', 'AARTIIND21NOV900PE', 'ADANIENT21NOV1700PE', 'ADANIPORTS21NOV750PE', 'AMARAJABAT21NOV680PE', 'AMBUJACEM21NOV400PE', 'APLLTD21NOV750PE', 'APOLLOHOSP21NOV5000PE', 'APOLLOTYRE21NOV230PE', 'ASHOKLEY21NOV145PE', 'ASIANPAINT21NOV3100PE', 'AUBANK21NOV1200PE', 'AXISBANK21NOV730PE', 'BAJAJFINSV21NOV18000PE', 'BEL21NOV220PE', 'BERGEPAINT21NOV800PE', 'BHARATFORG21NOV780PE', 'BHEL21NOV60PE', 'BIOCON21NOV350PE', 'BRITANNIA21NOV3700PE', 'CADILAHC21NOV490PE', 'CHOLAFIN21NOV640PE', 'COALINDIA21NOV160PE', 'CONCOR21NOV680PE', 'CUMMINSIND21NOV800PE', 'BANKBARODA21NOV100PE', 'CANBK21NOV220PE', 'COFORGE21NOV5600PE', 'COLPAL21NOV1500PE', 'DEEPAKNTR21NOV2300PE', 'DIVISLAB21NOV4900PE', 'DLF21NOV420PE', 'FEDERALBNK21NOV95PE', 'DRREDDY21NOV4800PE', 'EICHERMOT21NOV2600PE', 'GAIL21NOV145PE', 'GLENMARK21NOV500PE', 'GODREJCP21NOV900PE', 'GODREJPROP21NOV2300PE', 'GRANULES21NOV300PE', 'GRASIM21NOV1800PE', 'HCLTECH21NOV1100PE', 'HDFC21NOV2900PE', 'HDFCAMC21NOV2650PE', 'HDFCBANK21NOV1540PE', 'HEROMOTOCO21NOV2700PE', 'HINDALCO21NOV450PE', 'HINDPETRO21NOV340PE', 'HINDUNILVR21NOV2400PE', 'ICICIBANK21NOV770PE', 'ICICIPRULI21NOV650PE', 'INDIGO21NOV2200PE', 'INDUSTOWER21NOV280PE', 'IOC21NOV130PE', 'ITC21NOV230PE', 'JINDALSTEL21NOV390PE', 'JSWSTEEL21NOV600PE', 'JUBLFOOD21NOV4000PE', 'KOTAKBANK21NOV2000PE', 'L&TFH21NOV80PE', 'LT21NOV1940PE', 'LTTS21NOV5200PE', 'M&M21NOV900PE', 'M&MFIN21NOV180PE', 'MANAPPURAM21NOV190PE', 'MARUTI21NOV8000PE', 'MCDOWELL-N21NOV940PE', 'MFSL21NOV960PE', 'MGL21NOV1000PE', 'MOTHERSUMI21NOV240PE', 'MPHASIS21NOV3000PE', 'MRF21NOV75000PE', 'NAM-INDIA21NOV400PE', 'NAUKRI21NOV6000PE', 'NAVINFLUOR21NOV3500PE', 'NESTLEIND21NOV19000PE', 'NTPC21NOV130PE', 'ONGC21NOV150PE', 'PAGEIND21NOV40000PE', 'PETRONET21NOV230PE', 'PFIZER21NOV5200PE', 'PIDILITIND21NOV2400PE', 'PIIND21NOV2800PE', 'PVR21NOV1700PE', 'RBLBANK21NOV200PE', 'RELIANCE21NOV2500PE', 'MINDTREE21NOV4900PE', 'SBIN21NOV500PE', 'SHREECEM21NOV27000PE', 'SRTRANSFIN21NOV1600PE', 'SUNPHARMA21NOV810PE', 'SUNTV21NOV550PE', 'TATACHEM21NOV900PE', 'TATAMOTORS21NOV500PE', 'TATAPOWER21NOV220PE', 'TCS21NOV3500PE', 'TECHM21NOV1560PE', 'UBL21NOV1700PE', 'ULTRACEMCO21NOV8000PE', 'UPL21NOV780PE', 'WIPRO21NOV660PE', 'ACC21NOV2500PE', 'ALKEM21NOV3500PE', 'BAJFINANCE21NOV7500PE', 'BALKRISIND21NOV2300PE', 'BANDHANBNK21NOV300PE', 'BATAINDIA21NOV2200PE', 'BHARTIARTL21NOV730PE', 'HDFCLIFE21NOV700PE', 'CUB21NOV160PE', 'EXIDEIND21NOV180PE', 'ICICIGI21NOV1500PE', 'IDFCFIRSTB21NOV50PE', 'IGL21NOV500PE', 'INDUSINDBK21NOV1000PE', 'IRCTC21NOV900PE', 'LUPIN21NOV900PE', 'GUJGASLTD21NOV650PE', 'MARICO21NOV550PE', 'LICHSGFIN21NOV420PE', 'MUTHOOTFIN21NOV1660PE', 'NMDC21NOV140PE', 'RAMCOCEM21NOV1000PE', 'SBILIFE21NOV1160PE', 'SRF21NOV2100PE', 'TATACONSUM21NOV840PE', 'TATASTEEL21NOV1240PE', 'SIEMENS21NOV2300PE', 'TITAN21NOV2500PE', 'TRENT21NOV1100PE', 'TORNTPHARM21NOV2800PE', 'TVSMOTOR21NOV700PE', 'BOSCHLTD21NOV18000PE', 'CIPLA21NOV920PE', 'HAVELLS21NOV1360PE', 'INFY21NOV1780PE', 'LALPATHLAB21NOV3600PE', 'LTI21NOV7000PE', 'PEL21NOV2600PE', 'POWERGRID21NOV185PE', 'RECLTD21NOV140PE', 'BAJAJ-AUTO21NOV3600PE', 'TORNTPOWER21NOV540PE', 'VEDL21NOV330PE', 'GMRINFRA21NOV40PE', 'PFC21NOV130PE', 'VOLTAS21NOV1240PE', 'BPCL21NOV420PE', 'DABUR21NOV600PE', 'IDEA21NOV9PE', 'ABFRL21NOV290PE', 'COROMANDEL21NOV780PE', 'INDHOTEL21NOV220PE', 'METROPOLIS21NOV3000PE']

lot_size = {'BANKNIFTY': 25, 'NIFTY': 50, 'FINNIFTY': 40, 'ASTRAL': 275, 'AARTIIND': 850, 'ABBOTINDIA': 25, 'ACC': 250, 'ADANIENT': 500, 'ALKEM': 200, 'AMARAJABAT': 1000, 'AMBUJACEM': 1500, 'APLLTD': 550, 'APOLLOHOSP': 125, 'ASHOKLEY': 4500, 'AUBANK': 500, 'ATUL': 75, 'AUROPHARMA': 650, 'ADANIPORTS': 1250, 'BAJAJFINSV': 75, 'BAJFINANCE': 125, 'BALKRISIND': 200, 'BANDHANBNK': 1800, 'BATAINDIA': 550, 'BEL': 3800, 'BHARTIARTL': 1886, 'BHEL': 10500, 'BIOCON': 2300, 'AXISBANK': 1200, 'BPCL': 1800, 'CADILAHC': 1100, 'CANFINHOME': 975, 'CHOLAFIN': 1250, 'CIPLA': 650, 'COFORGE': 100, 'CUB': 3100, 'ASIANPAINT': 150, 'DABUR': 1250, 'DEEPAKNTR': 250, 'DIVISLAB': 100, 'DRREDDY': 125, 'GLENMARK': 1150, 'GODREJCP': 500, 'GODREJPROP': 325, 'GRANULES': 1550, 'GRASIM': 475, 'BSOFT': 1300, 'CANBK': 5400, 'HAL': 475, 'HAVELLS': 500, 'HCLTECH': 700, 'HDFCAMC': 200, 'HDFCBANK': 550, 'HINDALCO': 1075, 'CHAMBLFERT': 1500, 'HINDUNILVR': 300, 'BHARATFORG': 750, 'ICICIGI': 425, 'ICICIPRULI': 750, 'IDFCFIRSTB': 9500, 'BOSCHLTD': 50, 'IEX': 1250, 'INDHOTEL': 4022, 'EICHERMOT': 350, 'BRITANNIA': 200, 'FSL': 2600, 'INDIGO': 250, 'INFY': 300, 'IPCALAB': 225, 'GSPL': 1700, 'IRCTC': 1625, 'JSWSTEEL': 1350, 'JUBLFOOD': 125, 'KOTAKBANK': 400, 'COALINDIA': 4200, 'L&TFH': 8924, 'LALPATHLAB': 125, 'LT': 575, 'LTI': 150, 'LTTS': 200, 'CROMPTON': 1100, 'MANAPPURAM': 3000, 'MARICO': 1000, 'CUMMINSIND': 600, 'MCDOWELL-N': 1250, 'METROPOLIS': 200, 'MGL': 600, 'DELTACORP': 2300, 'MINDTREE': 200, 'MPHASIS': 325, 'MRF': 10, 'MUTHOOTFIN': 375, 'NATIONALUM': 8500, 'ITC': 3200, 'DIXON': 125, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'NESTLEIND': 25, 'OFSS': 125, 'ONGC': 7700, 'PAGEIND': 30, 'PFC': 6200, 'PIIND': 250, 'LAURUSLABS': 900, 'POLYCAB': 300, 'POWERGRID': 5333, 'GAIL': 6100, 'PVR': 407, 'RAMCOCEM': 850, 'RECLTD': 6000, 'RELIANCE': 250, 'SAIL': 4750, 'GMRINFRA': 22500, 'SBILIFE': 750, 'SHREECEM': 25, 'GUJGASLTD': 1250, 'SRF': 625, 'SRTRANSFIN': 400, 'STAR': 675, 'SUNPHARMA': 700, 'TATAMOTORS': 2850, 'TATAPOWER': 6750, 'TCS': 150, 'HDFC': 300, 'TORNTPHARM': 250, 'TORNTPOWER': 1500, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 3100, 'VOLTAS': 500, 'HDFCLIFE': 1100, 'IBULHSGFIN': 3100, 'ICICIBANK': 1375, 'ABFRL': 2600, 'JKCEMENT': 175, 'RBLBANK': 2900, 'LUPIN': 850, 'M&MFIN': 4000, 'SBICARD': 500, 'MARUTI': 100, 'NAM-INDIA': 1600, 'TVSMOTOR': 1400, 'WHIRLPOOL': 250, 'OBEROIRLTY': 700, 'PEL': 275, 'PERSISTENT': 150, 'PFIZER': 125, 'BANKBARODA': 11700, 'BERGEPAINT': 1100, 'TATACONSUM': 675, 'TRENT': 725, 'COLPAL': 350, 'CONCOR': 1563, 'COROMANDEL': 625, 'DLF': 1650, 'ESCORTS': 550, 'EXIDEIND': 3600, 'FEDERALBNK': 10000, 'HEROMOTOCO': 300, 'HINDPETRO': 2700, 'APOLLOTYRE': 2500, 'IGL': 1375, 'INDIAMART': 75, 'IOC': 6500, 'JINDALSTEL': 2500, 'LICHSGFIN': 2000, 'DALBHARAT': 250, 'M&M': 700, 'MCX': 350, 'MFSL': 650, 'MOTHERSUMI': 3500, 'SUNTV': 1500, 'NMDC': 6700, 'NTPC': 5700, 'PETRONET': 3000, 'PIDILITIND': 250, 'PNB': 16000, 'SBIN': 1500, 'SIEMENS': 275, 'INDIACEM': 2900, 'SYNGENE': 850, 'TATASTEEL': 425, 'TECHM': 600, 'TITAN': 375, 'UBL': 350, 'ZEEL': 3000, 'TATACHEM': 1000, 'BAJAJ-AUTO': 250, 'INDUSTOWER': 2800, 'IDEA': 70000, 'WIPRO': 800, 'INDUSINDBK': 900}


fnolistnse = []


def get_quantity(stock):
    stock_name = stock.split('21')[0]
    for symbol in lot_size:
        if (stock_name == symbol):
            return lot_size[symbol]

def placeGTT(symbol,quantity,sl_price, target, ltp):
    order_dict = [{"transaction_type": kite.TRANSACTION_TYPE_SELL, "quantity": quantity, 
                   'order_type': kite.ORDER_TYPE_LIMIT, "product": kite.PRODUCT_NRML , "price": sl_price}, 
                  {"transaction_type": kite.TRANSACTION_TYPE_SELL, "quantity": quantity, 
                   'order_type': kite.ORDER_TYPE_LIMIT, "product": kite.PRODUCT_NRML , "price": target} 
                  ]
    kite.place_gtt(kite.GTT_TYPE_OCO, symbol, kite.EXCHANGE_NFO, [sl_price, target], ltp, order_dict)

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

def buy_option(symbol,c):
    stock_bear=symbol
    stock_bear = stock_bear.replace('NFO:','')
    quantity=get_quantity(stock_bear)
    print(quantity)
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bear,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+10, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    placeGTT(stock_bear,quantity,c/2, c+30, c)

def check_and_buy(stock_list):
    for stock in stock_list:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(2)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        time.sleep(2)
        pyautogui.moveTo(145,645)
        pyautogui.click(145,645)
        char = click.prompt('Please enter a char', type=str)
        if char == "c":
            continue
        if char == "e":
            break
        if char == "b":
            try:
                o,h,l,c = kite_get_ohlc(stock)
                buy_option(stock,c)
            except:
                pass


def buy_stock_max_bear(fnolist):
    sbear = []
    stock_per_change = {}
    for symbol in fnolist:
        try:
            o,h,l,c = kite_get_ohlc(symbol)
        except:
            pass
        if o != 0:
            try:
                per_change = ((c-o)/(h-l))*100
                #per_change = ((c-o)/o)*100
                stock_per_change[symbol]=per_change
            except:
                pass

    stock_bear = max(stock_per_change, key=stock_per_change.get)
    o,h,l,c = kite_get_ohlc(stock_bear)
    print(stock_bear)
    stock_bear = stock_bear.replace('NFO:','')
    #quantity=int(10000/(c/5))
    #print(quantity)
    quantity = get_quantity(stock_bear)
    print(quantity)
    res = nlargest(10, stock_per_change, key = stock_per_change.get)
    res.reverse()
    print(res)
    check_and_buy(res)
    '''
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bear,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+10, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    placeGTT(stock_bear,quantity,c/2, c+30, c)
    '''
    #print(stock_bear)


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
buy_stock_max_bear(fnolistnse)

