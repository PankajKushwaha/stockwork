from kiteconnect import KiteConnect
from set_token import *
import os
import shutil
import pyautogui
import cv2
import time
import numpy as np
import time


core_dict = {}

fnolist =  ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BIOCON', 'BRITANNIA', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'BANKBARODA', 'CANBK', 'COFORGE', 'COLPAL', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'LTTS', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'SHREECEM', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'GUJGASLTD', 'MARICO', 'LICHSGFIN', 'NATIONALUM', 'MUTHOOTFIN', 'NMDC', 'RAMCOCEM', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'TORNTPHARM', 'TVSMOTOR', 'BOSCHLTD', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI', 'ZEEL', 'PEL', 'PNB', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'TORNTPOWER', 'VEDL', 'GMRINFRA', 'PFC', 'VOLTAS', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']

#fnolist = ["3MINDIA","ABB","POWERINDIA","ACC","AIAENG","APLAPOLLO","AUBANK","AARTIDRUGS","AARTIIND","AAVAS","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ABCAPITAL","ABFRL","ADVENZYMES","AEGISCHEM","AFFLE","AJANTPHARM","AKZOINDIA","ALEMBICLTD","APLLTD","ALKEM","ALKYLAMINE","ALOKINDS","AMARAJABAT","AMBER","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASHOKA","ASIANPAINT","ASTERDM","ASTRAZEN","ASTRAL","ATUL","AUROPHARMA","AVANTIFEED","DMART","AXISBANK","BASF","BEML","BSE","BAJAJ-AUTO","BAJAJCON","BAJAJELEC","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BALMLAWRIE","BALRAMCHIN","BANDHANBNK","BANKBARODA","BANKINDIA","MAHABANK","BATAINDIA","BAYERCROP","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARATRAS","BHARTIARTL","BIOCON","BIRLACORPN","BSOFT","BLISSGVS","BLUEDART","BLUESTARCO","BBTC","BOMDYEING","BOSCHLTD","BRIGADE","BRITANNIA","CARERATING","CCL","CESC","CRISIL","CSBBANK","CADILAHC","CANFINHOME","CANBK","CAPLIPOINT","CGCL","CARBORUNIV","CASTROLIND","CEATLTD","CENTRALBK","CENTURYPLY","CENTURYTEX","CERA","CHALET","CHAMBLFERT","CHENNPETRO","CHOLAHLDNG","CHOLAFIN","CIPLA","CUB","COALINDIA","COCHINSHIP","COFORGE","COLPAL","CONCOR","COROMANDEL","CREDITACC","CROMPTON","CUMMINSIND","CYIENT","DBCORP","DCBBANK","DCMSHRIRAM","DLF","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DHANI","DHANUKA","DBL","DISHTV","DCAL","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EIDPARRY","EIHOTEL","EPL","ESABINDIA","EDELWEISS","EICHERMOT","ELGIEQUIP","EMAMILTD","ENDURANCE","ENGINERSIN","EQUITAS","ERIS","ESCORTS","EXIDEIND","FDC","FEDERALBNK","FINEORG","FINCABLES","FINPIPE","FSL","FORTIS","FCONSUMER","FRETAIL","GAIL","GEPIL","GHCL","GMMPFAUDLR","GMRINFRA","GALAXYSURF","GRSE","GARFIBRES","GICRE","GILLETTE","GLAXO","GLENMARK","GODFRYPHLP","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRANULES","GRAPHITE","GRASIM","GESHIP","GREAVESCOT","GRINDWELL","GUJALKALI","GAEL","FLUOROCHEM","GUJGASLTD","GMDCLTD","GNFC","GPPL","GSFC","GSPL","GULFOILLUB","HEG","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HATHWAY","HATSUN","HAVELLS","HEIDELBERG","HERITGFOOD","HEROMOTOCO","HSCL","HINDALCO","HAL","HINDCOPPER","HINDPETRO","HINDUNILVR","HINDZINC","HONAUT","HUDCO","HDFC","HUHTAMAKI","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","ICRA","IDBI","IDFCFIRSTB","IDFC","IFBIND","IIFL","IIFLWAM","IOLCP","IRB","IRCON","ITC","ITI","INDIACEM","IBULHSGFIN","IBREALEST","INDIAMART","INDIANB","IEX","INDHOTEL","IOC","IOB","IRCTC","INDOCO","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INGERRAND","INOXLEISUR","INDIGO","IPCALAB","JBCHEPHARM","JKCEMENT","JKLAKSHMI","JKPAPER","JKTYRE","JMFINANCIL","JSWSTEEL","JTEKTINDIA","JAGRAN","JAICORPLTD","J&KBANK","JAMNAAUTO","JINDALSAW","JSLHISAR","JSL","JINDALSTEL","JCHAC","JUBLFOOD","JUSTDIAL","JYOTHYLAB","KEI","KNRCON","KRBL","KSB","KAJARIACER","KALPATPOWR","KANSAINER","KTKBANK","KARURVYSYA","KSCL","KEC","KOLTEPATIL","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LAOPALA","LAXMIMACH","LTI","LT","LAURUSLABS","LEMONTREE","LINDEINDIA","LUPIN","LUXIND","MASFIN","MMTC","MOIL","MRF","MGL","MAHSCOOTER","MAHSEAMLES","M&MFIN","M&M","MAHINDCIE","MHRIL","MAHLOG","MANAPPURAM","MRPL","MARICO","MARUTI","MFSL","METROPOLIS","MINDTREE","MINDACORP","MINDAIND","MIDHANI","MOTHERSUMI","MOTILALOFS","MPHASIS","MCX","MUTHOOTFIN","NATCOPHARM","NBCC","NCC","NESCO","NHPC","NLCINDIA","NMDC","NOCIL","NTPC","NH","NATIONALUM","NFL","NAVINFLUOR","NAVNETEDUL","NESTLEIND","NETWORK18","NILKAMAL","NAM-INDIA","OBEROIRLTY","ONGC","OIL","OMAXE","OFSS","ORIENTCEM","ORIENTELEC","PIIND","PNBHOUSING","PNCINFRA","PSPPROJECT","PTC","PVR","PAGEIND","PERSISTENT","PETRONET","PFIZER","PHILIPCARB","PHOENIXLTD","PIDILITIND","PEL","POLYMED","POLYCAB","POLYPLEX","PFC","POWERGRID","PRESTIGE","PRSMJOHNSN","PGHL","PGHH","PNB","QUESS","RBLBANK","RECLTD","RITES","RADICO","RVNL","RAIN","RAJESHEXPO","RALLIS","RCF","RATNAMANI","RAYMOND","REDINGTON","RELAXO","RELIANCE","SBICARD","SBILIFE","SIS","SJVN","SKFINDIA","SRF","SANOFI","SCHAEFFLER","SCHNEIDER","SEQUENT","SFL","SHILPAMED","SCI","SHOPERSTOP","SHREECEM","SHRIRAMCIT","SRTRANSFIN","SIEMENS","SOBHA","SOLARINDS","SOLARA","SONATSOFTW","SOUTHBANK","SPICEJET","STARCEMENT","SBIN","SAIL","SWSOLAR","STLTECH","STAR","SUDARSCHEM","SUMICHEM","SPARC","SUNPHARMA","SUNTV","SUNDARMFIN","SUNDRMFAST","SUNTECK","SUPRAJIT","SUPREMEIND","SUPPETRO","SUVENPHAR","SUZLON","SWANENERGY","SWARAJENG","SYMPHONY","SYNGENE","TCIEXP","TCNSBRANDS","TTKPRESTIG","TVTODAY","TV18BRDCST","TVSMOTOR","TASTYBITE","TATACHEM","TATACOFFEE","TATACOMM","TCS","TATACONSUM","TATAELXSI","TATAINVEST","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTEEL","TEAMLEASE","TECHM","NIACL","RAMCOCEM","THERMAX","THYROCARE","TIMKEN","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TRIDENT","TIINDIA","UCOBANK","UFLEX","UPL","UJJIVAN","UJJIVANSFB","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VMART","VIPIND","VRLLOG","VSTIND","VAIBHAVGBL","VAKRANGEE","VTL","VARROC","VBL","VENKEYS","VINATIORGA","IDEA","VOLTAS","WABCOINDIA","WELCORP","WELSPUNIND","WESTLIFE","WHIRLPOOL","WIPRO","WOCKPHARMA","YESBANK","ZEEL","ZENSARTECH","ZYDUSWELL","ECLERX"]

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
        if c>o and c> (h - fraction ) and o > (h-(fraction*4)): 
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
        if c>o and ((c-o)/(h-l)) > 0.9: 
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

def init_dict():
    for symbol in fnolist:
        core_dict[symbol]=[]



kite = set_token()

kite_ohlc_dict = get_ohlc_dict(fnolist)
print_all_ohlc(fnolistnse)
init_dict()
#green_hammer(fnolistnse)
strong_bull(fnolistnse)
strong_bear(fnolistnse)
#inverted_red_hammer(fnolistnse)
#minimum_candle(fnolistnse)

#print(kite.ohlc(fnolistnse))
#ohlc_dict=kite.ohlc(fnolistnse)
#print_all_ohlc(fnolist)
#print(ohlc_dict["NSE:ZEEL"]["ohlc"]["open"])

#print(kite_get_ohlc(ohlc_dict,"HCLTECH"))
