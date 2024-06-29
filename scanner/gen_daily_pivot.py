from nsetools import Nse
import pandas as pd

nse = Nse()


MY_NIFTY = ["WIPRO","LT","HCLTECH"]

NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M_M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL_N","WIPRO"]


def fix_precesion(num):
    return round ( int(num*1000)/1000, 2)


pivot_list = []

for stock in NIFTY100:
    print(stock)
    close = nse.get_quote(stock)
    if close is None:
        continue
    close = close['lastPrice']
    high = nse.get_quote(stock)['dayHigh']
    low = nse.get_quote(stock)['dayLow']

    center_pivot = fix_precesion((high+low+close)/3)
    bottom_cpr = fix_precesion((high+low)/2)
    top_cpr = fix_precesion((center_pivot - bottom_cpr) + center_pivot)

    tmp = min(top_cpr,bottom_cpr)
    top_cpr = max(top_cpr,bottom_cpr)
    bottom_cpr = tmp

    S1 =  fix_precesion((2 * center_pivot) - high)
    S2 =  fix_precesion(center_pivot - (high - low))
    R1 =  fix_precesion((2 * center_pivot) - low)
    R2 =  fix_precesion(center_pivot + (high - low))
    pivot_list.append([stock,R2,R1,top_cpr,center_pivot,bottom_cpr,R1,R2])

pivot_df = pd.DataFrame(pivot_list, columns = ['symbol','R2','R1','top_cpr','center_pivot','bottom_cpr','S1','S2'])

#print(pivot_list)
print (pivot_df)

pivot_df.to_csv('daily_pivot.csv')

