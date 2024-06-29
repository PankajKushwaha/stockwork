import pyautogui
import time
from pynput import keyboard
from nsetools import Nse
import math
import code, traceback, signal
import Xlib.threaded
import sys
import traceback
import os

max_fund_per_stock = 15000
slm_percent = 0.2
sl=0
order_type='n'
counter=0

nse = Nse()

def debug(sig, frame):
    """Interrupt running process, and provide a python prompt for
    interactive debugging."""
    d={'_frame':frame}         # Allow access to frame object.
    d.update(frame.f_globals)  # Unless shadowed by global
    d.update(frame.f_locals)

    i = code.InteractiveConsole(d)
    message  = "Signal received : entering python shell.\nTraceback:\n"
    message += ''.join(traceback.format_stack(frame))
    i.interact(message)

def listen():
    signal.signal(signal.SIGUSR1, debug)  # Register handler

def get_sl(order_type):
    global sl
    f=stock_price
    print(f)
    print(order_type)
    if order_type == 'b':
        sl=f-round(f*0.002,2)
        print ("pankaj")
        print (sl)
    if order_type == 's':
        sl=f+round(f*0.002,2)
    print(sl)
    sl_int = math.trunc(sl)
    print(sl_int)
    zerodha_sl = sl_int + ((int((int((sl-math.trunc(sl))*100)/5)) * 5)/100 )
    print(zerodha_sl)
    order_type='n'
    return zerodha_sl




def getCurrentPrice(symbol):
    global stock_price
    stock_price = nse.get_quote(symbol)['lastPrice']
    return int(stock_price)

def Buy_Stock(current_stock):
    pyautogui.press('backspace')
    pyautogui.click(529,120)
    current_price = getCurrentPrice(stock)

    num_of_share = int(max_fund_per_stock / current_price)
    print(num_of_share)

    if num_of_share == 0:
        exit()

    pyautogui.click(91,122) #thunder
    pyautogui.click(118,201)  #Buy
    time.sleep(2)
    pyautogui.click(638,673)  #Market
    pyautogui.moveTo(466,628) #Buy price window
    pyautogui.click(clicks=2)
    pyautogui.press('backspace')
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.typewrite(str(num_of_share))
    pyautogui.click(834,733) #brought
    return False

     
def Sell_Stock(stock_price):
    pyautogui.press('backspace')
    pyautogui.click(529,120)
    current_price = getCurrentPrice(stock)
    num_of_share = int(max_fund_per_stock / current_price)
    print(num_of_share)
    
    if num_of_share == 0:
        exit()

    pyautogui.click(91,122) #thunder
    pyautogui.click(216,204)  #sell
    time.sleep(2)
    pyautogui.click(638,673)  #Market
    pyautogui.moveTo(466,628) #sell price window
    pyautogui.click(clicks=2)
    pyautogui.press('backspace')
    pyautogui.click(clicks=1)
    time.sleep(1)
    pyautogui.typewrite(str(num_of_share))
    pyautogui.click(834,733) #sold
    return False
         
def put_slm(stoploss_market):
    if counter == 1:
        pyautogui.moveTo(262,434)
        time.sleep(1)
        pyautogui.click(clicks=1)
        time.sleep(1)
        pyautogui.click(162,467)
        time.sleep(1)
    
    if counter == 2:
        pyautogui.moveTo(256,476)
        time.sleep(1)
        pyautogui.click(clicks=1)
        time.sleep(1)
        pyautogui.click(135,501)

    if counter == 3:
        pyautogui.moveTo(256,516)
        time.sleep(1)
        pyautogui.click(clicks=1)
        time.sleep(1)
        pyautogui.click(133,546)

    if counter == 4:
        pyautogui.moveTo(262,555)
        time.sleep(1)
        pyautogui.click(clicks=1)
        time.sleep(1)
        pyautogui.click(134,587)
        
    time.sleep(2)
    pyautogui.click(927,673) #slm
    time.sleep(1)
    pyautogui.moveTo(820,628)
    pyautogui.click(clicks=2,interval=0.25)
    pyautogui.typewrite(str(stoploss_market))
    pyautogui.click(834,733) #sell/buy
    pyautogui.click(589,120) #Thunder cancle
    
def get_stoploss():
    None

def on_press(key):
    global counter 
    global order_type
    try:
        if key.char == 'b':
            Buy_Stock(stock)
            counter=counter+1
            sl = get_sl('b')
            put_slm(sl)
            return False

        if key.char == 's':
            Sell_Stock(stock)
            counter=counter+1
            sl = get_sl('s')
            put_slm(sl)
            return False

        if key.char == 'c':
            return False

        if key.char == 'e':
            print("exiting...")
            os._exit(1)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def start_listener_thread():
    with keyboard.Listener( on_press=on_press, on_release=None) as listener:
        listener.join()

NIFTY5 = ["TECHM","IOC"]

MY_10 = ["DLF" , "INDIGO" , "OFSS" , "HCLTECH" , "AMBUJACEM" ,"TITAN" ,"UPL", "GRASIM", "ICICIBANK" , "AARTIIND" ]

NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ_AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CAIRN","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M_M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]

NIFTY40 = ["ACC","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ_AUTO","BAJAJFINSV","BAJFINANCE","BPCL","BRITANNIA","CAIRN","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","IOC","JSWSTEEL","KOTAKBANK","LT","NESTLEIND","NTPC","ONGC","POWERGRID","SBILIFE","SBIN","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","UPL","WIPRO"]


NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M_M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL_N","WIPRO"]

NIFTY200 = ["AARTIIND","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIGAS","ADANIGREEN","ADANIPORTS","ADANITRANS","AJANTPHARM","ALKEM","AMARAJABAT","AMBUJACEM","APLLTD","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUBANK","AUROPHARMA","AXISBANK","BAJAJ_AUTO","BAJAJFINSV","BAJAJHLDNG","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BBTC","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CASTROLIND","CESC","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DHANI","DIVISLAB","DLF","DMART","DRREDDY","EDELWEISS","EICHERMOT","EMAMILTD","ENDURANCE","ESCORTS","EXIDEIND","FEDERALBNK","FORTIS","FRETAIL","GAIL","GICRE","GLENMARK","GMRINFRA","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRASIM","GSPL","GUJGASLTD","HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HUDCO","IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDHOTEL","INDIGO","INDUSINDBK","INFRATEL","INFY","IOC","IPCALAB","IRCTC","ISEC","ITC","JINDALSTEL","JSWENERGY","JSWSTEEL","JUBLFOOD","KOTAKBANK","L&TFH","LALPATHLAB","LICHSGFIN","LT","LTI","LTTS","LUPIN","M_M","M_MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL_N","MFSL","MGL","MINDTREE","MOTHERSUMI","MPHASIS","MRF","MUTHOOTFIN","NAM_INDIA","NATCOPHARM","NATIONALUM","NAUKRI","NAVINFLUOR","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","OIL","ONGC","PAGEIND","PEL","PETRONET","PFC","PFIZER","PGHH","PIDILITIND","PIIND","PNB","POLYCAB","POWERGRID","PRESTIGE","RAJESHEXPO","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SANOFI","SBICARD","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UNIONBANK","UPL","VBL","VGUARD","VOLTAS","WHIRLPOOL","WIPRO","YESBANK","ZEEL"]

global stock

print ( "please enter number of open postion:")
open_position = input()

if (open_position == ''):
    counter = 0
    print("0")
else:
    counter = int(open_position)

    if (counter < 0 or counter > 4):
        exit()

listen() #to debug

for stock in NIFTY200:
    pyautogui.click(166,122)
    pyautogui.typewrite(stock)
    #time.sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(167,206)
    #pyautogui.typewrite(["enter"])
    #time.sleep(5)
    with keyboard.Events() as events:
        event = events.get(300.0)
        if event is None:
            continue
        else:
            if str(event) == "Press(key='e')":
                os._exit(1)
            if str(event) == "Press(key='c')":
                pyautogui.click(166,122)
                pyautogui.press('backspace')
                continue 
            if str(event) == "Press(key='s')":
                pyautogui.click(166,122)
                pyautogui.press('backspace')
                pyautogui.click(800,750)
                start_listener_thread()
                    
