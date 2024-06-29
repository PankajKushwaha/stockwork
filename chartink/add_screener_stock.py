import pandas as pd
import pyautogui
import time
import sys

import os

def click_wl():
    pyautogui.click(140, 182)

def erase():
    pyautogui.moveTo(140, 182)
    pyautogui.doubleClick()


def search_stock(stock):
    pyautogui.write(stock)

def click_plus():
    pyautogui.moveTo(424,204)
    time.sleep(1)
    pyautogui.click()

df = pd.read_excel(sys.argv[1]) 
#df = pd.read_csv('/home/pankaj/Documents/stocks/chartink/fo_mktlots.csv') 
mylist = df['SYMBOL    '].tolist()
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
print(mylist)
mylist = list(set(mylist))
print(len(mylist))
#os.remove("/home/pankaj/Downloads/15 minute Stock Breakouts, Technical Analysis Scanner.xlsx")
mylist = sorted(mylist)
print(len(mylist))
'''
print(len(mylist[50:100]))
for stock in mylist[150:200]:
    print(stock)
    click_wl()
    time.sleep(1)
    search_stock(stock.strip())
    time.sleep(1)
    click_plus()
'''
