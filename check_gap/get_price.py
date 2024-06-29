from yahoo_fin import stock_info as si
import yfinance as yf

symbol = "ltts"

print(si.get_live_price(symbol+".ns"))

data = yf.download(symbol+".NS",)

print(data)


