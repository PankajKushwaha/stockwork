import pandas as pd
from kiteconnect import KiteConnect
import matplotlib.pyplot as plt
import mplfinance as mpf
from set_token import *
import sys
import time
import numpy as np
from myLib import *
from datetime import datetime

NIFTYFNO=get_fno_list_with_nse()
instrument_to_token = get_instrument_to_token(NIFTYFNO)
token_to_instrument = get_token_to_instrument(NIFTYFNO)
old_minute = 0
op = {key: [] for key in NIFTYFNO}
hp = {key: [] for key in NIFTYFNO}
lp = {key: [] for key in NIFTYFNO}
cp = {key: [] for key in NIFTYFNO}
ma20 = {key: [] for key in NIFTYFNO}


def min_ohlc():
    is20Complete = 0
    wait_for_1min()
    ltpdic=get_ltp_dict()
    df = pd.DataFrame([ltpdic])
    ohlc_df = pd.DataFrame()
    cm=get_current_minute()
    while True:
        nm=get_current_minute()
        if nm!=cm:
            ohlc_lst = []
            for column_name in df.columns:
                column_values = df[column_name]
                print(column_name)
                print(column_values.tolist())
                lst=column_values.tolist()
                o=lst[0]
                h=max(lst)
                l=min(lst)
                c=lst[-1]
                ohlc_lst.append((o,h,l,c))
                #op[column_name].append(lst[0])
                #hp[column_name].append(max(lst))
                #lp[column_name].append(min(lst))
                #cp[column_name].append(lst[-1])
            print(cp)
            cm=nm
            df = df.drop(df.index)
        time.sleep(0.5)
        ltpdic=get_ltp_dict()
        new_df = pd.DataFrame([ltpdic])
        df = pd.concat([df, new_df], ignore_index=True)
        print(df)
    
min_ohlc()

