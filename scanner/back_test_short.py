# Import date and timdelta class
# from datetime module
from datetime import date
from datetime import timedelta
from nsepy import get_history
import time
import sys
import pandas as pd

margin = 0.05

NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M_M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL_N","WIPRO"]

df = pd.read_csv('monthly_pivot_nifty500.csv')

def percent_by_margin(price):
    i = price + (price*margin)
    i=round(i,2)
    print("margin is")
    print(i)
    return i

def fix_precesion(price):
    return round ( int(price*1000) / 1000 , 2 )
# Get today's date
today = date.today()
print("Today is: ", today)
  
# Yesterday date
day_ago_20 = today - timedelta(days = 35)
day_ago_40 = today - timedelta(days = 70)
day_ago_200 = today - timedelta(days = 300)
day_ago_2 = today - timedelta(days = 6)



for ind in df.index:
    data2 = get_history(symbol=df['symbol'][ind], start=day_ago_2, end=today)
    data2.index.name=None

    #print("ma20")
    #print(ma20)
    if len(data2[-2:]["Close"].value_counts()) is 0:
        continue


    day_before_yesterday_open = float(data2[-2:-1]["Open"])
    day_before_yesterday_close = float(data2[-2:-1]["Close"])
    yesterday_open = float(data2[-3:-2]["Open"])
    yesterday_close = float(data2[-3:-2]["Close"])

    R1 = df['R1'][ind]
    R2 = df['R2'][ind]
    
    #if float(data2[-2:-1]["High"]) > R1 and day_before_yesterday_open < R1 and day_before_yesterday_close < R1:
    if  yesterday_open < R1 and yesterday_open > (R1- R1*0.01) :
            print(df['symbol'][ind])
            #print("day_before_yesterday_open")
            #print(day_before_yesterday_open)
            #print("day_before_yesterday_close")
            #print(day_before_yesterday_close)
    time.sleep(0.2)

