import pandas as pd

file_name="tick.csv"

df = pd.read_csv(file_name)
print(df)
df.drop(columns=['last_quantity','average_price','volume','buy_quantity','sell_quantity','ohlc','change','oi','oi_day_high','oi_day_low', 'depth'], inplace=True)
print(df.columns)
print(df)
filtered_df = df[~df["last_trade_time"].str.contains("18:39:")]
filtered_df.to_csv("output_tick.csv")
