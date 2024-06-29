import pandas as pd
import time
import pyautogui
import cv2
import numpy as np
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime
import os
import shutil

percent_margin = 0.004

conn = sqlite3.connect("stock.db")
cursor = conn.cursor()
disk_engine = create_engine('sqlite:///stock.db')

dir_path="/home/pankaj/Pictures/near_monthly_pivot/"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
else:
    shutil.rmtree(dir_path)
    os.makedirs(dir_path)


def less_by_margin(level):
    return (level - (level*percent_margin))

def more_by_margin(level):
    return (level + (level*percent_margin))

df = pd.read_csv('./monthly_pivot_nifty500_JUN.csv')

stock_list = []

count = 1
print(df)
for ind in df.index:
    #price = nse.get_quote(df['symbol'][ind])['lastPrice']
    try:
        p2 = pd.read_sql('select * from '+df['symbol'][ind],  conn)
    except:
        continue
    p2 = p2.tail(1)
    price = float(p2["Close"])
    count = count + 1
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
    cv2.imwrite(dir_path+stock+".png", image)



