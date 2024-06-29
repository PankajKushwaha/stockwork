import pyautogui
import pickle
import time
import pause,datetime
from nsetools import Nse

nse = Nse()

order_list = pickle.load( open( "order.p", "rb" ) )

def open_all_chart():
    print(sorted(list(order_list.keys()),reverse = True))
    for symbol in sorted(list(order_list.keys()),reverse = True):
        pyautogui.click(145,40) #click tab
        pyautogui.click(520,185) # search symbol
        print(order_list[symbol])
        pyautogui.typewrite(symbol)
        time.sleep(1)
        pyautogui.click(515,270)
        time.sleep(2)
        pyautogui.click(1240,185)
        time.sleep(4)

def prepare_order_window():
    symbolList = list(order_list.keys())
    print(type(symbolList))
    for symbol in sorted(symbolList):
        print(symbol)
        print(order_list[symbol])
        print(order_list[symbol][2])
        print(order_list[symbol][3])
        sl_percentage = ((order_list[symbol][1] - order_list[symbol][2])/order_list[symbol][1])*100  + 0.05
        sl_percentage = ( int(sl_percentage*100) - (int(sl_percentage*100)%5)) / 100
        sl_percentage = -sl_percentage
        target_percentage = ((order_list[symbol][3] - order_list[symbol][1])/order_list[symbol][1])*100  - 0.05
        target_percentage = ( int(target_percentage*100) - (int(target_percentage*100)%5)) / 100
        order_list[symbol][2] = sl_percentage
        order_list[symbol][3] = target_percentage
        print(sl_percentage)
        print(target_percentage)
        time.sleep(2)


def place_order():
    delta = 0
    for symbol in sorted(list(order_list.keys())):
        pyautogui.click(340+delta,45) # click tab
        pyautogui.click(90,120) # click thunder
        pyautogui.click(130,200) # click buy
        pyautogui.moveTo(475,575) # click quantiy
        time.sleep(1)
        pyautogui.typewrite(str(order_list[symbol][0]))
        print(symbol)
        ltp = nse.get_quote(symbol)['open']
        if ltp < float(order_list[symbol][1]):
            pyautogui.click(925,620) # click slm
            pyautogui.moveTo(845,585) # click pricewindow
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.typewrite(str(order_list[symbol][1]))
        else:
            pyautogui.click(720,620) # click limit order
            pyautogui.moveTo(675,575) # click pricewindow
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.typewrite(str(order_list[symbol][1]))

        pyautogui.click(515,675) # click  set sl
        pyautogui.moveTo(605,675)
        time.sleep(1)
        pyautogui.typewrite(str(order_list[symbol][2]))

        pyautogui.click(715,675) # click  set target
        pyautogui.moveTo(790,675)
        time.sleep(1)
        pyautogui.typewrite(str(order_list[symbol][3]))
        delta = delta + 180

def execute_order():
    delta = 0
    for symbol in sorted(list(order_list.keys())):
        pyautogui.click(340+delta,45) # click tab
        ltp = nse.get_quote(symbol)['open']
        if ltp < float(order_list[symbol][1]):
            time.sleep(1)
            pyautogui.click(925,620) # click slm
            pyautogui.moveTo(845,585) # click pricewindow
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.typewrite(str(order_list[symbol][1]))
        else:
            time.sleep(1)
            pyautogui.click(720,620) # click limit order
            pyautogui.moveTo(675,575) # click pricewindow
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.25)
            pyautogui.typewrite(str(order_list[symbol][1]))
        pyautogui.click(835,735) # click limit order
        delta = delta + 180

def click_all_tab():
    delta = 0
    for i in range(1,6):
        pyautogui.click(340+delta,45) # search symbol
        time.sleep(1)
        delta = delta + 180
        print(i)
        
open_all_chart()
prepare_order_window()
place_order()
dt = datetime.datetime(2021, 5, 14, 9, 15,2)
pause.until(dt)
execute_order()
