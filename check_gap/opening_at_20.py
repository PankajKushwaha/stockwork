import yfinance as yf
import pandas as pd
from nsetools import Nse
from nsepy import get_history

nse = Nse()

margin = 0.001
NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ_AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CAIRN","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M_M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]

NIFTY500 = ["3MINDIA","ABB","POWERINDIA","ACC","AIAENG","APLAPOLLO","AUBANK","AARTIDRUGS","AARTIIND","AAVAS","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ATGL","ADANITRANS","ABCAPITAL","ABFRL","ADVENZYMES","AEGISCHEM","AFFLE","AJANTPHARM","AKZOINDIA","ALEMBICLTD","APLLTD","ALKEM","ALKYLAMINE","ALOKINDS","AMARAJABAT","AMBER","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASHOKA","ASIANPAINT","ASTERDM","ASTRAZEN","ASTRAL","ATUL","AUROPHARMA","AVANTIFEED","DMART","AXISBANK","BASF","BEML","BSE","BAJAJ-AUTO","BAJAJCON","BAJAJELEC","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BALMLAWRIE","BALRAMCHIN","BANDHANBNK","BANKBARODA","BANKINDIA","MAHABANK","BATAINDIA","BAYERCROP","BERGEPAINT","BDL","BEL","BHARATFORG","BHEL","BPCL","BHARATRAS","BHARTIARTL","BIOCON","BIRLACORPN","BSOFT","BLISSGVS","BLUEDART","BLUESTARCO","BBTC","BOMDYEING","BOSCHLTD","BRIGADE","BRITANNIA","CARERATING","CCL","CESC","CRISIL","CSBBANK","CADILAHC","CANFINHOME","CANBK","CAPLIPOINT","CGCL","CARBORUNIV","CASTROLIND","CEATLTD","CENTRALBK","CDSL","CENTURYPLY","CENTURYTEX","CERA","CHALET","CHAMBLFERT","CHENNPETRO","CHOLAHLDNG","CHOLAFIN","CIPLA","CUB","COALINDIA","COCHINSHIP","COFORGE","COLPAL","CONCOR","COROMANDEL","CREDITACC","CROMPTON","CUMMINSIND","CYIENT","DBCORP","DCBBANK","DCMSHRIRAM","DLF","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DHANI","DHANUKA","DBL","DISHTV","DCAL","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EIDPARRY","EIHOTEL","EPL","ESABINDIA","EDELWEISS","EICHERMOT","ELGIEQUIP","EMAMILTD","ENDURANCE","ENGINERSIN","EQUITAS","ERIS","ESCORTS","EXIDEIND","FDC","FEDERALBNK","FINEORG","FINCABLES","FINPIPE","FSL","FORTIS","FCONSUMER","FRETAIL","GAIL","GEPIL","GHCL","GMMPFAUDLR","GMRINFRA","GALAXYSURF","GRSE","GARFIBRES","GICRE","GILLETTE","GLAXO","GLENMARK","GODFRYPHLP","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRANULES","GRAPHITE","GRASIM","GESHIP","GREAVESCOT","GRINDWELL","GUJALKALI","GAEL","FLUOROCHEM","GUJGASLTD","GMDCLTD","GNFC","GPPL","GSFC","GSPL","GULFOILLUB","HEG","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HFCL","HATHWAY","HATSUN","HAVELLS","HEIDELBERG","HERITGFOOD","HEROMOTOCO","HSCL","HINDALCO","HAL","HINDCOPPER","HINDPETRO","HINDUNILVR","HINDZINC","HONAUT","HUDCO","HDFC","HUHTAMAKI","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","ICRA","IDBI","IDFCFIRSTB","IDFC","IFBIND","IIFL","IIFLWAM","IOLCP","IRB","IRCON","ITC","ITI","INDIACEM","IBULHSGFIN","IBREALEST","INDIAMART","INDIANB","IEX","INDHOTEL","IOC","IOB","IRCTC","INDOCO","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INGERRAND","INOXLEISUR","INDIGO","IPCALAB","JBCHEPHARM","JKCEMENT","JKLAKSHMI","JKPAPER","JKTYRE","JMFINANCIL","JSWENERGY","JSWSTEEL","JTEKTINDIA","JAGRAN","JAICORPLTD","J&KBANK","JAMNAAUTO","JINDALSAW","JSLHISAR","JSL","JINDALSTEL","JCHAC","JUBLFOOD","JUSTDIAL","JYOTHYLAB","KEI","KNRCON","KRBL","KSB","KAJARIACER","KALPATPOWR","KANSAINER","KTKBANK","KARURVYSYA","KSCL","KEC","KOLTEPATIL","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LAOPALA","LAXMIMACH","LTI","LT","LAURUSLABS","LEMONTREE","LINDEINDIA","LUPIN","LUXIND","MASFIN","MMTC","MOIL","MRF","MGL","MAHSCOOTER","MAHSEAMLES","M&MFIN","M&M","MAHINDCIE","MHRIL","MAHLOG","MANAPPURAM","MRPL","MARICO","MARUTI","MFSL","METROPOLIS","MINDTREE","MINDACORP","MINDAIND","MIDHANI","MOTHERSUMI","MOTILALOFS","MPHASIS","MCX","MUTHOOTFIN","NATCOPHARM","NBCC","NCC","NESCO","NHPC","NLCINDIA","NMDC","NOCIL","NTPC","NH","NATIONALUM","NFL","NAVINFLUOR","NAVNETEDUL","NESTLEIND","NETWORK18","NILKAMAL","NAM-INDIA","OBEROIRLTY","ONGC","OIL","OMAXE","OFSS","ORIENTCEM","ORIENTELEC","ORIENTREF","PIIND","PNBHOUSING","PNCINFRA","PSPPROJECT","PTC","PVR","PAGEIND","PERSISTENT","PETRONET","PFIZER","PHILIPCARB","PHOENIXLTD","PIDILITIND","PEL","POLYMED","POLYCAB","POLYPLEX","PFC","POWERGRID","PRAJIND","PRESTIGE","PRSMJOHNSN","PGHL","PGHH","PNB","QUESS","RBLBANK","RECLTD","RITES","RADICO","RVNL","RAIN","RAJESHEXPO","RALLIS","RCF","RATNAMANI","RAYMOND","REDINGTON","RELAXO","RELIANCE","SBICARD","SBILIFE","SIS","SJVN","SKFINDIA","SRF","SANOFI","SCHAEFFLER","SCHNEIDER","SEQUENT","SFL","SHILPAMED","SCI","SHOPERSTOP","SHREECEM","SHRIRAMCIT","SRTRANSFIN","SIEMENS","SOBHA","SOLARINDS","SOLARA","SONATSOFTW","SOUTHBANK","SPICEJET","STARCEMENT","SBIN","SAIL","SWSOLAR","STLTECH","STAR","SUDARSCHEM","SUMICHEM","SPARC","SUNPHARMA","SUNTV","SUNDARMFIN","SUNDRMFAST","SUNTECK","SUPRAJIT","SUPREMEIND","SUPPETRO","SUVENPHAR","SUZLON","SWANENERGY","SWARAJENG","SYMPHONY","SYNGENE","TCIEXP","TCNSBRANDS","TTKPRESTIG","TVTODAY","TV18BRDCST","TVSMOTOR","TASTYBITE","TATACHEM","TATACOFFEE","TATACOMM","TCS","TATACONSUM","TATAELXSI","TATAINVEST","TATAMTRDVR","TATAMOTORS","TATAPOWER","TATASTLBSL","TATASTEEL","TEAMLEASE","TECHM","NIACL","RAMCOCEM","THERMAX","THYROCARE","TIMKEN","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TRIDENT","TIINDIA","UCOBANK","UFLEX","UPL","UJJIVAN","UJJIVANSFB","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VMART","VIPIND","VRLLOG","VSTIND","VAIBHAVGBL","VAKRANGEE","VTL","VARROC","VBL","VENKEYS","VINATIORGA","IDEA","VOLTAS","WABCOINDIA","WELCORP","WELSPUNIND","WESTLIFE","WHIRLPOOL","WIPRO","WOCKPHARMA","YESBANK","ZEEL","ZENSARTECH","ZYDUSWELL","ECLERX"]

def get_20_ma(symbol):
    data = yf.download(symbol+".NS",period="21d",interval="1d")
   # ma20 = float(sum(data["Close"].head(20))/20)
   # open_today = float(data["Open"].tail(1))
    close_ago = float(data["Low"].tail(3).head(1))
    
    if close_ago < ma20 and open_today > ma20:
        print(symbol)


for symbol in NIFTY500:
    get_20_ma(symbol)




