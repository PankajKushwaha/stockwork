import pyautogui
from myLib import *
import pyperclip

risk = 90

pyautogui.moveTo(x=668, y=82)
pyautogui.click(button='left', clicks=3, interval=0.25)
pyautogui.hotkey('ctrl', 'c')
copied_text = pyperclip.paste()
symbol=copied_text.split("/")[-2]
o,h,l,c=get_previous_ohlc_min5(symbol)
per = ((h-l)/h)*100
rs_to_buy = (100/per)*risk
quantity = int(rs_to_buy/c)
intraday_quantity = quantity/5
print(per)
print(rs_to_buy)
print(quantity)
print(get_previous_ohlc_min5(symbol))
pyperclip.copy(quantity)
pyautogui.moveTo(x=92, y=122)
pyautogui.click()
pyautogui.moveTo(x=220, y=200)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
pyautogui.moveTo(x=868, y=738)
pyautogui.click()
