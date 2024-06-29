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
mylist = df['Unnamed: 2'].tolist()
mylist.pop(0)
print(mylist)
for stock in mylist[0:50]:
    print(stock)
    click_wl()
    time.sleep(1)
    search_stock(stock.strip())
    time.sleep(1)
    click_plus()
