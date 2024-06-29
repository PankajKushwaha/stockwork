from kiteconnect import KiteConnect
import pickle
from set_token import *

def track_sl():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        print(dic['tradingsymbol'])
        print(dic['quantity'])
        print(dic['average_price'])

def get_sl():
    open_position_list = []
    pos = kite.positions()
    #print(pos)
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        print(dic['tradingsymbol'])
        q=dic['quantity']
        a=dic['average_price']
        print("target")
        s = ((q*a)+10000)/q
        print(round(s,3))
        print("stoploss")
        t = ((q*a)-10000)/q
        print(round(t,3))

def get_open_position_price_dic():
    open_position_list = []
    open_position_price_dic = {}
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        open_position_list.append("NFO:"+dic['tradingsymbol'])
    ltp_list=kite.ltp(open_position_list)
    #print(kite.ltp(open_position_list))
    for symbol in ltp_list:
        open_position_price_dic[symbol.replace("NFO:","")]=ltp_list[symbol]['last_price']
    
    return open_position_price_dic


kite=set_token()
get_sl()
#print(kite.ltp("NSE:ASIANPAINT"))
#print(kite.ohlc("NFO:ASIANPAINT22OCTFUT"))
#print(kite.ohlc("NSE:ASIANPAINT"))

#track_sl()

#print(get_open_position_price_dic())
