import yfinance as yf
import pandas as pd
from nsetools import Nse
import pyautogui
import time
import cv2
import numpy as np

nse = Nse()

NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M&M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]


NIFTY500 = ["3MINDIA","ABB","POWERINDIA","ACC","AIAENG","APLAPOLLO","AUBANK","AARTIDRUGS","AARTIIND","AAVAS","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ATGL","ADANITRANS","ABCAPITAL","ABFRL","ADVENZYMES","AEGISCHEM","AFFLE","AJANTPHARM","AKZOINDIA","ALEMBICLTD","APLLTD","ALKEM","ALKYLAMINE","ALOKINDS","AMARAJABAT","AMBER","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASHOKA","ASIANPAINT","ASTERDM","ASTRAZEN","ASTRAL","ATUL","AUROPHARMA","AVANTIFEED","DMART","AXISBANK","BASF","BEML","BSE","BAJAJ-AUTO","BAJAJCON","BAJAJELEC","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BALMLAWRIE","BALRAMCHIN","BANDHANBNK","BANKBARODA","BANKINDIA","MAHABANK","BATAINDIA","BAYERCROP","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARATRAS","BHARTIARTL","BIOCON","BIRLACORPN","BSOFT","BLISSGVS","BLUEDART","BLUESTARCO","BBTC","BOMDYEING","BOSCHLTD","BRIGADE","BRITANNIA","CARERATING","CCL","CESC","CRISIL","CSBBANK","CADILAHC","CANFINHOME","CANBK","CAPLIPOINT","CGCL","CARBORUNIV","CASTROLIND","CEATLTD","CENTRALBK","CDSL","CENTURYPLY","CENTURYTEX","CERA","CHALET","CHAMBLFERT","CHENNPETRO","CHOLAHLDNG","CHOLAFIN","CIPLA","CUB","COALINDIA","COCHINSHIP","COFORGE","COLPAL","CONCOR","COROMANDEL","CREDITACC","CROMPTON","CUMMINSIND","CYIENT","DBCORP","DCBBANK","DCMSHRIRAM","DLF","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DHANI","DHANUKA","DBL","DISHTV","DCAL","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EIDPARRY","EIHOTEL","EPL","ESABINDIA","EDELWEISS","EICHERMOT","ELGIEQUIP","EMAMILTD","ENDURANCE","ENGINERSIN","EQUITAS","ERIS","ESCORTS","EXIDEIND","FDC","FEDERALBNK","FINEORG","FINCABLES","FINPIPE","FSL","FORTIS","FCONSUMER","FRETAIL","GAIL","GEPIL","GHCL","GMMPFAUDLR","GMRINFRA","GALAXYSURF","GRSE","GARFIBRES","GICRE","GILLETTE","GLAXO","GLENMARK","GODFRYPHLP","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRANULES","GRAPHITE","GRASIM","GESHIP","GREAVESCOT","GRINDWELL","GUJALKALI","GAEL","FLUOROCHEM","GUJGASLTD","GMDCLTD","GNFC","GPPL","GSFC","GSPL","GULFOILLUB","HEG","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HFCL","HATHWAY","HATSUN","HAVELLS","HEIDELBERG","HERITGFOOD","HEROMOTOCO","HSCL","HINDALCO","HAL","HINDCOPPER","HINDPETRO","HINDUNILVR","HINDZINC","HONAUT","HUDCO","HDFC","HUHTAMAKI","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","ICRA","IDBI","IDFCFIRSTB","IDFC","IFBIND","IIFL","IIFLWAM","IOLCP","IRB","IRCON","ITC","ITI","INDIACEM","IBULHSGFIN","IBREALEST","INDIAMART","INDIANB","IEX","INDHOTEL","IOC","IOB","IRCTC","INDOCO","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INGERRAND","INOXLEISUR","INDIGO","IPCALAB","JBCHEPHARM","JKCEMENT","JKLAKSHMI","JKPAPER","JKTYRE","JMFINANCIL","JSWENERGY","JSWSTEEL","JTEKTINDIA","JAGRAN","JAICORPLTD","J&KBANK","JAMNAAUTO","JINDALSAW","JSLHISAR","JSL","JINDALSTEL","JCHAC","JUBLFOOD","JUSTDIAL","JYOTHYLAB","KEI","KNRCON","KRBL","KSB","KAJARIACER","KALPATPOWR","KANSAINER","KTKBANK","KARURVYSYA","KSCL","KEC","KOLTEPATIL","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LAOPALA","LAXMIMACH","LTI","LT","LAURUSLABS","LEMONTREE","LINDEINDIA","LUPIN","LUXIND","MASFIN","MMTC","MOIL","MRF","MGL","MAHSCOOTER","MAHSEAMLES","M&MFIN","M&M","MAHINDCIE","MHRIL","MAHLOG","MANAPPURAM","MRPL","MARICO","MARUTI","MFSL","METROPOLIS","MINDTREE","MINDACORP","MINDAIND","MIDHANI","MOTHERSUMI","MOTILALOFS","MPHASIS","MCX","MUTHOOTFIN","NATCOPHARM","NBCC","NCC","NESCO","NHPC","NLCINDIA","NMDC","NOCIL","NTPC","NH","NATIONALUM","NFL","NAVINFLUOR","NAVNETEDUL","NESTLEIND","NETWORK18","NILKAMAL","NAM-INDIA","OBEROIRLTY","ONGC","OIL","OMAXE","OFSS","ORIENTCEM","ORIENTELEC","ORIENTREF","PIIND","PNBHOUSING","PNCINFRA","PSPPROJECT","PTC","PVR","PAGEIND","PERSISTENT","PETRONET","PFIZER","PHILIPCARB","PHOENIXLTD","PIDILITIND","PEL","POLYMED","POLYCAB","POLYPLEX","PFC","POWERGRID","PRAJIND","PRESTIGE","PRSMJOHNSN","PGHL","PGHH","PNB","QUESS","RBLBANK","RECLTD","RITES","RADICO","RVNL","RAIN","RAJESHEXPO","RALLIS","RCF","RATNAMANI","RAYMOND","REDINGTON","RELAXO","RELIANCE","SBICARD","SBILIFE","SIS","SJVN","SKFINDIA","SRF","SANOFI","SCHAEFFLER","SCHNEIDER","SEQUENT","SFL","SHILPAMED","SCI","SHOPERSTOP","SHREECEM","SHRIRAMCIT","SRTRANSFIN","SIEMENS","SOBHA","SOLARINDS","SOLARA","SONATSOFTW","SOUTHBANK","SPICEJET","STARCEMENT","SBIN","SAIL","SWSOLAR","STLTECH","STAR","SUDARSCHEM","SUMICHEM","SPARC","SUNPHARMA","SUNTV","SUNDARMFIN","SUNDRMFAST","SUNTECK","SUPRAJIT","SUPREMEIND","SUPPETRO","SUVENPHAR","SUZLON","SWANENERGY","SWARAJENG","SYMPHONY","SYNGENE","TCIEXP","TCNSBRANDS","TTKPRESTIG","TVTODAY","TV18BRDCST","TVSMOTOR","TASTYBITE","TATACHEM","TATACOFFEE","TATACOMM","TCS","TATACONSUM","TATAELXSI","TATAINVEST","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTLBSL","TATASTEEL","TEAMLEASE","TECHM","NIACL","RAMCOCEM","THERMAX","THYROCARE","TIMKEN","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TRIDENT","TIINDIA","UCOBANK","UFLEX","UPL","UJJIVAN","UJJIVANSFB","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VMART","VIPIND","VRLLOG","VSTIND","VAIBHAVGBL","VAKRANGEE","VTL","VARROC","VBL","VENKEYS","VINATIORGA","IDEA","VOLTAS","WABCOINDIA","WELCORP","WELSPUNIND","WESTLIFE","WHIRLPOOL","WIPRO","WOCKPHARMA","YESBANK","ZEEL","ZENSARTECH","ZYDUSWELL","ECLERX"]
price_list = []
stock_list = []


count = 1
for stock in NIFTY500:
    data = yf.download(stock+".NS",period="3d")
    if data is None:
        continue

    h1 = float(data.tail(1)["High"])
    l1 = float(data.tail(1)["Low"])
    h2 = float(data.tail(2).head(1)["High"])
    l2 = float(data.tail(2).head(1)["Low"])
   # o1 = float(data.tail(1)["Open"])
   # c1 = float(data.tail(1)["Close"])
   # o2 = float(data.tail(2).head(1)["Open"])
   # c2 = float(data.tail(2).head(1)["Close"])
    h3 = float(data.head(1)["High"])
   # c3 = float(data.head(1)["Close"])
   # o3 = float(data.head(1)["Open"])
    l3 = float(data.head(1)["Low"])

    if l1<l2 and l1<l3 and h1>h2 and h1>h3:
           stock_list.append(stock)
    print(stock)


    #print(stock)
    #o=float(data.tail(8).head(1)["Open"])
    #print(h)
    count=count+1
    print(count)
    #print(data)


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


print(stock_list)
