from kiteconnect import KiteConnect
from set_token import *
import pickle

kite=set_token()
print(kite.ltp("NSE:ASIANPAINT"))

def load_from_file(filename):
    with open(filename, 'rb') as handle:
        obj = pickle.load(handle)
        return obj 

fnolist = load_from_file("bull_option_list.pkl") + load_from_file("bear_option_list.pkl")

def save_dict_to_file(discname,filename):
    with open(filename, 'wb') as handle:
        pickle.dump(discname, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_yesterday_ohlc(fnolist):
    fnolistnse = []
    for i in fnolist:
        tmp_symbol="NFO:"+i
        fnolistnse.append(tmp_symbol)
    ohlc_dict=kite.ohlc(fnolistnse)
    print(ohlc_dict)
    save_dict_to_file(ohlc_dict,"yesterday_ohlc_dict.pkl")

def kite_get_yesterday_ohlc(symbol):
    #symbol="NSE:"+symbol
    o=yesterday_ohlc_dict[symbol]["ohlc"]["open"]
    h=yesterday_ohlc_dict[symbol]["ohlc"]["high"]
    l=yesterday_ohlc_dict[symbol]["ohlc"]["low"]
    c=yesterday_ohlc_dict[symbol]["last_price"]

    return o,h,l,c


print(fnolist)
save_yesterday_ohlc(fnolist)
yesterday_ohlc_dict=load_from_file("yesterday_ohlc_dict.pkl")
for symbol in fnolist:
    o,h,l,c = kite_get_yesterday_ohlc("NFO:"+symbol)
    print(symbol)
    print(o)
    print(h)
    print(l)
    print(c)
#print(list_of_open_postion())
#print(kite_get_ohlc(ohlc_dict,"HCLTECH"))


