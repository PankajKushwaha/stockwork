from nsetools import Nse
import pandas as pd
import time

nse = Nse()

percent_margin = 0.001

def less_by_margin(level):
    return (level - (level*percent_margin))

def more_by_margin(level):
    return (level + (level*percent_margin))

df = pd.read_csv('./data/daily_pivot_nifty100.csv')

for ind in df.index:
    try:
        price = nse.get_quote(df['symbol'][ind])['lastPrice']
    except:
        pass

    if price is None:
        continue

    R2 = df['R2'][ind]
    if price > less_by_margin(R2) and price < more_by_margin(R2):
        print(df['symbol'][ind])
        continue
    
    R1 = df['R1'][ind]
    if price > less_by_margin(R1) and price < more_by_margin(R1):
        print(df['symbol'][ind])
        continue

    top_cpr = df['top_cpr'][ind]
    if price < more_by_margin(top_cpr) and price > top_cpr:
        print(df['symbol'][ind])
        continue

    bottom_cpr = df['bottom_cpr'][ind]
    if price > less_by_margin(bottom_cpr) and price < bottom_cpr:
        print(df['symbol'][ind])
        continue

    S2 = df['S2'][ind]
    if price > less_by_margin(S2) and price < more_by_margin(S2):
        print(df['symbol'][ind])
        continue

    S1 = df['R2'][ind]
    if price > less_by_margin(S1) and price < more_by_margin(S1):
        print(df['symbol'][ind])
        continue



