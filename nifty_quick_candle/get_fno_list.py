from nsepython import *
import pandas as pd
import pickle

def get_niftyfno_list():
    fnolst=fnolist()
    fnolst.remove("NIFTYIT")
    fnolst.remove("BANKNIFTY")
    fnolst.remove("NIFTY")
    fnolst.sort()
    fnolst.insert(0, "BANKNIFTY")
    fnolst.insert(0, "NIFTY")
    print(fnolst)

def get_nifty50_lst():
    URL = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
    df = pd.read_csv(URL)
    dflst = df.Symbol.tolist()
    dflst.insert(0, "BANKNIFTY")
    dflst.insert(0, "NIFTY")
    print(dflst)

