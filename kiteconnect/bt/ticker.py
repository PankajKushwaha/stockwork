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

   
def candle_close_near_low_20ma(start_date,end_date,timeframe):
    for symbol in NIFTYFNO:
        hist_df = pd.DataFrame(kite.historical_data(instrument_to_token[symbol], start_date, end_date, timeframe))
        ma20  = hist_df['close'].rolling(20).mean()
        ma200  = hist_df['close'].rolling(200).mean()
        hist_df['ma20']=ma20
        hist_df['ma200']=ma200
        for index, row in hist_df[210:-6].iterrows():
            c=row['close']
            o=row['open']
            l=row['low']
            h=row['high']
            ma20=row['ma20']
            ma200=row['ma200']
            hp1= hist_df.loc[index-1,'high']
            hp2= hist_df.loc[index-2,'high']
            hp3= hist_df.loc[index-3,'high']
            hp4= hist_df.loc[index-4,'high']
            hp5= hist_df.loc[index-5,'high']
            hp6= hist_df.loc[index-6,'high']
            hp7= hist_df.loc[index-7,'high']
            hp8= hist_df.loc[index-8,'high']
            hp9= hist_df.loc[index-9,'high']
            ma20p1= hist_df.loc[index-1,'ma20']
            ma20p2= hist_df.loc[index-2,'ma20']
            ma20p3= hist_df.loc[index-3,'ma20']
            ma20p4= hist_df.loc[index-4,'ma20']
            ma20p5= hist_df.loc[index-5,'ma20']
            ma20p6= hist_df.loc[index-6,'ma20']
            ma20p7= hist_df.loc[index-7,'ma20']
            ma20p8= hist_df.loc[index-8,'ma20']
            ma20p9= hist_df.loc[index-9,'ma20']
            hn1= hist_df.loc[index+1,'high']
            hn2= hist_df.loc[index+2,'high']
            hn3= hist_df.loc[index+3,'high']
            hn4= hist_df.loc[index+4,'high']
            hn5= hist_df.loc[index+5,'high']
            ln1= hist_df.loc[index+1,'low']
            ln2= hist_df.loc[index+2,'low']
            ln3= hist_df.loc[index+3,'low']
            ln4= hist_df.loc[index+4,'low']
            ln5= hist_df.loc[index+5,'low']
            ma20n1= hist_df.loc[index+1,'ma20']
            ma20n2= hist_df.loc[index+2,'ma20']
            ma20n3= hist_df.loc[index+3,'ma20']
            ma20n4= hist_df.loc[index+4,'ma20']
            ma20n5= hist_df.loc[index+5,'ma20']
            ma200n1= hist_df.loc[index+1,'ma200']
            ma200n2= hist_df.loc[index+2,'ma200']
            ma200n3= hist_df.loc[index+3,'ma200']
            ma200n4= hist_df.loc[index+4,'ma200']
            ma200n5= hist_df.loc[index+5,'ma200']
            if ( h>=ma20>l and 
                    hp1<ma20p1 and
                    hp2<ma20p2 and
                    hp3<ma20p3 and
                    hp4<ma20p4 and
                    hp5<ma20p5 and
                    hp6<ma20p6 and
                    hp7<ma20p7 and
                    hp8<ma20p8 and
                    hp9<ma20p9 and
                    h<=ma20+(ma20/10000) and
                    ma20>ma200-(ma200/200) and
                    ma20<ma200):
                print(symbol)
                print(row['date'])
                print(h)
                print(ma20)

            #if  ( c<(l+(h-l)/40) and h<(l+l/1000) and hist_df.loc[index+1,'high']>h and hist_df.loc[index+1,'open']<h
            #        and l<ma20<h and  hist_df.loc[index-1,'low']>hist_df.loc[index-1,'ma20'] ):

             #   print(symbol)
             #   print(row['date'])
            #if c<(l+(h-l)/40) and h>=ma20 and c<=ma20:
            #    print(symbol)
            #    print(row['date'])

start_date = '2024-01-20 09:00:00'
end_date = '2024-04-14 16:00:00'
timeframe='5minute'

candle_close_near_low_20ma(start_date,end_date,timeframe)
#save_screenshot(keys_with_least_values,"/home/pankaj/Pictures/")




