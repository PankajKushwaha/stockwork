from kiteconnect import KiteConnect
#from get_list_to_monitor import *
from set_token import *
import datetime
import os
import sys
import shutil
import pyautogui
import cv2
import time
import numpy as np
import click
import pickle
import time
import logging
from nsepython import *
from pynse import *
import pandas as pd
from heapq import nlargest
from heapq import nsmallest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from nsepython import *


def get_open_position_price_dic():
    target=float(sys.argv[1])
    open_position_list = []
    open_position_price_dic = {}
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        #open_position_list.append("NFO:"+dic['tradingsymbol'])
        print(dic['tradingsymbol'])
        q=dic['buy_quantity']
        p=dic['buy_price']
        tp=(target+q*p)/q
        print(tp)

get_open_position_price_dic()
