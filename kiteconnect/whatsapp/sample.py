import pyautogui
import pyperclip

pyautogui.moveTo(507,441)
pyautogui.click(clicks=2)
pyautogui.click(button='right')
pyautogui.moveTo(543,458)
pyautogui.click(clicks=1)

paste_data = pyperclip.paste()
print(paste_data)
