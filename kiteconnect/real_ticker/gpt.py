import pandas as pd
df = pd.read_csv("output_tick.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.sort_values(by='timestamp')
ohlc_df = df.groupby('instrument_token').resample('5T', on='timestamp').agg({
    'last_price': ['first', 'max', 'min', 'last']
}).reset_index()
ohlc_df.columns = ['instrument_token', 'timestamp', 'open', 'high', 'low', 'close']
#starting_time = ohlc_df['timestamp'].iloc[0]
#print(starting_time)
# Delete rows starting from the first timestamp
#ohlc_df = ohlc_df[ohlc_df['timestamp'] > starting_time]

print(ohlc_df)

