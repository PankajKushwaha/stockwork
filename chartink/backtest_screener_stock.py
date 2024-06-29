import pandas as pd
import pyautogui
import time

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

my_file = open("log1.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
mylist = data.split("\n")
print(mylist)
my_file.close()
'''
#df = pd.read_csv('/home/pankaj/Downloads/Backtest 15 minute Stock Breakouts, Technical Analysis Scanner.csv') 
df = pd.read_fwf('test.txt')
df.to_csv('test.csv')
df = pd.read_csv('/home/pankaj/Documents/stocks/chartink/test.csv')
print(df)
#df = pd.read_csv('/home/pankaj/Documents/stocks/chartink/fo_mktlots.csv') 
#mylist = df['SYMBOL    '].tolist()
mylist = df['Symbol'].tolist()
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
mylist.pop(0)
print(mylist)
'''
mylist = list(set(mylist))
print(len(mylist))
#os.remove("/home/pankaj/Downloads/Backtest 15 minute Stock Breakouts, Technical Analysis Scanner.csv")
mylist = sorted(mylist)
print(len(mylist))
for stock in mylist:
    print(stock)
    click_wl()
    time.sleep(1)
    search_stock(stock.strip())
    time.sleep(1)
    click_plus()

