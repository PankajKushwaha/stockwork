import os
import sys
import time
from set_token import *
from datetime import datetime
from itertools import cycle


filename="orderlist.txt"
last_high={}
last_low={}
call_dic={}
put_dic={}
candle_flag=0
candle_store={}
ltp_dic={}
old_keys=[]
old_size=0
old_minute=-1
symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}
lot_size={'ABB': 250, 'HONAUT': 15, 'DALBHARAT': 500, 'GODREJCP': 1000, 'BAJFINANCE': 125, 'BAJAJFINSV': 500, 'BRITANNIA': 200, 'AUBANK': 1000, 'TRENT': 725, 'GUJGASLTD': 1250, 'INTELLECT': 750, 'HINDUNILVR': 300, 'ESCORTS': 550, 'DIXON': 125, 'BATAINDIA': 275, 'ICICIGI': 425, 'CONCOR': 1000, 'APOLLOTYRE': 3500, 'WHIRLPOOL': 350, 'EICHERMOT': 350, 'RAMCOCEM': 850, 'HINDPETRO': 2700, 'M&MFIN': 4000, 'SIEMENS': 275, 'HEROMOTOCO': 300, 'SBICARD': 800, 'ASIANPAINT': 200, 'IEX': 3750, 'GODREJPROP': 325, 'ZEEL': 3000, 'HAVELLS': 500, 'CUMMINSIND': 600, 'TITAN': 375, 'MARUTI': 100, 'UBL': 400, 'COROMANDEL': 700, 'ABBOTINDIA': 40, 'BERGEPAINT': 1100, 'PERSISTENT': 150, 'JKCEMENT': 250, 'ABCAPITAL': 5400, 'LTTS': 200, 'DELTACORP': 2300, 'AARTIIND': 850, 'MRF': 10, 'KOTAKBANK': 400, 'BOSCHLTD': 50, 'INDIACEM': 2900, 'TATACONSUM': 900, 'LICHSGFIN': 2000, 'COLPAL': 350, 'SHREECEM': 25, 'BPCL': 1800, 'PAGEIND': 15, 'SUNTV': 1500, 'RBLBANK': 5000, 'FSL': 5200, 'BAJAJ-AUTO': 250, 'PIIND': 250, 'GLENMARK': 1150, 'BIOCON': 2300, 'NAUKRI': 125, 'M&M': 700, 'ADANIPORTS': 1250, 'MGL': 800, 'HDFCAMC': 300, 'DLF': 1650, 'VOLTAS': 500, 'OBEROIRLTY': 700, 'IBULHSGFIN': 4000, 'L&TFH': 8924, 'MCDOWELL-N': 625, 'NESTLEIND': 40, 'INDUSTOWER': 2800, 'PIDILITIND': 250, 'DABUR': 1250, 'MPHASIS': 175, 'GMRINFRA': 22500, 'IPCALAB': 650, 'MFSL': 650, 'CANBK': 2700, 'OFSS': 200, 'APOLLOHOSP': 125, 'PETRONET': 3000, 'COFORGE': 150, 'POLYCAB': 300, 'ICICIPRULI': 1500, 'GRASIM': 475, 'SBIN': 1500, 'BHEL': 10500, 'MINDTREE': 200, 'LTI': 150, 'TVSMOTOR': 1400, 'CROMPTON': 1500, 'AUROPHARMA': 1000, 'INDUSINDBK': 900, 'BANDHANBNK': 1800, 'MARICO': 1200, 'ULTRACEMCO': 100, 'IDFCFIRSTB': 15000, 'MOTHERSON': 4500, 'INDIGO': 300, 'AMARAJABAT': 1000, 'TORNTPOWER': 1500, 'ALKEM': 200, 'TCS': 150, 'INDIAMART': 150, 'LAURUSLABS': 900, 'ACC': 250, 'ASHOKLEY': 5000, 'METROPOLIS': 300, 'IRCTC': 875, 'HDFCBANK': 550, 'DEEPAKNTR': 250, 'DIVISLAB': 150, 'TATACOMM': 500, 'HINDCOPPER': 4300, 'AXISBANK': 1200, 'NATIONALUM': 4250, 'JUBLFOOD': 1250, 'BHARTIARTL': 950, 'IGL': 1375, 'TATAMOTORS': 1425, 'IDFC': 10000, 'ABFRL': 2600, 'ZYDUSLIFE': 1800, 'ICICIBANK': 1375, 'TATACHEM': 1000, 'INFY': 300, 'BANKBARODA': 5850, 'RECLTD': 8000, 'UPL': 1300, 'ADANIENT': 500, 'HDFC': 300, 'BEL': 11400, 'TECHM': 600, 'JINDALSTEL': 1250, 'GNFC': 1300, 'BALKRISIND': 300, 'PEL': 275, 'CIPLA': 650, 'NAVINFLUOR': 225, 'FEDERALBNK': 10000, 'ITC': 3200, 'PNB': 16000, 'CANFINHOME': 975, 'MANAPPURAM': 6000, 'WIPRO': 1000, 'EXIDEIND': 3600, 'TATAPOWER': 3375, 'CHAMBLFERT': 1500, 'HCLTECH': 700, 'JSWSTEEL': 1350, 'SBILIFE': 750, 'ASTRAL': 275, 'AMBUJACEM': 1800, 'INDHOTEL': 4022, 'SUNPHARMA': 700, 'SRF': 375, 'TORNTPHARM': 500, 'GSPL': 2500, 'LALPATHLAB': 250, 'CUB': 5000, 'SRTRANSFIN': 600, 'CHOLAFIN': 1250, 'GAIL': 9150, 'SAIL': 6000, 'LUPIN': 850, 'RAIN': 3500, 'DRREDDY': 125, 'PFC': 6200, 'TATASTEEL': 4250, 'MUTHOOTFIN': 375, 'PVR': 407, 'BHARATFORG': 1000, 'LT': 300, 'SYNGENE': 1000, 'COALINDIA': 4200, 'GRANULES': 2000, 'HAL': 475, 'ATUL': 75, 'RELIANCE': 250, 'NTPC': 5700, 'HDFCLIFE': 1100, 'HINDALCO': 1075, 'VEDL': 1550, 'BSOFT': 1300, 'IOC': 9750, 'POWERGRID': 2700, 'NMDC': 3350, 'BALRAMCHIN': 1600, 'ONGC': 3850}

def get_quantity(stock):
    stock_name = stock.split('22')[0]
    for symbol in lot_size:
        if (stock_name == symbol):
            return lot_size[symbol]

def update_last_high(lst):
    #print(lst)
    print(" === UPDATING LAST HIGH ===")
    global candle_store
    for symbol in lst:
        date=datetime.today().strftime('%Y-%m-%d')
        #candle = kite.historical_data(symbol_to_token[symbol], "date"+" 09:15:00", date+" 15:35:00", "5minute", continuous=False, oi=False)
        candle = kite.historical_data(symbol_to_token[symbol],  "2022-09-26 00:00:00", date+" 15:35:00", "5minute", continuous=False, oi=False)
        h=candle[-2]["high"]
        l=candle[-2]["low"]
        last_high[symbol]=h
        last_low[symbol]=l
        print(symbol)
        print(l)
        print(h)
        print("   ")
        candle_store[symbol]=candle
    #print(last_high)

def update_last_low(lst):
    global candle_store
    print(" === UPDATING LAST  LOW===")
    global candle_store
    for symbol in lst:
        date=datetime.today().strftime('%Y-%m-%d')
        #candle = kite.historical_data(symbol_to_token[symbol], "date"+" 09:15:00", date+" 15:35:00", "5minute", continuous=False, oi=False)
        candle = kite.historical_data(symbol_to_token[symbol],  "2022-09-26 00:00:00", date+" 15:35:00", "5minute", continuous=False, oi=False)
        l=candle[-2]["low"]
        h=candle[-2]["high"]
        last_low[symbol]=l
        last_high[symbol]=h
        print(symbol)
        print(l)
        print(h)
        print("   ")
        candle_store[symbol]=candle
    #print(last_low)

def remove_str_from_file(filename,stringname):
    with open(filename) as oldfile,open("newfile.txt","a") as newfile:
        for line in oldfile:
            tmpstr=stringname.replace("NSE:","")
            tmpstr=tmpstr.lower()
            if tmpstr not in line:
                newfile.write(line)
    command = "mv newfile.txt "+filename
    os.system(command)

def get_call_put_dic(filename):
    global old_keys
    with open(filename) as oldfile:
        for line in oldfile:
            if ",ce" in line:
                s=line.split(",")
                key="NSE:"+s[0].upper()
                value=s[1]
                if key not in call_dic:
                    call_dic[key]=value
            if ",pe" in line:
                s=line.split(",")
                key="NSE:"+s[0].upper()
                value=s[1]
                if key not in put_dic:
                    put_dic[key]=value
    #print(call_dic)
    #print(put_dic)
    return call_dic,put_dic

def is_time_to_update():
    time_now = datetime.now()
    global old_minute
    m=time_now.minute
    m=int(m/5)*5
    if old_minute==-1:
        old_minute=m
        return True
    if old_minute != m and m%5==0:
        old_minute=m
        time.sleep(3)
        return True

    return False

def get_watch_list():
    return list(call_dic.keys()),list(put_dic.keys())

def update_high_low_dic():
    if is_time_to_update() or candle_flag == 1:
        call_wl,put_wl=get_watch_list()
        update_last_high(call_wl)
        update_last_low(put_wl)

def get_expiry_month():
    return "22OCT"

def update_ltp_dic():
    global ltp_dic
    call_wl,put_wl=get_watch_list()
    wl=call_wl+put_wl
    #print(wl)
    ltp=kite.ltp(wl)
    for symbol in ltp:
        ltp_dic[symbol]=ltp[symbol]["last_price"]
    #print(ltp_dic)

def getfnosymbol(symbol):
    if symbol in list(call_dic.keys()):
        return symbol.replace("NSE:","")+get_expiry_month()+call_dic[symbol]+"CE"
    if symbol in list(put_dic.keys()):
        return symbol.replace("NSE:","")+get_expiry_month()+put_dic[symbol]+"PE"

def set_sl(fnosymbol):
    tmpstr=""
    symbol="NSE:"+fnosymbol.split("22OCT")[0]
    call_wl,put_wl=get_watch_list()
    print("=== SETTING STOP LOSS ===")
    if symbol in call_wl: 
        sl=last_low[symbol]
        tmpstr=symbol+","+str(sl)+","+fnosymbol
        print(symbol)
        print(sl)
    if symbol in put_wl: 
        sl=last_high[symbol]
        tmpstr=symbol+","+str(sl)+","+fnosymbol
        print(symbol)
        print(sl)
    print(tmpstr)
    with open('stoploss.txt', 'a') as slfile:
        slfile.write(tmpstr)
        slfile.write("\n")

def ltp_fno_symbol(symbol):
    ltp_dict=kite.ltp(["NFO:"+symbol])
    c=ltp_dict["NFO:"+symbol]["last_price"]
    return c

def check_call_correction(lst):
    lst.reverse()
    #print(lst)
    lst.pop(0)
    count=0
    for e,i in enumerate(lst):
        nxt=lst[(e + 1) % len(lst)]
        #print(i)
        #print(nxt)
        if i<nxt and count < 3:
            count=count+1
        elif i==next:
            continue
        elif i>nxt and count<3:
            return False
        elif count==3:
            return True

def check_put_correction(lst):
    lst.reverse()
    lst.pop(0)
    count=0
    for e,i in enumerate(lst):
        nxt=lst[(e + 1) % len(lst)]
        if i>nxt and count < 3:
            count=count+1
        elif i==next:
            continue
        elif i<nxt and count<3:
            return False
        elif count==3:
            return True

def update_sl_in_ltp_dic():
    sl_symbol_list=[]
    if os.path.isfile("stoploss.txt"):
        with open("stoploss.txt") as slfile:
            for line in slfile:
                #print(line)
                tmpline=line.split(",")
                sl_symbol_list.append(tmpline[0])
    #print(sl_symbol_list)
    ltp=kite.ltp(sl_symbol_list)
    for symbol in ltp:
        ltp_dic[symbol]=ltp[symbol]["last_price"]


def check_sl():
    symbol_to_remove=[]
    if os.path.isfile("stoploss.txt"):
        update_sl_in_ltp_dic()
        with open("stoploss.txt") as slfile:
            for line in slfile:
                if line[-3:].strip() == "CE":
                    tmpline=line.split(",")
                    #print(ltp_dic[tmpline[0]])
                    #print(tmpline[1])
                    if ltp_dic[tmpline[0]] < float(tmpline[1]):
                        sell_fno_symbol(tmpline[2].strip(),1)
                        symbol_to_remove.append(tmpline[2])
                elif line[-3:].strip() == "PE":
                    tmpline=line.split(",")
                    if ltp_dic[tmpline[0]] > float(tmpline[1]):
                        tmpline=line.split(",")
                        #print(ltp_dic[tmpline[0]])
                        #print(tmpline[1])
                        sell_fno_symbol(tmpline[2].strip(),1)
                        symbol_to_remove.append(tmpline[2])
                    #print(tmpline)
            with open("stoploss.txt") as slfile , open("stoplossnew.txt",'a') as newfile:
                for line in slfile:
                    if line.split(",")[2] not in symbol_to_remove:
                        newfile.write(line)
                os.system("mv stoplossnew.txt stoploss.txt")
            if os.path.getsize("stoploss.txt") == 0:
                os.system("rm stoploss.txt")


def sell_fno_symbol(symbol,n):
    if symbol not in list_of_open_position():
        with open("stoploss.txt") as slfile , open("stoplossnew.txt",'a') as newfile:
            for line in slfile:
                if symbol not in line:
                    newfile.write(line)
            os.system("mv stoplossnew.txt stoploss.txt")
        return None
    quantity = get_quantity(symbol)
    quantity= quantity*n
    c=ltp_fno_symbol(symbol)
    print("==SELLING FNO SYMBOL==")
    print(symbol)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='SELL', quantity=quantity, product='NRML', order_type='LIMIT', price=c-2, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)

def buy_fno_symbol(symbol,n):
    c=ltp_fno_symbol(symbol)
    quantity = get_quantity(symbol)
    quantity=quantity*n
    print("==BUYING FNO SYMBOL==")
    print(symbol)
    print(c)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='LIMIT', price=c+2, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    set_sl(symbol)

def handle_call(symbol):
    global candle_store
    high_list=[]
    for candle in candle_store[symbol]:
        h=candle["high"]
        high_list.append(h)
    
    #if ltp_dic[symbol]>last_high[symbol] and high_list[-2]<high_list[-3] and high_list[-3]<high_list[-4]:
    if ltp_dic[symbol]>last_high[symbol]:
        if check_call_correction(high_list) == True:
            fnosymbol=getfnosymbol(symbol)
            buy_fno_symbol(fnosymbol,1)
            del call_dic[symbol]
            remove_str_from_file("orderlist.txt",symbol)
        #exit()

def handle_put(symbol):
    global candle_store
    low_list=[]
    for candle in candle_store[symbol]:
        l=candle["low"]
        low_list.append(l)

#    if ltp_dic[symbol]<last_low[symbol] and low_list[-2]>low_list[-3] and low_list[-3]>low_list[-4]:
    if ltp_dic[symbol]<last_low[symbol]:
        if check_put_correction(low_list) == True:
            fnosymbol=getfnosymbol(symbol)
            buy_fno_symbol(fnosymbol,1)
            del put_dic[symbol]
            remove_str_from_file("orderlist.txt",symbol)
        #exit()

def buy_on_correction():
    update_high_low_dic()
    update_ltp_dic()
    call_wl,put_wl=get_watch_list()

    for symbol in call_wl:
        handle_call(symbol)
    for symbol in put_wl:
        handle_put(symbol)

def list_of_open_position():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        if dic['quantity'] > 0:
            open_position_list.append(dic['tradingsymbol'])
    return open_position_list

def is_new_key():
    global old_keys
    total_keys=list(call_dic.keys())+list(put_dic.keys())
    #print(old_keys)
    #print(total_keys)

    if set(total_keys) != set(old_keys):
        print("got new key in orderlist.txt")
        old_keys=total_keys
        return True

def main_function():
    global candle_flag
    while True:
        check_sl()
        if os.path.isfile(filename) and os.path.getsize(filename)!=0:
            global call_dic
            global put_dic
            call_dic,put_dic=get_call_put_dic(filename)
            if candle_flag == 1:
                candle_flag = 0
            if is_new_key() == True:
                candle_flag=1
            buy_on_correction()
        time.sleep(3)

main_function()
