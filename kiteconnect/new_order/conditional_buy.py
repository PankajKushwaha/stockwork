from myLib import *
import time
import pandas as pd

print(get_ohlc_dict())
print(get_ltp_dict())
ohlc=get_ohlc_dict()
ltp=get_ltp_dict()

lot=get_lot_size()
print(lot)
df=pd.read_csv("order.csv")
#print(df)
print(lot)

for index, row in df.iterrows():
#    print("Row index:", index)
#    print("Values:", row)
    symbol=row["symbol"] 
    symbol="NSE:"+symbol.upper()
    print(symbol)
    if row["condition1"] == "<":
        if row["price1"]=="ma20":
            price1=get_20ma_day(symbol[4:])
        elif row["price1"]=="ma200":
            price1=get_200ma_day(symbol[4:])
        else:
            price1=row["price1"]
        print(price1)        
        if ohlc[symbol][row["ohlc"]]<price1:
            print("again passing")
            if row["condition2"] == ">":
                if ltp[symbol] > row["price2"]:
                    if row["order_type"] == "b":
                        print("again again passing")
                        buy_fno_symbol(symbol)
                        break

    if row["condition1"] == ">":
        if ohlc[symbol][row["ohlc"]]>row["price1"]:
            print("again passing")

print(get_fno_symbol("NSE:ITC"))
'''
while True:
    ohlc=get_ohlc_dict()
    ltp=get_ltp_dict()
    symbol="itc"
    symbol="NSE:"+symbol.upper()
    print(ohlc[symbol]["low"])
    print(ltp[symbol])

    time.sleep(4)
'''
