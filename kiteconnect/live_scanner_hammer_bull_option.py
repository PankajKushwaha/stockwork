from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
import click
from heapq import nlargest

fnolist = ['AUROPHARMA21NOV700CE', 'AARTIIND21NOV1000CE', 'ADANIENT21NOV1800CE', 'ADANIPORTS21NOV760CE', 'AMARAJABAT21NOV680CE', 'AMBUJACEM21NOV420CE', 'APLLTD21NOV800CE', 'APOLLOHOSP21NOV5200CE', 'APOLLOTYRE21NOV235CE', 'ASHOKLEY21NOV150CE', 'ASIANPAINT21NOV3200CE', 'AUBANK21NOV1240CE', 'AXISBANK21NOV750CE', 'BAJAJFINSV21NOV18500CE', 'BEL21NOV230CE', 'BERGEPAINT21NOV800CE', 'BHARATFORG21NOV800CE', 'BHEL21NOV80CE', 'BIOCON21NOV370CE', 'BRITANNIA21NOV3800CE', 'CADILAHC21NOV490CE', 'CHOLAFIN21NOV650CE', 'COALINDIA21NOV170CE', 'CONCOR21NOV700CE', 'CUMMINSIND21NOV940CE', 'BANKBARODA21NOV110CE', 'CANBK21NOV230CE', 'COFORGE21NOV5800CE', 'COLPAL21NOV1600CE', 'DEEPAKNTR21NOV2400CE', 'DIVISLAB21NOV5000CE', 'DLF21NOV430CE', 'FEDERALBNK21NOV105CE', 'DRREDDY21NOV5000CE', 'EICHERMOT21NOV2800CE', 'GAIL21NOV150CE', 'GLENMARK21NOV540CE', 'GODREJCP21NOV940CE', 'GODREJPROP21NOV2400CE', 'GRANULES21NOV320CE', 'GRASIM21NOV1900CE', 'HCLTECH21NOV1200CE', 'HDFC21NOV3000CE', 'HDFCAMC21NOV2700CE', 'HDFCBANK21NOV1600CE', 'HEROMOTOCO21NOV2800CE', 'HINDALCO21NOV460CE', 'HINDPETRO21NOV350CE', 'HINDUNILVR21NOV2440CE', 'ICICIBANK21NOV780CE', 'ICICIPRULI21NOV670CE', 'INDIGO21NOV2400CE', 'INDUSTOWER21NOV300CE', 'IOC21NOV140CE', 'ITC21NOV250CE', 'JINDALSTEL21NOV400CE', 'JSWSTEEL21NOV670CE', 'JUBLFOOD21NOV4100CE', 'KOTAKBANK21NOV2100CE', 'L&TFH21NOV85CE', 'LT21NOV1980CE', 'LTTS21NOV5400CE', 'M&M21NOV950CE', 'M&MFIN21NOV190CE', 'MANAPPURAM21NOV200CE', 'MARUTI21NOV8000CE', 'MCDOWELL-N21NOV940CE', 'MFSL21NOV980CE', 'MGL21NOV1020CE', 'MOTHERSUMI21NOV250CE', 'MPHASIS21NOV3500CE', 'MRF21NOV80000CE', 'NAM-INDIA21NOV430CE', 'NAUKRI21NOV6500CE', 'NAVINFLUOR21NOV3600CE', 'NESTLEIND21NOV19500CE', 'NTPC21NOV140CE', 'ONGC21NOV160CE', 'PAGEIND21NOV41000CE', 'PETRONET21NOV240CE', 'PFIZER21NOV5200CE', 'PIDILITIND21NOV2500CE', 'PIIND21NOV3200CE', 'PVR21NOV1800CE', 'RBLBANK21NOV210CE', 'RELIANCE21NOV2600CE', 'MINDTREE21NOV5000CE', 'SBIN21NOV520CE', 'SHREECEM21NOV30000CE', 'SRTRANSFIN21NOV1700CE', 'SUNPHARMA21NOV820CE', 'SUNTV21NOV600CE', 'TATACHEM21NOV950CE', 'TATAMOTORS21NOV520CE', 'TATAPOWER21NOV250CE', 'TCS21NOV3600CE', 'TECHM21NOV1600CE', 'UBL21NOV1800CE', 'ULTRACEMCO21NOV8100CE', 'UPL21NOV800CE', 'WIPRO21NOV660CE', 'ACC21NOV2600CE', 'ALKEM21NOV3600CE', 'BAJFINANCE21NOV7600CE', 'BALKRISIND21NOV2500CE', 'BANDHANBNK21NOV320CE', 'BATAINDIA21NOV2260CE', 'BHARTIARTL21NOV740CE', 'HDFCLIFE21NOV720CE', 'CUB21NOV170CE', 'EXIDEIND21NOV180CE', 'ICICIGI21NOV1540CE', 'IDFCFIRSTB21NOV55CE', 'IGL21NOV500CE', 'INDUSINDBK21NOV1100CE', 'IRCTC21NOV1000CE', 'LUPIN21NOV950CE', 'GUJGASLTD21NOV680CE', 'MARICO21NOV550CE', 'LICHSGFIN21NOV430CE', 'MUTHOOTFIN21NOV1700CE', 'NMDC21NOV150CE', 'RAMCOCEM21NOV1100CE', 'SBILIFE21NOV1200CE', 'SRF21NOV2200CE', 'TATACONSUM21NOV850CE', 'TATASTEEL21NOV1300CE', 'SIEMENS21NOV2400CE', 'TITAN21NOV2600CE', 'TRENT21NOV1200CE', 'TORNTPHARM21NOV2800CE', 'TVSMOTOR21NOV750CE', 'BOSCHLTD21NOV19000CE', 'CIPLA21NOV940CE', 'HAVELLS21NOV1400CE', 'INFY21NOV1800CE', 'LALPATHLAB21NOV3700CE', 'LTI21NOV7300CE', 'PEL21NOV2700CE', 'POWERGRID21NOV190CE', 'RECLTD21NOV145CE', 'BAJAJ-AUTO21NOV3650CE', 'TORNTPOWER21NOV550CE', 'VEDL21NOV340CE', 'GMRINFRA21NOV45CE', 'PFC21NOV140CE', 'VOLTAS21NOV1300CE', 'BPCL21NOV430CE', 'DABUR21NOV610CE', 'IDEA21NOV11CE', 'ABFRL21NOV300CE', 'COROMANDEL21NOV800CE', 'INDHOTEL21NOV220CE', 'METROPOLIS21NOV3300CE']


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
    stock_bull=symbol
    stock_bull = stock_bull.replace('NFO:','')
    quantity=get_quantity(stock_bull)
    print(quantity)
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+10, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    placeGTT(stock_bull,quantity,c/2, c+30, c)

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

def buy_stock_max_bull(fnolist):
    sbull = []
    stock_per_change = {}
    for symbol in fnolist:
        try:
            o,h,l,c = kite_get_ohlc(symbol)
        except:
            pass
        if o != 0:
            try:
                per_change = ((c-o)/(h-l))*100
                stock_per_change[symbol]=per_change
            except:
                pass

    stock_bull = max(stock_per_change, key=stock_per_change.get)
    o,h,l,c = kite_get_ohlc(stock_bull)
    print(stock_bull)
    stock_bull = stock_bull.replace('NFO:','')
    quantity=get_quantity(stock_bull)
    print(quantity)
    '''
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+10, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    placeGTT(stock_bull,quantity,c/2, c+30, c)
    '''
    #print(stock_bear)
    res = nlargest(10, stock_per_change, key = stock_per_change.get)
    res.reverse()
    print(res)
    check_and_buy(res)


def get_ohlc_dict(fnolist):
    for i in fnolist:
        tmp_symbol="NSE:"+i
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
buy_stock_max_bull(fnolistnse)
#print(len(fnolist))

