from myLib import *
import os
import sys
import time

#python3 buyatprice.py itc:300,balramchin:400

symbols=sys.argv[1].split(",")
print(symbols)
while True:
    for symbol in symbols:
        symbol=symbol.split(":")
        price=float(symbol[1])
        symbol=symbol[0]
        print(symbol)
        print(price)
        ltp_dic=get_ltp_dict()
        symbol=symbol.upper()
        o,h,l,c=get_current_ohlc_min5(symbol)
        ltp=ltp_dic["NSE:"+symbol]
        if ltp>=price and l<price:
            os.system("python3 buy_future.py "+symbol.lower())
            print("buy symbol")
            exit()
        print(l)
    time.sleep(2)
