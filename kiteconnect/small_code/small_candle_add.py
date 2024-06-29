from set_token import *
import pyautogui
import pyperclip

file_path = "small_candle.pkl"

lst=[]

with open(file_path, 'rb') as f:
    loaded_list = pickle.load(f)

pyautogui.moveTo(x=668, y=82)
pyautogui.click(button='left', clicks=3, interval=0.25)
pyautogui.hotkey('ctrl', 'c')
copied_text = pyperclip.paste()
symbol=copied_text.split("/")[-2]

print(symbol)
