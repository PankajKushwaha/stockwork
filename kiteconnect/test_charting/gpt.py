import pandas as pd
from kiteconnect import KiteConnect
import matplotlib.pyplot as plt
import mplfinance as mpf
from set_token import *


instrument_token = '408065'  # Example: Infosys instrument token
from_date = '2024-01-01'
to_date = '2024-03-31'
interval = '5minute'  

historical_data = kite.historical_data(instrument_token, from_date, to_date, interval)
df = pd.DataFrame(historical_data)
df.set_index('date', inplace=True)
mpf.plot(df, type='candle', volume=True, title='Infosys Stock Chart')
plt.show()

