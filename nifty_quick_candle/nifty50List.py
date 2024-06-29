import pandas as pd
import pickle

def get_nifty50_lst():
    URL = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
    df = pd.read_csv(URL)
    dflst = df.Symbol.tolist()
    dflst.insert(0, "BANKNIFTY")
    dflst.insert(0, "NIFTY")
    print(dflst)
    return dflst

s=get_nifty50_lst()
sn=[]

for i in s:
    s.append('NSE:'+i)
