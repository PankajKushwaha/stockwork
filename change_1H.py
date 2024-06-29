import pyautogui
import time

tab = [(220,48),(317,47),(416,43),(508,45),(611,37),(688,39),(807,48),(899,45),(984,48),(1097,43)]

def H_1():
    pyautogui.moveTo(1096,748)
    time.sleep(0.5)
    pyautogui.click(clicks=1,interval=0.25)

for a,b in tab:
    pyautogui.moveTo(a,b)
    pyautogui.click(clicks=1,interval=0.25)
    H_1()

