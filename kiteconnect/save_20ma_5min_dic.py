from kiteconnect import KiteConnect
from set_token import *
import pickle
import time
from operator import itemgetter

kite=set_token()

fail_count = 0
pass_count = 0
token_to_symbol = {}
ma20_dict={}

def save_to_file(name,filename):
    with open(filename, 'wb') as handle:
        pickle.dump(name, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_list_from_file(filename):
    with open(filename, 'rb') as handle:
        lst = pickle.load(handle)
        return lst


def get_token_list(symbol_list):
    token_list = []
    new_symbol_list = ["NFO:" + x for x in symbol_list]
    ohlc = kite.ohlc(new_symbol_list)
    for symbol in new_symbol_list:
        instrument_token = ohlc[symbol]["instrument_token"]
        token_to_symbol[instrument_token] = symbol
        token_list.append(instrument_token)
    return token_list

def check_stratagy(hist_candles,token):
    #print(hist_candles)
    close_list = []
    low_list = []
    high_list = []
    base_price = 0
    flag = False
    open_price = 0
    global fail_count
    global pass_count
    for idx,single_candle in enumerate(hist_candles):
        if single_candle["close"] < 10:
            break
        high_list.append(single_candle["high"])
        #if idx<1:
        #    continue
        if flag == False:
            open_price = single_candle["open"]
            close_price = single_candle["close"]
            high_price = single_candle["high"]
            high_list.append(single_candle["high"])
            low_price = single_candle["low"]
            if (close_price%10)<9  and close_price ==  high_price and close_price > open_price and open_price > (low_price+((high_price-low_price)/2)):
                print("same=============")
                flag = True
                print("entering trade")
                base_price=single_candle["close"]
                print(single_candle)
                continue
            else:
                break
        if flag == False:
            if idx>10:
                break
            #if single_candle["close"]>yh and single_candle["close"] > high_price:
            if single_candle["close"] == low_price and single_candle["close"]<single_candle["open"]:
                print("entering trade")
                flag=True
                base_price=single_candle["close"]
                print(single_candle)
                continue
        if flag == True:
            if single_candle["low"] < (base_price - (base_price/10)):
                fail_count = fail_count + 1
                print("###############")
                print("exiting trade fail")
                print(single_candle)
                break
            if single_candle["high"] > (base_price +((base_price/10)*3)):
                pass_count =  pass_count + 1
                print("###############")
                print("exiting trade pass")
                print(single_candle)
                break

def get_20ma(candle):
    ma20=sum(item['close'] for item in candle[-20:])/20
    #ma40=sum(item['close'] for item in candle[-40:])/40
    #ma200=sum(item['close'] for item in candle[-200:])/200
    return ma20
    #ma40=sum(candle["close"][-40:])/40
    #ma200=sum(candle["close"][-200:])/200
    #print(ma20)
    avg_ma=sorted([ma20,ma40,ma200])
    if ma20==ma40 or ma40==ma200:
        return 100
    try:
        avg1 = (avg_ma[1]-avg_ma[0])/avg_ma[0]
        avg2 = (avg_ma[2]-avg_ma[1])/avg_ma[1]
    except:
        return 100
    return ma20

def main_function():
    symbol_list = load_list_from_file("bull_option_list.pkl") + load_list_from_file("bear_option_list.pkl") 
    token_list = get_token_list(symbol_list)
    from_date = "2021-11-26 00:00:00"
    to_date = "2021-11-26 23:59:59"
    yesterday_from_date = "2021-11-24 00:00:00"
    yesterday_to_date = "2021-11-25 23:59:59"
    last_list=[]
    #hist_candles = kite.historical_data(21126658, from_date, to_date, "hour", continuous=False, oi=False)
    for token in token_list:
        print(token_to_symbol[token])
        '''
        yesterday_hist_candles = kite.historical_data(token, yesterday_from_date, yesterday_to_date, "day", continuous=False, oi=False)
        for single_candle in yesterday_hist_candles:
            h = hist_candle["high"]
            c = hist_candle["close"]
            o = hist_candle["open"]
            l = hist_candle["low"]
        '''
        hist_candles_today = kite.historical_data(token, from_date, to_date, "5minute", continuous=False, oi=False)
        #print(hist_candles_today[0])
        hist_candles_yesterday = kite.historical_data(token, yesterday_from_date, yesterday_to_date, "5minute", continuous=False, oi=False)
        ma20=get_20ma(hist_candles_today)
        print(ma20)
        ma20_dict[token_to_symbol[token]]=ma20
        #ma_dict[token_to_symbol[token]]=avg
        #print(hist_candles_yesterday[0])
        #t=hist_candles_today[0]
        #print(t)
        #if t["close"]==t["high"] and t["close"]>ma20 and t["volume"]>10000 and t["close"]<ma20+((ma20/10)*3):
        #print(hist_candles_today)
        '''
        t=hist_candles_today[0]
        y=hist_candles_yesterday[0]
        if t["close"] > t["open"] and (t["close"]-t["open"])/(t["high"]-t["low"]) >0.8 and t["close"]>ma20 and t["open"]>=(ma20) and t["open"]<ma20+(ma20/20):
            print(token_to_symbol[token])
            print(ma20)
            last_list.append(token_to_symbol[token])
    print(last_list)
    '''
    print(ma20_dict)
    save_to_file(ma20_dict,"ma20.pkl")

main_function()
#historical_data(	self, instrument_token, from_date, to_date, interval, continuous=False, oi=False)
#hist_day_candles = kite.historical_data(21126658, "2021-11-11 00:00:00", "2021-11-19 23:59:59", "minute", continuous=False, oi=False)
#print(hist_day_candles)
#print(kite.ohlc(["NFO:HEROMOTOCO21NOV2700PE"]))

