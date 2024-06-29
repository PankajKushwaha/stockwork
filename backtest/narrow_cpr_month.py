import pandas as pd
from nsetools import Nse

nse = Nse()

df = pd.read_csv('monthly_pivot_nifty100_may.csv')

price_dic = {}

df_premarket = pd.read_csv("MW-Pre-Open-Market-07-May-2021.csv")
df_premarket.columns = df_premarket.columns.str.replace('\\n', '')
df_premarket.columns = df_premarket.columns.str.replace(' ', '')

for ind in df_premarket.index:
    price_dic[df_premarket['SYMBOL'][ind]] = df_premarket['IEPPRICE'][ind]



for ind in df.index:
    bottom_cpr = df['bottom_cpr'][ind]
    top_cpr = df['top_cpr'][ind]
    #try:
        #low = nse.get_quote(df['symbol'][ind])['dayLow']
    #except:
     #   pass

    #if low > top_cpr and low < ( top_cpr+top_cpr*0.005): 
     #   print(df['symbol'][ind])
      #  continue
    if top_cpr < (bottom_cpr+bottom_cpr*0.008): 
        print(df['symbol'][ind])
        continue


