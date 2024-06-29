import yfinance as yf
import yahoo_fin.options as ops

expiration_dates = ops.get_expiration_dates("nifty.ns")

hcltech = yf.Ticker("wipro")

print(hcltech.option_chain('2021-06-28'))
