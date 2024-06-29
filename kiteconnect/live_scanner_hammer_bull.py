from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
import operator

#fnolist =  ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BIOCON', 'BRITANNIA', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'BANKBARODA', 'CANBK', 'COFORGE', 'COLPAL', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'LTTS', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI','MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'SHREECEM', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'GUJGASLTD', 'MARICO', 'LICHSGFIN', 'NATIONALUM', 'MUTHOOTFIN', 'NMDC', 'RAMCOCEM', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'TORNTPHARM', 'TVSMOTOR', 'BOSCHLTD', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI', 'ZEEL', 'PEL', 'PNB', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'TORNTPOWER', 'VEDL', 'GMRINFRA', 'PFC', 'VOLTAS', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']

#fnolist = ["3MINDIA","ABB","POWERINDIA","ACC","AIAENG","APLAPOLLO","AUBANK","AARTIDRUGS","AARTIIND","AAVAS","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ABCAPITAL","ABFRL","ADVENZYMES","AEGISCHEM","AFFLE","AJANTPHARM","AKZOINDIA","ALEMBICLTD","APLLTD","ALKEM","ALKYLAMINE","ALOKINDS","AMARAJABAT","AMBER","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASHOKA","ASIANPAINT","ASTERDM","ASTRAZEN","ASTRAL","ATUL","AUROPHARMA","AVANTIFEED","DMART","AXISBANK","BASF","BEML","BSE","BAJAJ-AUTO","BAJAJCON","BAJAJELEC","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BALMLAWRIE","BALRAMCHIN","BANDHANBNK","BANKBARODA","BANKINDIA","MAHABANK","BATAINDIA","BAYERCROP","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARATRAS","BHARTIARTL","BIOCON","BIRLACORPN","BSOFT","BLISSGVS","BLUEDART","BLUESTARCO","BBTC","BOMDYEING","BOSCHLTD","BRIGADE","BRITANNIA","CARERATING","CCL","CESC","CRISIL","CSBBANK","CADILAHC","CANFINHOME","CANBK","CAPLIPOINT","CGCL","CARBORUNIV","CASTROLIND","CEATLTD","CENTRALBK","CDSL","CENTURYPLY","CENTURYTEX","CERA","CHALET","CHAMBLFERT","CHENNPETRO","CHOLAHLDNG","CHOLAFIN","CIPLA","CUB","COALINDIA","COCHINSHIP","COFORGE","COLPAL","CONCOR","COROMANDEL","CREDITACC","CROMPTON","CUMMINSIND","CYIENT","DBCORP","DCBBANK","DCMSHRIRAM","DLF","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DHANI","DHANUKA","DBL","DCAL","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EIDPARRY","EIHOTEL","EPL","ESABINDIA","EDELWEISS","EICHERMOT","ELGIEQUIP","EMAMILTD","ENDURANCE","ENGINERSIN","EQUITAS","ERIS","ESCORTS","EXIDEIND","FDC","FEDERALBNK","FINEORG","FINCABLES","FINPIPE","FSL","FORTIS","FCONSUMER","FRETAIL","GAIL","GEPIL","GHCL","GMMPFAUDLR","GMRINFRA","GALAXYSURF","GRSE","GARFIBRES","GICRE","GILLETTE","GLAXO","GLENMARK","GODFRYPHLP","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRANULES","GRAPHITE","GRASIM","GESHIP","GREAVESCOT","GRINDWELL","GUJALKALI","GAEL","GUJGASLTD","GMDCLTD","GNFC","GPPL","GSFC","GSPL","GULFOILLUB","HEG","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HFCL","HATHWAY","HATSUN","HAVELLS","HEIDELBERG","HERITGFOOD","HEROMOTOCO","HSCL","HINDALCO","HAL","HINDCOPPER","HINDPETRO","HINDUNILVR","HINDZINC","HONAUT","HUDCO","HDFC","HUHTAMAKI","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","ICRA","IDBI","IDFCFIRSTB","IDFC","IFBIND","IIFL","IIFLWAM","IOLCP","IRB","IRCON","ITC","ITI","INDIACEM","IBULHSGFIN","IBREALEST","INDIAMART","INDIANB","IEX","INDHOTEL","IOC","IOB","IRCTC","INDOCO","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INGERRAND","INOXLEISUR","INDIGO","IPCALAB","JBCHEPHARM","JKCEMENT","JKLAKSHMI","JKPAPER","JKTYRE","JMFINANCIL","JSWSTEEL","JTEKTINDIA","JAGRAN","JAICORPLTD","J&KBANK","JAMNAAUTO","JINDALSAW","JSLHISAR","JSL","JINDALSTEL","JCHAC","JUBLFOOD","JUSTDIAL","JYOTHYLAB","KEI","KNRCON","KRBL","KSB","KAJARIACER","KALPATPOWR","KANSAINER","KTKBANK","KARURVYSYA","KSCL","KEC","KOLTEPATIL","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LAOPALA","LAXMIMACH","LTI","LT","LAURUSLABS","LEMONTREE","LINDEINDIA","LUPIN","LUXIND","MASFIN","MMTC","MOIL","MRF","MGL","MAHSCOOTER","MAHSEAMLES","M&MFIN","M&M","MAHINDCIE","MHRIL","MAHLOG","MANAPPURAM","MRPL","MARICO","MARUTI","MFSL","METROPOLIS","MINDTREE","MINDACORP","MINDAIND","MIDHANI","MOTHERSUMI","MOTILALOFS","MPHASIS","MCX","MUTHOOTFIN","NATCOPHARM","NBCC","NCC","NESCO","NHPC","NLCINDIA","NMDC","NOCIL","NTPC","NH","NATIONALUM","NFL","NAVINFLUOR","NAVNETEDUL","NESTLEIND","NETWORK18","NILKAMAL","NAM-INDIA","OBEROIRLTY","ONGC","OIL","OMAXE","OFSS","ORIENTELEC","PIIND","PNBHOUSING","PNCINFRA","PSPPROJECT","PTC","PVR","PAGEIND","PERSISTENT","PETRONET","PFIZER","PHOENIXLTD","PIDILITIND","PEL","POLYMED","POLYCAB","POLYPLEX","PFC","POWERGRID","PRESTIGE","PRSMJOHNSN","PGHL","PGHH","PNB","QUESS","RBLBANK","RECLTD","RITES","RADICO","RVNL","RAIN","RAJESHEXPO","RALLIS","RCF","RATNAMANI","RAYMOND","REDINGTON","RELAXO","RELIANCE","SBICARD","SBILIFE","SIS","SJVN","SKFINDIA","SRF","SANOFI","SCHAEFFLER","SCHNEIDER","SEQUENT","SFL","SHILPAMED","SCI","SHOPERSTOP","SHREECEM","SHRIRAMCIT","SRTRANSFIN","SIEMENS","SOBHA","SOLARINDS","SOLARA","SONATSOFTW","SOUTHBANK","SPICEJET","STARCEMENT","SBIN","SAIL","SWSOLAR","STLTECH","STAR","SUDARSCHEM","SUMICHEM","SPARC","SUNPHARMA","SUNTV","SUNDARMFIN","SUNDRMFAST","SUNTECK","SUPRAJIT","SUPREMEIND","SUPPETRO","SUVENPHAR","SUZLON","SWANENERGY","SWARAJENG","SYMPHONY","SYNGENE","TCIEXP","TCNSBRANDS","TTKPRESTIG","TVTODAY","TV18BRDCST","TVSMOTOR","TASTYBITE","TATACHEM","TATACOFFEE","TATACOMM","TCS","TATACONSUM","TATAELXSI","TATAINVEST","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTEEL","TEAMLEASE","TECHM","NIACL","RAMCOCEM","THERMAX","THYROCARE","TIMKEN","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TIINDIA","UCOBANK","UFLEX","UPL","UJJIVAN","UJJIVANSFB","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VMART","VIPIND","VRLLOG","VSTIND","VAIBHAVGBL","VAKRANGEE","VTL","VARROC","VBL","VENKEYS","VINATIORGA","IDEA","VOLTAS","WABCOINDIA","WELCORP","WELSPUNIND","WESTLIFE","WHIRLPOOL","WIPRO","WOCKPHARMA","YESBANK","ZEEL","ZENSARTECH","ZYDUSWELL","ECLERX"]

fnolist = ["IDEA","UBL","MINDTREE","LALPATHLAB","JUBLFOOD","METROPOLIS","BHEL","ALKEM","EICHERMOT","COROMANDEL","ULTRACEMCO","CUB","CANBK","ACC","COFORGE","AMBUJACEM","BAJFINANCE","RAMCOCEM","CADILAHC","ICICIGI","BATAINDIA","IRCTC","TORNTPHARM","ADANIPORTS","GRASIM","BAJAJFINSV","TRENT","INDUSTOWER","PFIZER","TORNTPOWER","ADANIENT","NESTLEIND","CONCOR","TATACONSUM","BIOCON","NAVINFLUOR","MRF","CUMMINSIND","HAVELLS","ASTRAL","MARICO","BRITANNIA","SRTRANSFIN","BANKBARODA","IDFCFIRSTB","AARTIIND","CIPLA","SHREECEM","NAUKRI","PAGEIND","HDFCLIFE","DLF","PIDILITIND","IOC","MGL","DEEPAKNTR","TCS","RELIANCE","UPL","DABUR","RECLTD","BERGEPAINT","ICICIPRULI","HDFCAMC","NAM-INDIA","HINDUNILVR","ITC","TITAN","PETRONET","MPHASIS","GMRINFRA","DIVISLAB","L&TFH","PEL","HINDPETRO","M&M","TECHM","VOLTAS","SUNPHARMA","LTTS","PFC","MUTHOOTFIN","BOSCHLTD","AMARAJABAT","LTI","HDFCBANK","GODREJCP","FEDERALBNK","INDHOTEL","GLENMARK","EXIDEIND","ABFRL","LUPIN","DRREDDY","M&MFIN","TATASTEEL","BPCL","LT","TATAPOWER","ASIANPAINT","INFY","HEROMOTOCO","COALINDIA","NTPC","ONGC","TATACHEM","BHARTIARTL","SBIN","INDIGO","NMDC","MARUTI","PVR","PIIND","STAR","AXISBANK","LICHSGFIN","IGL","CHOLAFIN","APOLLOTYRE","HCLTECH","JSWSTEEL","BALKRISIND","WIPRO","GUJGASLTD","ASHOKLEY","HDFC","RBLBANK","MOTHERSUMI","BHARATFORG","COLPAL","GODREJPROP","APLLTD","BANDHANBNK","SUNTV","ZEEL","INDUSINDBK","GRANULES","SIEMENS","TVSMOTOR","AUBANK","SAIL","GAIL","MFSL","BEL","SRF","POWERGRID","PNB","TATAMOTORS","AUROPHARMA","ESCORTS","SBILIFE","JINDALSTEL","ICICIBANK","MANAPPURAM","HINDALCO","KOTAKBANK","APOLLOHOSP","VEDL","NATIONALUM","IBULHSGFIN"]

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
        fraction = (h-l)/10
        print(c)
        if c>o and c> (h - (fraction*2) ) and o > (h-(fraction*6)): 
            gHammer.append(symbol)
    print("gHammer")
    print(gHammer)
    save_screenshot(gHammer,"green_hammer")


def red_hammer(fnolist):
    rHammer = []
    per_dic = {}
    for symbol in fnolist:
        print(symbol)
        o,h,l,c = kite_get_ohlc(symbol)
        if h!=o :
            continue
        per = ((o-c)/o)*100
        #per_dic[per]=symbol
        per_dic[symbol]=per
    print(per_dic)
    #print(sorted(per_dic, key=per_dic.get, reverse=True)[:5])
    print(dict(sorted(per_dic.items(), key=operator.itemgetter(1) )[:5]).keys())
    a=dict(sorted(per_dic.items(), key=operator.itemgetter(1) )[:5]).keys()
#    print(rHammer)
    save_screenshot(a,"red_hammer")


def inverted_red_hammer(fnolist):
    iHammer = []
    for symbol in fnolist:
        print(symbol)
        o,h,l,c = kite_get_ohlc(symbol)
        fraction = (h-l)/10
        print(c)
        if c<o and c<l+fraction :
            iHammer.append(symbol)
    print("iHammer")
    print(iHammer)
    save_screenshot(iHammer,"inverted_red_hammer")

def near_day_high(fnolist):
    neardayhigh = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        fraction = (h-l)/10
        if c>o and c > (h-fraction): 
            neardayhigh.append(symbol)
    save_screenshot(neardayhigh,"near_Day_high")


def near_day_low(fnolist):
    neardaylow = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        fraction = (h-l)/10
        if c<o and c < (l-fraction):
            neardaylow.append(symbol)
    save_screenshot(neardaylow,"near_Day_low")


def strong_bull(fnolist):
    sbull = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        if c>o and ((c-o)/(h-l)) > 0.7:
            sbull.append(symbol)
    print("bull")
    print(sbull)
    save_screenshot(sbull,"strong_bull")

def buy_stock_max_bull(fnolist):
    sbull = []
    stock_per_change = {}
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        per_change = ((c-o)/o)*100
        stock_per_change[symbol]=per_change

    stock_bull = max(stock_per_change, key=stock_per_change.get)
    o,h,l,c = kite_get_ohlc(stock_bull)
    print(stock_bull)
    stock_bull = stock_bull.replace('NSE:','')
    quantity=int(10000/(c/5))
    print(quantity)
    '''
    kite.place_order(variety='regular', exchange='NSE', tradingsymbol=stock_bull,
            transaction_type='BUY', quantity=int(10000/(c/4)), product='MIS', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    '''
    #print(stock_bear)

def round_number(fnolist):
    rnumber = []
    for symbol in fnolist:
        o,h,l,c = kite_get_ohlc(symbol)
        i=int(c)
        print(symbol)
        while True:
            print(i)
            i=i-1
            if i%100 == 0:
                break
        if c>i and c<(i+(i/100)):
            print("found number")
            rnumber.append(symbol)
    save_screenshot(rnumber,"rnumber")


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
        factor = (((h-l)/l))
        candle_dict[symbol]=factor
        factor_list.append(factor)
        print(symbol)
        print(factor)

    factor_list=sorted(factor_list)
    factor_list = factor_list[:20]
    print(factor_list)
    for i in factor_list:
        k=get_key(candle_dict,i)
        symbol_list.append(k)
    save_screenshot(symbol_list,"min_candle")


def get_ohlc_dict(fnolist):
    for i in fnolist:
        tmp_symbol="NSE:"+i
        fnolistnse.append(tmp_symbol)
    ohlc_dict=kite.ohlc(fnolistnse)
    #print(ohlc_dict)
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
#print_all_ohlc(fnolistnse)
#green_hammer(fnolistnse)
#near_day_high(fnolistnse)
#red_hammer(fnolistnse)
#strong_bull(fnolistnse)
#round_number(fnolistnse)
#strong_bear(fnolistnse)
#strong_bull(fnolistnse)
near_day_high(fnolistnse)
near_day_low(fnolistnse)
#inverted_red_hammer(fnolistnse)
#minimum_candle(fnolistnse)
#buy_stock_max_bull(fnolistnse)

#print(kite.ohlc(fnolistnse))
#ohlc_dict=kite.ohlc(fnolistnse)
#print_all_ohlc(fnolist)
#print(ohlc_dict["NSE:ZEEL"]["ohlc"]["open"])

#print(kite_get_ohlc(ohlc_dict,"HCLTECH"))
