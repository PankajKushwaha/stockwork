from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
import click
import pickle
import time
from heapq import nlargest

fnolistnse = []
kite = set_token()
def load_list_from_file(filename):
    with open(filename, 'rb') as handle:
        lst = pickle.load(handle)
        return lst

def load_from_file(filename):
    with open(filename, 'rb') as handle:
        obj = pickle.load(handle)
        return obj

def get_ohlc_dict(fnolist):
    for i in fnolist:
        tmp_symbol="NFO:"+i
        fnolistnse.append(tmp_symbol)
    #print(fnolistnse)
    ohlc_dict=kite.ohlc(fnolistnse)
    #print(ohlc_dict)
    return ohlc_dict


kite_ohlc_dict =  {}
yesterday_ohlc_dict= {}
fnolist = load_list_from_file("bull_option_list.pkl") + load_list_from_file("bear_option_list.pkl") 
kite_ohlc_dict = get_ohlc_dict(fnolist)
yesterday_ohlc_dict=load_from_file("yesterday_ohlc_dict.pkl")

#print(fnolist)

lot_size = {'BANKNIFTY': 25, 'NIFTY': 50, 'FINNIFTY': 40, 'ASTRAL': 275, 'AARTIIND': 850, 'ABBOTINDIA': 25, 'ACC': 250, 'ADANIENT': 500, 'ALKEM': 200, 'AMARAJABAT': 1000, 'AMBUJACEM': 1500, 'APLLTD': 550, 'APOLLOHOSP': 125, 'ASHOKLEY': 4500, 'AUBANK': 500, 'ATUL': 75, 'AUROPHARMA': 650, 'ADANIPORTS': 1250, 'BAJAJFINSV': 75, 'BAJFINANCE': 125, 'BALKRISIND': 200, 'BANDHANBNK': 1800, 'BATAINDIA': 550, 'BEL': 3800, 'BHARTIARTL': 1886, 'BHEL': 10500, 'BIOCON': 2300, 'AXISBANK': 1200, 'BPCL': 1800, 'CADILAHC': 1100, 'CANFINHOME': 975, 'CHOLAFIN': 1250, 'CIPLA': 650, 'COFORGE': 100, 'CUB': 3100, 'ASIANPAINT': 150, 'DABUR': 1250, 'DEEPAKNTR': 250, 'DIVISLAB': 100, 'DRREDDY': 125, 'GLENMARK': 1150, 'GODREJCP': 500, 'GODREJPROP': 325, 'GRANULES': 1550, 'GRASIM': 475, 'BSOFT': 1300, 'CANBK': 5400, 'HAL': 475, 'HAVELLS': 500, 'HCLTECH': 700, 'HDFCAMC': 200, 'HDFCBANK': 550, 'HINDALCO': 1075, 'CHAMBLFERT': 1500, 'HINDUNILVR': 300, 'BHARATFORG': 750, 'ICICIGI': 425, 'ICICIPRULI': 750, 'IDFCFIRSTB': 9500, 'BOSCHLTD': 50, 'IEX': 1250, 'INDHOTEL': 4022, 'EICHERMOT': 350, 'BRITANNIA': 200, 'FSL': 2600, 'INDIGO': 250, 'INFY': 300, 'IPCALAB': 225, 'GSPL': 1700, 'IRCTC': 1625, 'JSWSTEEL': 1350, 'JUBLFOOD': 125, 'KOTAKBANK': 400, 'COALINDIA': 4200, 'L&TFH': 8924, 'LALPATHLAB': 125, 'LT': 575, 'LTI': 150, 'LTTS': 200, 'CROMPTON': 1100, 'MANAPPURAM': 3000, 'MARICO': 1000, 'CUMMINSIND': 600, 'MCDOWELL-N': 1250, 'METROPOLIS': 200, 'MGL': 600, 'DELTACORP': 2300, 'MINDTREE': 200, 'MPHASIS': 325, 'MRF': 10, 'MUTHOOTFIN': 375, 'NATIONALUM': 8500, 'ITC': 3200, 'DIXON': 125, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'NESTLEIND': 25, 'OFSS': 125, 'ONGC': 7700, 'PAGEIND': 30, 'PFC': 6200, 'PIIND': 250, 'LAURUSLABS': 900, 'POLYCAB': 300, 'POWERGRID': 5333, 'GAIL': 6100, 'PVR': 407, 'RAMCOCEM': 850, 'RECLTD': 6000, 'RELIANCE': 250, 'SAIL': 4750, 'GMRINFRA': 22500, 'SBILIFE': 750, 'SHREECEM': 25, 'GUJGASLTD': 1250, 'SRF': 625, 'SRTRANSFIN': 400, 'STAR': 675, 'SUNPHARMA': 700, 'TATAMOTORS': 2850, 'TATAPOWER': 6750, 'TCS': 150, 'HDFC': 300, 'TORNTPHARM': 250, 'TORNTPOWER': 1500, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 3100, 'VOLTAS': 500, 'HDFCLIFE': 1100, 'IBULHSGFIN': 3100, 'ICICIBANK': 1375, 'ABFRL': 2600, 'JKCEMENT': 175, 'RBLBANK': 2900, 'LUPIN': 850, 'M&MFIN': 4000, 'SBICARD': 500, 'MARUTI': 100, 'NAM-INDIA': 1600, 'TVSMOTOR': 1400, 'WHIRLPOOL': 250, 'OBEROIRLTY': 700, 'PEL': 275, 'PERSISTENT': 150, 'PFIZER': 125, 'BANKBARODA': 11700, 'BERGEPAINT': 1100, 'TATACONSUM': 675, 'TRENT': 725, 'COLPAL': 350, 'CONCOR': 1563, 'COROMANDEL': 625, 'DLF': 1650, 'ESCORTS': 550, 'EXIDEIND': 3600, 'FEDERALBNK': 10000, 'HEROMOTOCO': 300, 'HINDPETRO': 2700, 'APOLLOTYRE': 2500, 'IGL': 1375, 'INDIAMART': 75, 'IOC': 6500, 'JINDALSTEL': 2500, 'LICHSGFIN': 2000, 'DALBHARAT': 250, 'M&M': 700, 'MCX': 350, 'MFSL': 650, 'MOTHERSUMI': 3500, 'SUNTV': 1500, 'NMDC': 6700, 'NTPC': 5700, 'PETRONET': 3000, 'PIDILITIND': 250, 'PNB': 16000, 'SBIN': 1500, 'SIEMENS': 275, 'INDIACEM': 2900, 'SYNGENE': 850, 'TATASTEEL': 425, 'TECHM': 600, 'TITAN': 375, 'UBL': 350, 'ZEEL': 3000, 'TATACHEM': 1000, 'BAJAJ-AUTO': 250, 'INDUSTOWER': 2800, 'IDEA': 70000, 'WIPRO': 800, 'INDUSINDBK': 900}




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
    #print(kite_ohlc_dict)
    o=kite_ohlc_dict[symbol]["ohlc"]["open"]
    h=kite_ohlc_dict[symbol]["ohlc"]["high"]
    l=kite_ohlc_dict[symbol]["ohlc"]["low"]
    c=kite_ohlc_dict[symbol]["last_price"]

    return o,h,l,c

def kite_get_yesterday_ohlc(symbol):
    #symbol="NSE:"+symbol
    o=yesterday_ohlc_dict[symbol]["ohlc"]["open"]
    h=yesterday_ohlc_dict[symbol]["ohlc"]["high"]
    l=yesterday_ohlc_dict[symbol]["ohlc"]["low"]
    c=yesterday_ohlc_dict[symbol]["last_price"]

    return o,h,l,c

def print_all_ohlc(fnolist):
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        print(symbol)
        print(o)
        print(h)
        print(l)
        print(c)

def buy_option(symbol):
    stock_bull=symbol
    stock_bull = stock_bull.replace('NFO:','')
    o,h,l,c = kite_get_ohlc(symbol)
    quantity=get_quantity(stock_bull)
    print(symbol)
    print(quantity)
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+4, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    '''
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='SL', price=h+(h/25), validity='DAY',
            disclosed_quantity=None, trigger_price=h+(h/100), squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    print("put following gtt")
    print(symbol)
    print("SL")
    base_price = h + (h/100)
    print(base_price - (base_price/10))
    print("TARGET")
    print(base_price - ((base_price/10)*3))
    '''
    placeGTT(stock_bull,quantity,c-(c/20), c+(c/10), c)

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
        '''
        char = click.prompt('Please enter a char, b to buy , c to continue', type=str)
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
        '''

def list_of_open_postion():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        open_position_list.append(dic['tradingsymbol'])
    return open_position_list

def is_already_brought(symbol):
    open_pos = list_of_open_postion()
    if symbol in open_pos:
        return True
    else:
        return False

def buy_stock_max_bull(fnolist):
    sbull = []
    stock_per_change = {}
    check_and_buy_list = []
    check_and_buy_dic = {}
    option_dic = {}
    kite_ohlc_dict = get_ohlc_dict(fnolist)
    for symbol in fnolist:
        try:
            print(symbol)
            o,h,l,c = kite_get_ohlc(symbol)
            if c<10:
                continue
            oy,hy,ly,cy = kite_get_yesterday_ohlc(symbol)
        except:
            pass
        #if o != 0 and (h-l)!=0 and c>((o*4)+2) and c > 10 and is_already_brought(symbol) == False and c>hy:
        #if o != 0 and (h-l)!=0 and c>o+(o/2) and c > 10 and is_already_brought(symbol) == False and c>hy and o>ly:
        #if o != 0 and (h-l)!=0 and c>2*o and c > 10 and is_already_brought(symbol) == False and c>hy and o>ly:
        if o != 0 and (h-l)!=0 and c>(h-(h/20)) and is_already_brought(symbol) == False and c>o :
            try:
                print("####BUY FOLLOWING####")
                print(symbol)
                flag=True
                for order in kite.orders():
                    if order["tradingsymbol"] == symbol:
                        flag=False
                        break
                if flag==True:
                    check_and_buy_list.append(symbol)
                    check_and_buy_dic[symbol]= ((c-o)/o)*100
                #buy_option(symbol,c)
                continue
            except:
                pass
    while True: 
        for idx,symbol in enumerate(check_and_buy_list):
            print(idx,symbol)
            option_dic[idx] = symbol
            o,h,l,c = kite_get_ohlc(symbol)
        char = click.prompt('Please enter a char, c for break and continue', type=str)
        if char == "c":
            break
        else:
           # check_and_buy(check_and_buy_list)
           check_and_buy([option_dic[int(char)]])
    '''
    stock_bull = max(stock_per_change, key=stock_per_change.get)
    o,h,l,c = kite_get_ohlc(stock_bull)
    print(stock_bull)
    stock_bull = stock_bull.replace('NFO:','')
    quantity=get_quantity(stock_bull)
    print(quantity)
    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+10, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    placeGTT(stock_bull,quantity,c/2, c+30, c)
    #print(stock_bear)
    res = nlargest(10, stock_per_change, key = stock_per_change.get)
    res.reverse()
    print(res)
    check_and_buy(res)
    '''


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

def get_strong_bull_dic(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        #print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/(h-l))*100
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change


def strong_bull():
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(20, per_change, key = per_change.get)
    res.reverse()
    print(res)
    return res[-1]

def top_gainer():
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(20, per_change, key = per_change.get)
    res.reverse()
    print(res)
    return res[-1]

def stratagy():
    kite_ohlc_dict=get_ohlc_dict(fnolist)
    #print(kite_ohlc_dict)
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        oy,hy,ly,cy = kite_get_yesterday_ohlc(symbol)


def main_function():
        symbol = top_gainer()
        #symbol = strong_bull()
        if is_already_brought(symbol) == False:
            print("pankaj")
            #buy_option(symbol)

main_function()


