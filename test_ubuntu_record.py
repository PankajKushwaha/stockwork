import pyautogui

def make_fullscreen():
    pyautogui.click(1230,45)

def start_stop_recording():
    pyautogui.keyDown('ctrl')  # hold down the shift key
    pyautogui.keyDown('alt')  # hold down the shift key
    pyautogui.keyDown('shift')  # hold down the shift key
    pyautogui.keyDown('R')  # hold down the shift key
    pyautogui.keyUp('ctrl')  # hold down the shift key
    pyautogui.keyUp('alt')  # hold down the shift key
    pyautogui.keyUp('shift')  # hold down the shift key
    pyautogui.keyUp('R')  # hold down the shift key

def main_fun():
    make_fullscreen()

make_fullscreen()
