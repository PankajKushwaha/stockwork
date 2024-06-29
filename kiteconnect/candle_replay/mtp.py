import matplotlib.pyplot as plt
from kiteconnect import KiteConnect
import mplfinance as mpf
import pandas as pd
from set_token import *


# Define the instrument token for the symbol you want to plot
instrument_token = 3329  # Replace with the actual instrument token

# Fetch historical data using Kite Connect
historical_data = kite.historical_data(
    instrument_token,
    from_date='2023-01-01',
    to_date='2023-01-10',
    interval='day',  # Use 'minute' for intraday data
    continuous=False,
)

# Convert historical data to a DataFrame
df = pd.DataFrame(historical_data)
df.set_index('timestamp', inplace=True)

# Plot candlestick chart using Matplotlib
mpf.plot(df, type='candle', style='yahoo', title='Candlestick Chart', ylabel='Price', figsize=(10, 6))

# Show the chart
plt.show()

