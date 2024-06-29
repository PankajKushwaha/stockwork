import pyautogui
import time
from nsepython import *

sample_list = ["WIPRO","TCS","TECHM"]

NIFTY100=["ACC","ABBOTINDIA","ADANIGREEN","ADANIPORTS","ADANITRANS","ALKEM","AMBUJACEM","ASIANPAINT","AUROPHARMA","DMART","AXISBANK","BAJAJ_AUTO","BAJFINANCE","BAJAJFINSV","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BERGEPAINT","BPCL","BHARTIARTL","BIOCON","BOSCHLTD","BRITANNIA","CADILAHC","CIPLA","COALINDIA","COLPAL","CONCOR","DLF","DABUR","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GICRE","GODREJCP","GRASIM","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HAVELLS","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HDFC","ICICIBANK","ICICIGI","ICICIPRULI","ITC","IOC","IGL","INDUSTOWER","INDUSINDBK","NAUKRI","INFY","INDIGO","JSWSTEEL","KOTAKBANK","LTI","LT","LUPIN","M_M","MARICO","MARUTI","MOTHERSUMI","MUTHOOTFIN","NMDC","NTPC","NESTLEIND","ONGC","OFSS","PETRONET","PIDILITIND","PEL","PFC","POWERGRID","PGHH","PNB","RELIANCE","SBICARD","SBILIFE","SHREECEM","SIEMENS","SBIN","SUNPHARMA","TCS","TATACONSUM","TATAMOTORS","TATASTEEL","TECHM","TITAN","TORNTPHARM","UPL","ULTRACEMCO","UBL","MCDOWELL_N","WIPRO"]

#fno_list = ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BIOCON', 'BRITANNIA', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'BANKBARODA', 'CANBK', 'COFORGE', 'COLPAL', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'LTTS', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'SHREECEM', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'GUJGASLTD', 'MARICO', 'LICHSGFIN', 'NATIONALUM', 'MUTHOOTFIN', 'NMDC', 'RAMCOCEM', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'TORNTPHARM', 'TVSMOTOR', 'BOSCHLTD', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI', 'ZEEL', 'PEL', 'PNB', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'TORNTPOWER', 'VEDL', 'GMRINFRA', 'PFC', 'VOLTAS', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']
#fno_list = sorted(fno_list)
#print(len(fno_list))

def get_fno_list():
    lst=fnolist()
    lst.remove("NIFTYIT")
    lst.remove("NIFTY")
    lst.remove("BANKNIFTY")
    lst.remove("IDEA")
    lst.remove("MCX")
    print(lst)
    return lst

fno_list=get_fno_list()

def click_wl():
    pyautogui.click(140, 182)

def erase():
    pyautogui.moveTo(140, 182)
    pyautogui.doubleClick()


def search_stock(stock):
    pyautogui.write(stock)

def click_plus():
    pyautogui.moveTo(431,229)
    time.sleep(1)
    pyautogui.click()

def add_one_stock(stock):
    pyautogui.click(140, 182)
    pyautogui.doubleClick()
    pyautogui.write(stock)
    pyautogui.moveTo(453,236)
    time.sleep(0.5)
    pyautogui.click()

def add_stock(lst):
    for stock in lst:
        add_one_stock(stock)


add_stock(NIFTY100[:10])
'''
for stock in sample_list:
    click_wl()
    erase()
    time.sleep(1)
    search_stock(stock)
    time.sleep(1)
    click_plus()
'''