from myLib import *
import time
import os
from datetime import datetime

old_ltp = {}

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return ["NSE:"+line.strip().upper() for line in lines]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def run():
    ltp_dic = get_ltp_dict( read_file ( "buy_fut.txt"))
    print(ltp_dic)
    if len(old_ltp) == 0:
        for symbol in ltp_dic:
            ltp=ltp_dic[symbol]
            old_ltp[symbol]=ltp
    else:
        for symbol in ltp_dic:
            new_ltp=ltp_dic[symbol]
            ma20=get_20ma_5minute(symbol)
            if new_ltp > ma20 and old_ltp[symbol] < ma20:
                os.system("python3 buy_future.py "+symbol)
                print("=== EXECUTED ===")
                break
            else:
                old_ltp[symbol]=new_ltp


#print(read_file("buy_fut.txt"))
while True:
    print(datetime.now())
    run()
    time.sleep(2)
