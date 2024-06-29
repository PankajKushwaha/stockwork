import pandas as pd
from kiteconnect import KiteConnect
import matplotlib.pyplot as plt
import mplfinance as mpf
from set_token import *
import sys
import time
import numpy as np
from myLib import *

NIFTYFNO=get_fno_list_with_nse()
instrument_to_token = get_instrument_to_token(NIFTYFNO)
token_to_instrument = get_token_to_instrument(NIFTYFNO)


def get_stddev(symbol,start_date,end_date,timeframe,period,refrence_price):
    hist_df = pd.DataFrame(kite.historical_data(instrument_to_token[symbol], start_date, end_date, timeframe))
    ma20  = hist_df['close'].rolling( 20).mean()
    ma200 = hist_df['close'].rolling(200).mean()
    gap = [x - y for x, y in zip(ma200, ma20)]

    hist_df['ma20']=ma20
    hist_df['ma200']=ma200
    hist_df['gap']=gap
    #print(hist_df)

    if refrence_price == "high":
        highList = list(hist_df[0-period:]['high'])
        return np.std(highList)
    if refrence_price == "low":
        lowList = list(hist_df[0-period:]['low'])
        return np.std(lowList)
    if refrence_price == "close":
        closeList = list(hist_df[0-period:]['close'])
        return np.std(closeList)
    if refrence_price == "ma20":
        ma20List = list(hist_df[0-period:]['ma20'])
        return np.std(ma20List)
    if refrence_price == "ma200":
        ma200List = list(hist_df[0-period:]['ma200'])
        return np.std(ma20List)
    if refrence_price == "gap":
        gapList = list(hist_df[0-period:]['gap'])
        return np.std(gapList)

def get_stddev_dic(symbol_list,start_date,end_date,timeframe,period,refrence_price):
    stddev_dic={}
    for symbol in symbol_list:
        stddev_dic[symbol] = get_stddev(symbol,start_date,end_date,timeframe,period,refrence_price)
    return stddev_dic
    
start_date = '2024-03-20 09:00:00'
end_date = '2024-04-06 16:00:00'
timeframe='5minute'
period=15
refrence_price="gap"

my_dict=get_stddev_dic(NIFTYFNO,start_date,end_date,timeframe,period,refrence_price)

sorted_keys = sorted(my_dict, key=my_dict.get)

# Get the 10 keys with the least values
keys_with_least_values = sorted_keys[:20]

save_screenshot(keys_with_least_values,"/home/pankaj/Pictures/")

print(keys_with_least_values)



