import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime

conn = sqlite3.connect("stock.db")
cursor = conn.cursor()
disk_engine = create_engine('sqlite:///stock.db')

NIFTY200=["ACC","AUBANK","AARTIIND","ABBOTINDIA","ADANIENT","ADANIGREEN","ADANIPORTS","ATGL","ADANITRANS","ABCAPITAL","ABFRL","AJANTPHARM","APLLTD","ALKEM","AMARAJABAT","AMBUJACEM","APOLLOHOSP","APOLLOTYRE","ASHOKLEY","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BALKRISIND","BANDHANBNK","BANKBARODA","BANKINDIA","BATAINDIA","BERGEPAINT","BEL","BHARATFORG","BHEL","BPCL","BHARTIARTL","BIOCON","BBTC","BOSCHLTD","BRITANNIA","CESC","CADILAHC","CANBK","CASTROLIND","CHOLAFIN","CIPLA","CUB","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL","CROMPTON","CUMMINSIND","DLF","DABUR","DALBHARAT","DEEPAKNTR","DHANI","DIVISLAB","DIXON","LALPATHLAB","DRREDDY","EICHERMOT","EMAMILTD","ENDURANCE","ESCORTS","EXIDEIND","FEDERALBNK","FORTIS","GAIL","GMRINFRA","GLENMARK","GODREJAGRO","GODREJCP","GODREJIND","GODREJPROP","GRASIM","GUJGASLTD","GSPL","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HAL","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ISEC","IDFCFIRSTB","ITC","IBULHSGFIN","INDIAMART","INDHOTEL","IOC","IRCTC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","IPCALAB","JSWENERGY","JSWSTEEL","JINDALSTEL","JUBLFOOD","KOTAKBANK","L&TFH","LTTS","LICHSGFIN","LTI","LT","LAURUSLABS","LUPIN","MRF","MGL","M&MFIN","M&M","MANAPPURAM","MARICO","MARUTI","MFSL","MINDTREE","MOTHERSUMI","MPHASIS","MUTHOOTFIN","NATCOPHARM","NMDC","NTPC","NAVINFLUOR","NESTLEIND","NAM-INDIA","OBEROIRLTY","ONGC","OIL","PIIND","PAGEIND","PETRONET","PFIZER","PIDILITIND","PEL","POLYCAB","PFC","POWERGRID","PRESTIGE","PGHH","PNB","RBLBANK","RECLTD","RELIANCE","SBICARD","SBILIFE","SRF","SANOFI","SHREECEM","SRTRANSFIN","SIEMENS","SBIN","SAIL","SUNPHARMA","SUNTV","SYNGENE","TVSMOTOR","TATACHEM","TCS","TATACONSUM","TATAELXSI","TATAMOTORS","TATAPOWER","TATASTEEL","TECHM","RAMCOCEM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","UPL","ULTRACEMCO","UNIONBANK","UBL","MCDOWELL-N","VGUARD","VBL","VEDL","IDEA","VOLTAS","WHIRLPOOL","WIPRO","YESBANK","ZEEL"]

stock_list = []

for stock in NIFTY200:
    print(stock)
    if stock == "BAJAJ-AUTO":
        stock="BAJAJAUTO"
    if stock == "M&MFIN":
        stock="MMFIN"
    if stock == "L&TFH":
        stock="LTFH"
    if stock == "M&M":
        stock="MM"
    if stock == "M&M":
        stock="MM"
    if stock == "NAM-INDIA":
        stock="NAMINDIA"
    if stock == "MCDOWELL-N":
        stock="MCDOWELLN"
    p2 = pd.read_sql('select * from '+stock ,  conn)
    p2 = p2.tail(3)
    plst = p2["Low"].tolist()
    if plst[0] < plst[1] < plst[2]:
        r = (plst[2] - plst[1]) / (plst[1]-plst[0])
        if 0.6 < r < 1.4:
            stock_list.append(stock)

print(stock_list)
    #print(data)
"""
for stock in NIFTY5:
#    date_today = "'"+str(datetime.date(datetime.now()))+"'"
#    p2 = pd.read_sql('select * from '+stock+ ' where `index` =' + date_today ,  conn)
    p2 = pd.read_sql('select * from '+stock ,  conn)
    print(p2)
    time.sleep(0.5)
    """
