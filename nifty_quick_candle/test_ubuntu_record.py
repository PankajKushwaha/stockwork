import pyautogui
import time
import os, os.path

def make_fullscreen():
    pyautogui.click(1230,45)

def total_number_of_file():
    lst = os.listdir('/home/pankaj/Pictures') # dir is your directory path
    number_files = len(lst)
    return number_files
    #return len([name for name in os.listdir('/home/pankaj/Pictures') if os.path.isfile(name)])

def open_single_image():
    pyautogui.click(33,317)
    time.sleep(2)
    pyautogui.click(143,280)
    time.sleep(1)
    pyautogui.moveTo(340,105)
    pyautogui.doubleClick()
    time.sleep(1)

def start_stop_recording(folder):
    counter=0
    pyautogui.hotkey('ctrl', 'alt','shift', 'R')
    '''
    pyautogui.keyDown('ctrl')  # hold down the shift key
    pyautogui.keyDown('alt')  # hold down the shift key
    pyautogui.keyDown('shift')  # hold down the shift key
    pyautogui.keyDown('R')  # hold down the shift key
    pyautogui.keyUp('ctrl')  # hold down the shift key
    pyautogui.keyUp('alt')  # hold down the shift key
    pyautogui.keyUp('shift')  # hold down the shift key
    pyautogui.keyUp('R')  # hold down the shift key
    '''

def main_func():
    print(total_number_of_file())

main_func()
