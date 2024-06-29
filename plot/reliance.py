import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = "RELIANCE.NS"  # RELIANCE stock on the National Stock Exchange of India (NSE)
start_date = "2022-01-01"
end_date = "2022-12-31"

# Fetch historical stock data using yfinance
reliance_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Display the historical data
print(reliance_data.head())

