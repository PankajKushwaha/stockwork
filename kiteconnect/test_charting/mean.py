import mplfinance as mpf
import pandas as pd

# Sample financial data (OHLC)
data = pd.read_csv('Acc.csv', index_col=0, parse_dates=True)

# Calculate rolling mean
rolling_mean = data['Close'].rolling(window=20).mean()

# Plotting rolling mean only
mpf.plot(rolling_mean, type='line')

