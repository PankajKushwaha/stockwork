from myLib import *
import pyautogui

lst = get_all_fut_symbol()

add_stock(lst[:100])
pyautogui.click(140,751)
add_stock(lst[100:])
