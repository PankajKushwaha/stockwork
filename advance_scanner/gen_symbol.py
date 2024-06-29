import pandas as pd

df = pd.read_csv("./ind_nifty200list.csv")
stock_list=df["Symbol"].tolist()

s = "NIFITY200=["

for stock in stock_list:
    s=s+"\""+stock+"\""+","
s=s+"]"
s=s.replace(",]","]")
print(s)
#print(df["Symbol"].tolist())
