from myLib import *
import sys

symbols=sys.argv[1].split(",")
print(symbols)

for symbol in symbols:
    ltp_dic=get_ltp_dict()
    symbol=symbol.upper()
    ma20=get_20ma_5minute(symbol)
    o,h,l,c=get_current_ohlc_min5(symbol)
    print(symbol)
    print(ma20)
    print(ltp_dic["NSE:"+symbol])
    print(get_current_ohlc_min5(symbol))
    if l<=ma20 and c>o:
        print("buy symbol")
