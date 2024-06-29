from datetime import date, timedelta
from nsepython import *
from pynse import *
import pandas as pd
import time
import os

#fnolist =  ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'stock', 'BHARATFORG', 'BHEL', 'stock', 'stock', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'stock', 'CANBK', 'COFORGE', 'stock', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT',  'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'stock', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'stock', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'stock', 'SRTRANSFIN', 'SUNPHARMA', 'stock', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'stock', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'stock', 'MARICO', 'LICHSGFIN', 'stock', 'MUTHOOTFIN', 'NMDC', 'stock', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'stock', 'TVSMOTOR', 'stock', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI',  'PEL', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'stock', 'VEDL', 'GMRINFRA', 'stock', 'stock', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']
fnolist =  ['AUROPHARMA', 'AARTIIND','stock']

fnoStrikePriceDictPut = {}
fnoStrikePriceListPut = []
fnoStrikePriceDictCall = {}
fnoStrikePriceListCall = []

stock = sys.argv[1]

nse = Nse()
pd.set_option('display.max_columns', None)
oi_data, ltp, crontime = oi_chain_builder(stock,"23-Feb-2023","full")

#print(oi_data)
#print(oi_data.iloc[oi_data["PUTS_Chng in OI"].idxmax()]["Strike Price"])
#print(oi_data.iloc[oi_data["Strike Price"]%100 == 0 ]["Strike Price"])
#print(option_chain('PVR'))

def get_strike_price_put(symbol,expiry_date):
    #print(expiry_date)
    oi_data, ltp, crontime = oi_chain_builder(symbol,expiry_date,"full")
    a = int(oi_data.iloc[oi_data["PUTS_Volume"].idxmax()]["Strike Price"])
    #print(oi_data.iloc[oi_data["PUTS_Volume"]])
    #print(oi_data)
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,expiry_date,"full")
        a = int(oi_data.iloc[oi_data["PUTS_Volume"].idxmax()]["Strike Price"])
        v = int(oi_data.iloc[oi_data["PUTS_Volume"].idxmax()]["PUTS_Volume"])
        print(v)
        #print(oi_data.iloc[oi_data["PUTS_Volume"]])
        #print(oi_data)
    except:
        a=None
    return a

def get_strike_price_call(symbol,expiry_date):
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,expiry_date,"full")
        a = int(oi_data.iloc[oi_data["CALLS_Volume"].idxmax()]["Strike Price"])
        v = int(oi_data.iloc[oi_data["CALLS_Volume"].idxmax()]["CALLS_Volume"])
        print(v)
        #print(oi_data.iloc[oi_data["CALLS_Volume"].idxmax()])
        #print(oi_data)
    except:
        a=None
    return a
'''
for symbol in fnolist:
    print(symbol)
    sp = get_strike_price_put(symbol)
    if sp==None:
        continue
    fnoStrikePriceDictPut[symbol] = str(symbol)+"23DEC"+str(sp)+"PE"
    fnoStrikePriceListPut.append(str(symbol)+"22DEC"+str(sp)+"PE")
    print(fnoStrikePriceDictPut[symbol])

for symbol in fnolist:
    print(symbol)
    sp = get_strike_price_call(symbol)
    if sp==None:
        continue
    fnoStrikePriceDictCall[symbol] = str(symbol)+"22DEC"+str(sp)+"CE"
    fnoStrikePriceListCall.append(str(symbol)+"22DEC"+str(sp)+"CE")
    print(fnoStrikePriceDictCall[symbol])
'''
def get_call_put_option(symbol,expiry_date,expiry_month,current_year):
    #get_call_put_option(stock,"25-Jan-2023","DEC","22")
    #print(expiry_date)
    sp_call = get_strike_price_call(symbol,expiry_date)
    sp_put = get_strike_price_put(symbol,expiry_date)
    #print(symbol+current_year+expiry_month+str(sp_call)+"CE")
    #print(symbol+current_year+expiry_month+str(sp_put)+"PE")
    call_symbol=symbol+current_year+expiry_month+str(sp_call)+"CE"
    put_symbol=symbol+current_year+expiry_month+str(sp_put)+"PE"
    return call_symbol,put_symbol

call_symbol,put_symbol=get_call_put_option(stock,"23-Feb-2023","FEB","23")
print(call_symbol)
print(put_symbol)
def save_list_to_file(listname,filename):
    with open(filename, 'wb') as handle:
        pickle.dump(listname, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_list_from_file(filename):
    with open(filename, 'rb') as handle:
        lst = pickle.load(handle)
        return lst

#print(fnoStrikePriceDictPut)
#print(fnoStrikePriceListPut)
#print(fnoStrikePriceListCall)

os.remove("bull_option_list.pkl")
os.remove("bear_option_list.pkl")
save_list_to_file(fnoStrikePriceListPut,"bear_option_list.pkl")
save_list_to_file(fnoStrikePriceListCall,"bull_option_list.pkl")

#print(nse_get_fno_lot_sizes())
