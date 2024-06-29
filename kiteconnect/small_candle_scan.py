from set_token import *
import pyautogui
import pyperclip
from myLib import *
import time
import getch

def user_input():
    while True:
        print("Press 'c' to continue: ", end='', flush=True)
        char = getch.getch()
        if char.lower() == 'c':
            print("\nContinuing...")
            break
        else:
            print("\nInvalid input. Please press 'c' to continue.")

kill_scanner()

margin=0.1

while True:
    lst=get_symbols_from_file("small_candle.txt")
    time.sleep(wait_for_5min()+10)
    for symbol in lst: 
        print(symbol)
        print(get_previous_ohlc_min5(symbol))
        o,h,l,c=get_previous_ohlc_min5(symbol)
        print(get_ma("NSE:"+symbol,"5minute"))
        if h<((l+l/10000)*8) and c<o:
            print(symbol)
            save_screenshot(symbol)

        '''
        sma20,sma40,sma200 =  get_ma("NSE:"+symbol,"5minute")
        save_screenshot(list(symbol))
        #user_input()
        if l<=sma20<=h or l<=sma200<=h:
            if h<=l+l*(margin/100):
                print("small_candle")
                print(symbol)
                save_screenshot(symbol)
    time.sleep(wait_for_5min())
        '''
