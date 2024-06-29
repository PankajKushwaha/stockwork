import pyautogui
import time

tab = [(220,48),(317,47),(416,43),(508,45),(611,37),(688,39),(807,48),(899,45),(984,48),(1097,43)]

def H_3():
    pyautogui.moveTo(760,127)
    #time.sleep(1)
    pyautogui.click(clicks=1,interval=0.25)
    pyautogui.moveTo(763,466)
    #time.sleep(1)
    pyautogui.click(clicks=1,interval=0.25)

for a,b in tab:
    pyautogui.moveTo(a,b)
    pyautogui.click(clicks=1,interval=0.25)
    time.sleep(0.5)
    H_3()

