import pyautogui
import time


chart_wl = [(344,233),(346,284),(340,330),(339,382),(345,422),(343,466),(347,517),(346,553),(340,608),(345,650)]

print(len(chart_wl))

def tab():
    pyautogui.moveTo(95,44)
    pyautogui.click(clicks=2,interval=0.25)

def popout():
    pyautogui.moveTo(1243,183)
    pyautogui.click(clicks=2,interval=0.25)


for a,b in chart_wl:
    tab()
    pyautogui.moveTo(a,b)
    time.sleep(1)
    pyautogui.click(clicks=2,interval=0.25)
    time.sleep(2)
    popout()
