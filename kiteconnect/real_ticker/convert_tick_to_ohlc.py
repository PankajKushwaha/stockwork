import pandas as pd
from myLib import *

tick_file_name="tick.csv"
NIFTY_FNO=get_fno_list_new()
token_to_symbol=get_token_to_instrument(get_fno_list_new())

def remove_unnecessary_column():
    df = pd.read_csv(tick_file_name)
    df.drop(columns=['tradable','mode','last_quantity','average_price','volume','buy_quantity','sell_quantity','ohlc','change','oi','oi_day_high','oi_day_low', 'depth'], inplace=True)
    df.rename(columns={'instrument_token': 'instrument'}, inplace=True)
    df['instrument'] = df['instrument'].map(token_to_symbol)
    print(df)
    print(df.columns)
    return df

#def remove_unnecessary_time(df):
#    filtered_df = df[~df['timestamp'].apply(contains_substring)]
#    return filtered_df

def convert_to_5min_ohlc(symbol,df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print(symbol)
    filtered_df = df[df['instrument'] == symbol]
    #print(filtered_df)
    filtered_df = filtered_df.sort_values(by='timestamp')
    ohlc_df = filtered_df.resample('5T', on='timestamp').agg({
    'last_price': ['first', 'max', 'min', 'last']
}).reset_index()
    #ohlc_df["instrument"]=symbol
    ohlc_df.insert(0, "instrument", [symbol] * len(ohlc_df))
    ohlc_df = ohlc_df.reset_index(drop=True)
    #print(ohlc_df)
    ohlc_df.columns = ['instrument','timestamp','open','high','low','close']
    print(ohlc_df.columns)
    #print(ohlc_df)
    ohlc_df.to_csv("ohlc.csv",index=False)
    return ohlc_df

def is_20_200ma_support(df):
        last_row = df.tail(1)
        print(last_row)
        lrh=float(last_row["high"])
        print(lrh)
        print(type(lrh))
        lrl=float(last_row["low"])
        if lrh/lrl>=1.002:
            return
        lrma20=float(last_row["ma20"])
        lrma200=float(last_row["ma200"])

        '''
        if (lrma20-lrma20/10000)<=lrl<=(lrma20+lrma20/10000):
            print(lrl)
            print(lrma20)
            print(lrma200)
            return True
        if (lrma20-lrma20/10000)<=lrh<=(lrma20+lrma20/10000):
            print(lrh)
            print(lrma20)
            print(lrma200)
            return True
        '''
        if (lrma200-lrma200/10000)<=lrl<=(lrma200+lrma200/10000):
            print(lrl)
            print(lrma20)
            print(lrma200)
            return True
        if (lrma200-lrma200/10000)<=lrh<=(lrma200+lrma200/10000):
            print(lrh)
            print(lrma20)
            print(lrma200)
            return True
        return False

def ma20_breakout(df):
    last_15_rows = df.iloc[-15:]
    condition1 = all(last_15_rows.iloc[:14]['close'] < last_15_rows.iloc[:14]['ma20'])
    condition2 = last_15_rows.iloc[14]['close'] > last_15_rows.iloc[14]['ma20']
    if condition1 and condition2:
        return True
    else:
        return False

def scan():
    lst=[]
    df=remove_unnecessary_column()
    #df=remove_unnecessary_time(df)
    base_df=pd.read_csv("base_df.csv")
    for symbol in NIFTY_FNO:
        ohlc_df=convert_to_5min_ohlc(symbol,df)
        result_df=pd.concat([base_df, ohlc_df], axis=0)
        #print(result_df)
        filtered_df = result_df[result_df['instrument'] == symbol]
        #filtered_df = filtered_df.sort_values(by='timestamp')
        mav20  = filtered_df['close'].rolling( 20).mean()
        mav200 = filtered_df['close'].rolling(200).mean()
        filtered_df['ma20']=mav20
        filtered_df['ma200']=mav200
        print(filtered_df)
        print(symbol)
        if is_20_200ma_support(filtered_df) == True:
            lst.append(symbol)
        if ma20_breakout(filtered_df) == True:
            lst.append(symbol)
        
    print(lst)
    save_screenshot(list(lst))
scan()
#convert_to_5min_ohlc("NSE:NTPC")



