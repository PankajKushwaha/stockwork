from datetime import date, timedelta
from nsepython import *
from pynse import *
import pandas as pd
import time
import os


nse = Nse()

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

def get_call_put_option(symbol,expiry_date,expiry_month,current_year):
    #get_call_put_option(stock,"25-Jan-2023","DEC","22")
    #print(expiry_date)
    sp_call = get_strike_price_call(symbol,expiry_date)
    sp_put = get_strike_price_put(symbol,expiry_date)
    #print(symbol+current_year+expiry_month+str(sp_call)+"CE")
    #print(symbol+current_year+expiry_month+str(sp_put)+"PE")
    call_symbol=symbol+current_year+expiry_month+str(sp_call)+"CE"
    put_symbol=symbol+current_year+expiry_month+str(sp_put)+"PE"
    return call_symbol,put_symbol,sp_call,sp_put

call_symbol,put_symbol,call_strike,put_strike=get_call_put_option(sys.argv[1],"23-Feb-2023","FEB","23")

print(call_symbol)
print(call_strike)
print(put_symbol)
print(put_strike)
