from myLib import *


def add_to_alert_given(symbol):
    with open('alert_given.txt', 'a') as file:
        file.write(symbol+"\n")

def is_stock_bw_200ma_day():
    symbols=get_symbols_from_file("stock_bw_day_200ma.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)
    for symbol in symbols:
        sma200 = get_200ma_day(symbol)
        o,h,l,c = get_current_ohlc_day(symbol)
        if l<=sma200<=h and symbol not in symbols_alert:
            tmpstr = symbol + " between daily 200ma "
            print(tmpstr)
            os.system('spd-say "symbol between daily 200 ma"')
            add_to_alert_given(symbol)

def is_stock_bw_20ma_day():
    symbols=get_symbols_from_file("stock_bw_day_20ma.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)
    for symbol in symbols:
        sma20 = get_20ma_day(symbol)
        o,h,l,c = get_current_ohlc_day(symbol)
        if l<=sma20<=h and symbol not in symbols_alert:
            tmpstr = symbol + " between daily 20ma "
            print(tmpstr)
            os.system('spd-say "symbol between daily 20 ma"')
            add_to_alert_given(symbol)

def high_greater_than_price():
    symbols=get_symbols_from_file("high_greater_than_price.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)
    for symbolprice in symbols:
        symbol=symbolprice.split(",")[0]
        price=symbolprice.split(",")[1]
        print(symbol)
        print(price)
        o,h,l,c = get_current_ohlc_day(symbol)
        if h>float(price) and symbol not in symbols_alert:
            tmpstr = symbol + " high greater than price "
            print(tmpstr)
            os.system('spd-say "high greater than price"')
            add_to_alert_given(symbol)

def low_less_than_price():
    symbols=get_symbols_from_file("low_less_than_price.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)
    for symbolprice in symbols:
        symbol=symbolprice.split(",")[0]
        price=symbolprice.split(",")[1]
        print(symbol)
        print(price)
        o,h,l,c = get_current_ohlc_day(symbol)
        if l<float(price) and symbol not in symbols_alert:
            tmpstr = symbol + " low less than than price "
            print(tmpstr)
            os.system('spd-say "low less than price"')
            add_to_alert_given(symbol)

def is_ltp_bw_200ma_min5():
    symbols=get_symbols_from_file("ma200_stocks.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)

    for symbol in symbols:
        sma200 = get_200ma_5minute(symbol)
        o,h,l,c = get_current_ohlc_min5(symbol)
        if l<=sma200<=h and symbol not in symbols_alert:
            tmpstr = symbol + " betweel 5minute 200ma "
            print(tmpstr)
            os.system('spd-say "symbol between five mintue 200 ma"')
            add_to_alert_given(symbol)

def is_ltp_bw_20ma_min5():
    symbols=get_symbols_from_file("ma20_stocks.txt")
    symbols_alert=get_symbols_from_file("alert_given.txt")
    print(symbols)

    for symbol in symbols:
        sma20 = get_20ma_5minute(symbol)
        o,h,l,c = get_current_ohlc_min5(symbol)
        if l<=sma20<=h and symbol not in symbols_alert:
            tmpstr = symbol + " betweel 5minute 20ma "
            print(tmpstr)
            os.system('spd-say "symbol between five mintue 20 ma"')
            add_to_alert_given(symbol)

def alerts():
    is_ltp_bw_200ma_min5()
    is_ltp_bw_20ma_min5()
    #is_stock_bw_20ma_day()
    #is_stock_bw_200ma_day()
    #high_greater_than_price()
    #low_less_than_price()

def main():
    while ( True ):
        alerts()
        time.sleep(60)

main()

