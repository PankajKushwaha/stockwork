from myLib import *

fnolst = get_fno_list()

def add_stock(stock):
    pyautogui.click(140, 182)
    pyautogui.doubleClick()
    pyautogui.write(stock)
    pyautogui.moveTo(466,261)
    time.sleep(1)
    pyautogui.click()

lst = []
for symbol in fnolst:
    o,h,l,c=get_current_ohlc_min5(symbol)
    ma200 = get_200ma_5minute(symbol)
    if l<=ma200<h:
        lst.append(symbol)
        print(symbol)
        print(ma200)
        print(h)
        print(l)
        add_stock(symbol)
#save_screenshot(lst,"/home/pankaj/Pictures")
