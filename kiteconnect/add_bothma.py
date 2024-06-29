import pyautogui
import pyperclip
from myLib import *

def get_symbol_from_page():
    pyautogui.moveTo(x=668, y=82)
    pyautogui.click(button='left', clicks=3, interval=0.25)
    pyautogui.hotkey('ctrl', 'c')
    copied_text = pyperclip.paste()
    symbol=copied_text.split("/")[-2]
    return symbol

symbol=get_symbol_from_page()
write_symbol_to_file("ma20_stocks.txt",symbol)
write_symbol_to_file("ma200_stocks.txt",symbol)
