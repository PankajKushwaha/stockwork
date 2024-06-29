from pynse import *
import datetime
import pause
import logging

nse = Nse()

NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ_AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CAIRN","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M_M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]

NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M_M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL_N","WIPRO"]



p = nse.bhavcopy_fno(datetime.date(2021,6,28))
print(p)
