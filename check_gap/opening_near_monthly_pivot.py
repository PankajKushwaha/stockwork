import pandas as pd

percent_margin = 0.003

df_premarket = pd.read_csv("MW-Pre-Open-Market-06-May-2021.csv")
df_pivot = pd.read_csv("monthly_pivot_nifty500_may.csv")

def less_by_margin(level):
    return (level - (level*percent_margin))

def more_by_margin(level):
    return (level + (level*percent_margin))


dic = {}

#remove new line character and space
df_premarket.columns = df_premarket.columns.str.replace('\\n', '')
df_premarket.columns = df_premarket.columns.str.replace(' ', '')


#for ind in df.index:
 #   df_premarket


#for ind in df_premarket.index:
#df_premarket.index.name = None
k = df_premarket[df_premarket['SYMBOL'] == "ONGC"]["IEPPRICE"]


#print(k[0])


for ind in df_premarket.index:
    #print(df_premarket['SYMBOL'][ind])
    #print(df_premarket['IEPPRICE'][ind])
    dic[df_premarket['SYMBOL'][ind]] = df_premarket['IEPPRICE'][ind]
    #dic.add(df_premarket['SYMBOL'][ind],df_premarket['IEPPRICE'][ind])

print(dic)

for ind in df_pivot.index:
    if df_pivot['symbol'][ind] in dic:
        #print(df_pivot['symbol'][ind])
        #print(dic[df_pivot['symbol'][ind]])
        price = dic[df_pivot['symbol'][ind]]
        price = price.replace(",","")
        price = float(price)


        #R2 = df_pivot['R2'][ind]
        #if price > less_by_margin(R2) and price < more_by_margin(R2):
         #   print(df_pivot['symbol'][ind])
          #  continue

        R1 = df_pivot['R1'][ind]
        #if price > less_by_margin(R1) and price < more_by_margin(R1):
        if price < less_by_margin(R1) and price > R1:
            print(df_pivot['symbol'][ind])
            continue

        top_cpr = df_pivot['top_cpr'][ind]
        if price < more_by_margin(top_cpr) and price > top_cpr:
            print(df_pivot['symbol'][ind])
            continue

        #bottom_cpr = df_pivot['bottom_cpr'][ind]
        #if price > less_by_margin(bottom_cpr) and price < bottom_cpr:
         #   print(df_pivot['symbol'][ind])
          #  continue


        #S2 = df_pivot['S2'][ind]
        #if price > less_by_margin(S2) and price < more_by_margin(S2):
         #   print(df_pivot['symbol'][ind])
          #  continue

        #S1 = df_pivot['R2'][ind]
        #if price > less_by_margin(S1) and price < more_by_margin(S1):
         #   print(df_pivot['symbol'][ind])
          #  continue



    #print(dic["WIPRO"])

#    if price is None:
 #       continue

 
