from myLib import *
import pandas as pd

df=pd.read_csv("tick.csv")
filtered_df = df[~df['timestamp'].apply(contains_substring)]
filtered_df.to_csv("tick.csv")


