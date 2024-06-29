from myLib import *
import datetime
import time

test_dic = {}

fno_lst = get_fno_list()

def get_min():
    current_minute = datetime.datetime.now().minute
    return current_minute

for symbol in fno_lst:
    test_dic[symbol] = []

def myFunc():
    flag=0
    while True:
        oldm=get_min()
        if oldm%5 == 0:
            while True:
                newm=get_min()
                ltpdic = get_ltp_dict()
                for symbol in fno_lst:
                    test_dic[symbol].append(ltpdic["NSE:"+symbol]) 
                if newm%5 == 0 and newm>oldm:
                    flag=1
                    break
                time.sleep(1)
                print(test_dic)
        if flag == 1:
            for symbol in fno_lst:
                print("NSE:"+symbol) 
                print("open") 
                print(test_dic[symbol][0]) 
                print("high") 
                print(max(test_dic[symbol])) 
                print("low") 
                print(min(test_dic[symbol])) 
                print("close") 
                print(test_dic[symbol][-1]) 
            break
        time.sleep(1)
        print(oldm)

myFunc()
