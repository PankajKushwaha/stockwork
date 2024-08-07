from nsetools import Nse
import pandas as pd
import time
import pyautogui
import cv2
import numpy as np

nse = Nse()

percent_margin = 0.004
          

def less_by_margin(level):
    return (level - (level*percent_margin))

def more_by_margin(level):
    return (level + (level*percent_margin))

df = pd.read_csv('./monthly_pivot_nifty500_JUN.csv')

stock_list = []

count = 1
print(df)
for ind in df.index:
    try:
        price = nse.get_quote(df['symbol'][ind])['lastPrice']
    except:
        pass
    count = count + 1
    if count == 10:
        break
    if price is None:
        continue
    print(ind)
    R2 = df['R2'][ind]
    if price > less_by_margin(R2) and price < more_by_margin(R2):
        print(df['symbol'][ind])
        stock_list.append(df['symbol'][ind])
        continue
    
    R1 = df['R1'][ind]
    if price > less_by_margin(R1) and price < more_by_margin(R1):
        print(df['symbol'][ind])
        stock_list.append(df['symbol'][ind])
        continue

    top_cpr = df['top_cpr'][ind]
    if price < more_by_margin(top_cpr) and price > top_cpr:
        print(df['symbol'][ind])
        stock_list.append(df['symbol'][ind])
        continue

  #  bottom_cpr = df['bottom_cpr'][ind]
   # if price > less_by_margin(bottom_cpr) and price < bottom_cpr:
    #    print(df['symbol'][ind])
     #   continue

    S2 = df['S2'][ind]
    if price > less_by_margin(S2) and price < more_by_margin(S2):
        print(df['symbol'][ind])
        stock_list.append(df['symbol'][ind])
        continue

    S1 = df['R2'][ind]
    if price > less_by_margin(S1) and price < more_by_margin(S1):
        print(df['symbol'][ind])
        stock_list.append(df['symbol'][ind])
        continue


print(stock_list)
for stock in stock_list:
    pyautogui.click(166,122)
    pyautogui.typewrite(stock)
    time.sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(167,206)
    #pyautogui.typewrite(["enter"])
    time.sleep(1)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
    cv2.imwrite("/home/pankaj/Pictures/pivot/"+stock+".png", image)



