import yfinance as yf
import pandas as pd
from nsetools import Nse
import pyautogui
import time
import cv2
import numpy as np

nse = Nse()

NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M&M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]

NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M&M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL-N","WIPRO"]

NIFTY200 = ["AARTIIND","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ATGL","ADANIGREEN","ADANIPORTS","ADANITRANS","AJANTPHARM","ALKEM","AMARAJABAT","AMBUJACEM","APLLTD","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJAJHLDNG","BAJFINANCE","BALKRISIND","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BBTC","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","CADILAHC","CANBK","CASTROLIND","CESC","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DHANI","DIVISLAB","DLF","DMART","DRREDDY","EDELWEISS","EICHERMOT","EMAMILTD","ENDURANCE","ESCORTS","EXIDEIND","FEDERALBNK","FORTIS","FRETAIL","GAIL","GICRE","GLENMARK","GMRINFRA","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRASIM","GSPL","GUJGASLTD","HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HUDCO","IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFCFIRSTB","IGL","INDHOTEL","INDIGO","INDUSINDBK","INDUSTOWER","INFY","IOC","IPCALAB","IRCTC","ISEC","ITC","JINDALSTEL","JSWENERGY","JSWSTEEL","JUBLFOOD","KOTAKBANK","L&TFH","LALPATHLAB","LICHSGFIN","LT","LTI","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MFSL","MGL","MINDTREE","MOTHERSUMI","MPHASIS","MRF","MUTHOOTFIN","NAM-INDIA","NATCOPHARM","NATIONALUM","NAUKRI","NAVINFLUOR","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","OIL","ONGC","PAGEIND","PEL","PETRONET","PFC","PFIZER","PGHH","PIDILITIND","PIIND","PNB","POLYCAB","POWERGRID","PRESTIGE","RAJESHEXPO","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SANOFI","SBICARD","SBILIFE","SBIN","SHREECEM","SIEMENS","SRF","SRTRANSFIN","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACONSUM","TATAMOTORS","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UNIONBANK","UPL","VBL","VGUARD","VOLTAS","WHIRLPOOL","WIPRO","YESBANK","ZEEL"]

NIFTY500 = ["3MINDIA","ABB","POWERINDIA","ACC","AIAENG","APLAPOLLO","AUBANK","AARTIDRUGS","AARTIIND","AAVAS","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ATGL","ADANITRANS","ABCAPITAL","ABFRL","ADVENZYMES","AEGISCHEM","AFFLE","AJANTPHARM","AKZOINDIA","ALEMBICLTD","APLLTD","ALKEM","ALKYLAMINE","ALOKINDS","AMARAJABAT","AMBER","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASHOKA","ASIANPAINT","ASTERDM","ASTRAZEN","ASTRAL","ATUL","AUROPHARMA","AVANTIFEED","DMART","AXISBANK","BASF","BEML","BSE","BAJAJ-AUTO","BAJAJCON","BAJAJELEC","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BALMLAWRIE","BALRAMCHIN","BANDHANBNK","BANKBARODA","BANKINDIA","MAHABANK","BATAINDIA","BAYERCROP","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARATRAS","BHARTIARTL","BIOCON","BIRLACORPN","BSOFT","BLISSGVS","BLUEDART","BLUESTARCO","BBTC","BOMDYEING","BOSCHLTD","BRIGADE","BRITANNIA","CARERATING","CCL","CESC","CRISIL","CSBBANK","CADILAHC","CANFINHOME","CANBK","CAPLIPOINT","CGCL","CARBORUNIV","CASTROLIND","CEATLTD","CENTRALBK","CDSL","CENTURYPLY","CENTURYTEX","CERA","CHALET","CHAMBLFERT","CHENNPETRO","CHOLAHLDNG","CHOLAFIN","CIPLA","CUB","COALINDIA","COCHINSHIP","COFORGE","COLPAL","CONCOR","COROMANDEL","CREDITACC","CROMPTON","CUMMINSIND","CYIENT","DBCORP","DCBBANK","DCMSHRIRAM","DLF","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DHANI","DHANUKA","DBL","DISHTV","DCAL","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EIDPARRY","EIHOTEL","EPL","ESABINDIA","EDELWEISS","EICHERMOT","ELGIEQUIP","EMAMILTD","ENDURANCE","ENGINERSIN","EQUITAS","ERIS","ESCORTS","EXIDEIND","FDC","FEDERALBNK","FINEORG","FINCABLES","FINPIPE","FSL","FORTIS","FCONSUMER","FRETAIL","GAIL","GEPIL","GHCL","GMMPFAUDLR","GMRINFRA","GALAXYSURF","GRSE","GARFIBRES","GICRE","GILLETTE","GLAXO","GLENMARK","GODFRYPHLP","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRANULES","GRAPHITE","GRASIM","GESHIP","GREAVESCOT","GRINDWELL","GUJALKALI","GAEL","FLUOROCHEM","GUJGASLTD","GMDCLTD","GNFC","GPPL","GSFC","GSPL","GULFOILLUB","HEG","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HFCL","HATHWAY","HATSUN","HAVELLS","HEIDELBERG","HERITGFOOD","HEROMOTOCO","HSCL","HINDALCO","HAL","HINDCOPPER","HINDPETRO","HINDUNILVR","HINDZINC","HONAUT","HUDCO","HDFC","HUHTAMAKI","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","ICRA","IDBI","IDFCFIRSTB","IDFC","IFBIND","IIFL","IIFLWAM","IOLCP","IRB","IRCON","ITC","ITI","INDIACEM","IBULHSGFIN","IBREALEST","INDIAMART","INDIANB","IEX","INDHOTEL","IOC","IOB","IRCTC","INDOCO","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INGERRAND","INOXLEISUR","INDIGO","IPCALAB","JBCHEPHARM","JKCEMENT","JKLAKSHMI","JKPAPER","JKTYRE","JMFINANCIL","JSWENERGY","JSWSTEEL","JTEKTINDIA","JAGRAN","JAICORPLTD","J&KBANK","JAMNAAUTO","JINDALSAW","JSLHISAR","JSL","JINDALSTEL","JCHAC","JUBLFOOD","JUSTDIAL","JYOTHYLAB","KEI","KNRCON","KRBL","KSB","KAJARIACER","KALPATPOWR","KANSAINER","KTKBANK","KARURVYSYA","KSCL","KEC","KOLTEPATIL","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LAOPALA","LAXMIMACH","LTI","LT","LAURUSLABS","LEMONTREE","LINDEINDIA","LUPIN","LUXIND","MASFIN","MMTC","MOIL","MRF","MGL","MAHSCOOTER","MAHSEAMLES","M&MFIN","M&M","MAHINDCIE","MHRIL","MAHLOG","MANAPPURAM","MRPL","MARICO","MARUTI","MFSL","METROPOLIS","MINDTREE","MINDACORP","MINDAIND","MIDHANI","MOTHERSUMI","MOTILALOFS","MPHASIS","MCX","MUTHOOTFIN","NATCOPHARM","NBCC","NCC","NESCO","NHPC","NLCINDIA","NMDC","NOCIL","NTPC","NH","NATIONALUM","NFL","NAVINFLUOR","NAVNETEDUL","NESTLEIND","NETWORK18","NILKAMAL","NAM-INDIA","OBEROIRLTY","ONGC","OIL","OMAXE","OFSS","ORIENTCEM","ORIENTELEC","ORIENTREF","PIIND","PNBHOUSING","PNCINFRA","PSPPROJECT","PTC","PVR","PAGEIND","PERSISTENT","PETRONET","PFIZER","PHILIPCARB","PHOENIXLTD","PIDILITIND","PEL","POLYMED","POLYCAB","POLYPLEX","PFC","POWERGRID","PRAJIND","PRESTIGE","PRSMJOHNSN","PGHL","PGHH","PNB","QUESS","RBLBANK","RECLTD","RITES","RADICO","RVNL","RAIN","RAJESHEXPO","RALLIS","RCF","RATNAMANI","RAYMOND","REDINGTON","RELAXO","RELIANCE","SBICARD","SBILIFE","SIS","SJVN","SKFINDIA","SRF","SANOFI","SCHAEFFLER","SCHNEIDER","SEQUENT","SFL","SHILPAMED","SCI","SHOPERSTOP","SHREECEM","SHRIRAMCIT","SRTRANSFIN","SIEMENS","SOBHA","SOLARINDS","SOLARA","SONATSOFTW","SOUTHBANK","SPICEJET","STARCEMENT","SBIN","SAIL","SWSOLAR","STLTECH","STAR","SUDARSCHEM","SUMICHEM","SPARC","SUNPHARMA","SUNTV","SUNDARMFIN","SUNDRMFAST","SUNTECK","SUPRAJIT","SUPREMEIND","SUPPETRO","SUVENPHAR","SUZLON","SWANENERGY","SWARAJENG","SYMPHONY","SYNGENE","TCIEXP","TCNSBRANDS","TTKPRESTIG","TVTODAY","TV18BRDCST","TVSMOTOR","TASTYBITE","TATACHEM","TATACOFFEE","TATACOMM","TCS","TATACONSUM","TATAELXSI","TATAINVEST","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTLBSL","TATASTEEL","TEAMLEASE","TECHM","NIACL","RAMCOCEM","THERMAX","THYROCARE","TIMKEN","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TRIDENT","TIINDIA","UCOBANK","UFLEX","UPL","UJJIVAN","UJJIVANSFB","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VMART","VIPIND","VRLLOG","VSTIND","VAIBHAVGBL","VAKRANGEE","VTL","VARROC","VBL","VENKEYS","VINATIORGA","IDEA","VOLTAS","WABCOINDIA","WELCORP","WELSPUNIND","WESTLIFE","WHIRLPOOL","WIPRO","WOCKPHARMA","YESBANK","ZEEL","ZENSARTECH","ZYDUSWELL","ECLERX"]

stock_list = []
percent_margin = 0.01
ma_margin = 0.3
df = pd.read_csv('./monthly_pivot_nifty500_JUN.csv')


def less_by_margin(level):
    return (level - (level*percent_margin))

def more_by_margin(level):
    return (level + (level*percent_margin))

def bullish_engulf_weak(stock,data):
    h1 = float(data.tail(1)["High"])
    l1 = float(data.tail(1)["Low"])
    h2 = float(data.tail(2).head(1)["High"])
    l2 = float(data.tail(2).head(1)["Low"])
    h3 = float(data.head(1)["High"])
    l3 = float(data.head(1)["Low"])
    if l1<l2 and l1<l3 and h1>h2 and h1>h3:
           stock_list.append(stock)

def bullish_engulf_strong(stock,data):
    h1 = float(data.tail(1)["High"])
    l1 = float(data.tail(1)["Low"])
    h2 = float(data.tail(2).head(1)["High"])
    l2 = float(data.tail(2).head(1)["Low"])
    o1 = float(data.tail(1)["Open"])
    c1 = float(data.tail(1)["Close"])
    o2 = float(data.tail(2).head(1)["Open"])
    c2 = float(data.tail(2).head(1)["Close"])
    # yesterday red today green
    if c2<o2 and o1<c1:
        if o1<c2 and l1<l2 and c1>o2 and h1>h2:
            print(data)
            stock_list.append(stock)

def is_near_month_pivot(stock,lastPrice):
    if lastPrice is None:
        return

    R2 =df[df["symbol"]==stock]["R2"]
    if len(R2) == 0:
        return
    
    R2=float(R2)

    if lastPrice > less_by_margin(R2) and lastPrice < more_by_margin(R2):
        stock_list.append(stock)

    R1 = float(df[df["symbol"]==stock]["R1"])
    if lastPrice > less_by_margin(R1) and lastPrice < more_by_margin(R1):
        stock_list.append(stock)

    top_cpr = float(df[df["symbol"]==stock]["top_cpr"])
    if lastPrice < more_by_margin(top_cpr) and lastPrice > top_cpr:
        stock_list.append(stock)

    bottom_cpr = float(df[df["symbol"]==stock]["bottom_cpr"])
    if lastPrice > less_by_margin(bottom_cpr) and lastPrice < bottom_cpr:
        stock_list.append(stock)

    S2 = float(df[df["symbol"]==stock]["S2"])
    if lastPrice > less_by_margin(S2) and lastPrice < more_by_margin(S2):
        stock_list.append(stock)


    S1 = float(df[df["symbol"]==stock]["S1"])
    if lastPrice > less_by_margin(S1) and lastPrice < more_by_margin(S1):
        stock_list.append(stock)

def higer_high_lower_high(stock,data):
    h1 = float(data.tail(1)["High"])
    l1 = float(data.tail(1)["Low"])
    h2 = float(data.tail(2).head(1)["High"])
    l2 = float(data.tail(2).head(1)["Low"])
    h3 = float(data.head(1)["High"])
    l3 = float(data.head(1)["Low"])

    if h1>h2>h3 and l1>l2>l3:
        dh1 = h1 - h2
        dh2 = h2 - h3
        dl1 = l1 - l2
        dl2 = l2 - l3
        r1 = float(dh1/dh2)
        r2 = float(dl1/dl2)
        if 0.7<r1<1.3 and 0.7<r2<1.3:
            stock_list.append(stock)

def high_eq_ltp(stock,data):
    c = float(data["Close"])
    h = float(data["High"])
    if c == h or c > h - (h/100)*0.2:
        stock_list.append(stock)

def low_eq_open(stock,data):
    l = float(data["Low"])
    o = float(data["Open"])
    if l == o or o < l+ (l/100)*0.2:
        stock_list.append(stock)

def green_hammer(stock,data):
    low = float(data.tail(1)["Low"])
    high = float(data.tail(1)["High"])
    openPrice = float(data.tail(1)["Open"])
    close = float(data.tail(1)["Close"])

    if (close-openPrice) !=0:
        if (high - low ) / (close - openPrice) > 5:
            print(stock)
            stock_list.append(stock)

def closing_20_40_200ma(stock,data):
    ma20=float(sum(data.tail(20)["Close"]))/20
    ma40=float(sum(data.tail(40)["Close"]))/40
    ma200=float(sum(data.tail(200)["Close"]))/200
    ltp=float(data.tail(1)["Close"])

    if (ma20+((ma20/100)*ma_margin) > ltp and ma20-((ma20/100)*ma_margin) < ltp) or \
        (ma40+((ma40/100)*ma_margin) > ltp and ma40-((ma40/100)*ma_margin) < ltp) or \
        (ma200+((ma200/100)*ma_margin) > ltp and ma200-((ma200/100)*ma_margin) < ltp):
            stock_list.append(stock)
            print(stock)

count = 1
start = time.time()
for stock in NIFTY500:
    data = yf.download(stock+".NS",period="200d")
    if data is None:
        continue
    print(stock)
    higer_high_lower_high(stock,data)
    is_near_month_pivot(stock,float(data.tail(1)["Close"]))
    bullish_engulf_weak(stock,data.tail(3))
    high_eq_ltp(stock,data.tail(1))
    low_eq_open(stock,data.tail(1))
    
    #verify with new data
    bullish_engulf_strong(stock,data)
    green_hammer(stock,data)
    closing_20_40_200ma(stock,data)
    time.sleep(1)
    

stock_list = sorted(list(set(stock_list)))

print(stock_list)
    
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
    cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)

end = time.time()
print("time duration")
print(end - start)
