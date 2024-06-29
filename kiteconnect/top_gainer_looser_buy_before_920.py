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
from pynput import keyboard
from dateutil.relativedelta import relativedelta
from threading import Thread, Lock
import concurrent.futures


sys.tracebacklimit = None
already_top_gainer = []
already_top_looser = []
new_day_high_dic={}
new_day_low_dic={}
min5_ohlc_dic={}
#global_high_low = []
global_high_low_flag = 0
old_minute=-1
roc_dic={}
old_ltp_dict ={}
firsttime=True

nse = Nse()
pd.set_option('display.max_columns', None)

gSecondNow=0
gNumOfCall=0
mutex=Lock()


def save_structure_to_file(list_name):
    with open("finallist", 'wb') as handle:
        pickle.dump(list_name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def save_structure_to_file_wrapper(filename,structure_name):
    with open(filename, 'wb') as handle:
        pickle.dump(structure_name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_structure_from_file(watchlist):
    if os.path.isfile(watchlist):
        with open(watchlist, 'rb') as handle:
            lst = pickle.load(handle)
            return lst
    else:
        return []

global_high_low=load_structure_from_file("finallist")
global_cross_ma20 = load_structure_from_file("global_cross_ma20")
global_cross_ma200 = load_structure_from_file("global_cross_ma200")
def get_strike_price_put(symbol,expiry_date):
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,str(expiry_date),"full")
        a = int(oi_data.iloc[oi_data["PUTS_Volume"].idxmax()]["Strike Price"])
    except:
        a=None
    return a

def get_strike_price_call(symbol,expiry_date):
    try:
        oi_data, ltp, crontime = oi_chain_builder(symbol,str(expiry_date),"full")
        a = int(oi_data.iloc[oi_data["CALLS_Volume"].idxmax()]["Strike Price"])
    except:
        a=None
    return a

def get_call_put_option(symbol,expiry_date,expiry_month,current_year):
    #get_call_put_option("ZEEL","25-Aug-2022","AUG","22")
    sp_call = get_strike_price_call(symbol,expiry_date)
    sp_put = get_strike_price_put(symbol,expiry_date)
    #print(symbol+current_year+expiry_month+str(sp_call)+"CE")
    #print(symbol+current_year+expiry_month+str(sp_put)+"PE")
    call_symbol=symbol+current_year+expiry_month+str(sp_call)+"CE"
    put_symbol=symbol+current_year+expiry_month+str(sp_put)+"PE"
    return call_symbol,put_symbol

old_day_low = {}
old_day_high = {}
ohlc_bw_20_200ma=[]
sma19=load_structure_from_file("ma19")
sma199=load_structure_from_file("ma199")
redCandle=load_structure_from_file("redCandle")
greenCandle=load_structure_from_file("greenCandle")


#NIFTYFNO=load_structure_from_file("listtomonitor")
#print(len(NIFTYFNO))

NIFTYFNO=['NSE:ABCAPITAL', 'NSE:APOLLOHOSP', 'NSE:ABFRL', 'NSE:ASIANPAINT', 'NSE:ACC', 'NSE:ASHOKLEY', 'NSE:BHARTIARTL', 'NSE:BAJAJ-AUTO', 'NSE:APOLLOTYRE', 'NSE:BALKRISIND', 'NSE:ASTRAL', 'NSE:ATUL', 'NSE:AXISBANK', 'NSE:BAJFINANCE', 'NSE:BIOCON', 'NSE:BRITANNIA', 'NSE:BALRAMCHIN', 'NSE:BANDHANBNK', 'NSE:BANKBARODA', 'NSE:BATAINDIA', 'NSE:BERGEPAINT', 'NSE:BHARATFORG', 'NSE:CANBK', 'NSE:RBLBANK', 'NSE:BHEL', 'NSE:CIPLA', 'NSE:COLPAL', 'NSE:BOSCHLTD', 'NSE:BPCL', 'NSE:BSOFT', 'NSE:CUMMINSIND', 'NSE:CANFINHOME', 'NSE:COALINDIA', 'NSE:CONCOR', 'NSE:COROMANDEL', 'NSE:FEDERALBNK', 'NSE:CUB', 'NSE:DIVISLAB', 'NSE:DLF', 'NSE:GODREJCP', 'NSE:ESCORTS', 'NSE:HAL', 'NSE:EXIDEIND', 'NSE:FSL', 'NSE:HDFC', 'NSE:GAIL', 'NSE:GLENMARK', 'NSE:GMRINFRA', 'NSE:HDFCBANK', 'NSE:HDFCLIFE', 'NSE:GODREJPROP', 'NSE:GRANULES', 'NSE:GRASIM', 'NSE:HEROMOTOCO', 'NSE:HDFCAMC', 'NSE:INFY', 'NSE:HINDPETRO', 'NSE:IBULHSGFIN', 'NSE:ICICIBANK', 'NSE:IOC', 'NSE:ICICIPRULI', 'NSE:IEX', 'NSE:IGL', 'NSE:INDIACEM', 'NSE:INDIAMART', 'NSE:JKCEMENT', 'NSE:INTELLECT', 'NSE:LT', 'NSE:LUPIN', 'NSE:IPCALAB', 'NSE:MANAPPURAM', 'NSE:JUBLFOOD', 'NSE:KOTAKBANK', 'NSE:MPHASIS', 'NSE:L&TFH', 'NSE:LALPATHLAB', 'NSE:LAURUSLABS', 'NSE:LICHSGFIN', 'NSE:NAUKRI', 'NSE:NESTLEIND', 'NSE:M&MFIN', 'NSE:MARICO', 'NSE:MCDOWELL-N', 'NSE:OFSS', 'NSE:MFSL', 'NSE:MGL', 'NSE:ONGC', 'NSE:ABBOTINDIA', 'NSE:MOTHERSON', 'NSE:MRF', 'NSE:NAVINFLUOR', 'NSE:OBEROIRLTY', 'NSE:PAGEIND', 'NSE:PEL', 'NSE:PFC', 'NSE:PIDILITIND', 'NSE:PNB', 'NSE:PETRONET', 'NSE:RECLTD', 'NSE:SBIN', 'NSE:SRF', 'NSE:TATAPOWER', 'NSE:TECHM', 'NSE:ZYDUSLIFE', 'NSE:POLYCAB', 'NSE:PVR', 'NSE:RAIN', 'NSE:ADANIENT', 'NSE:CHAMBLFERT', 'NSE:RELIANCE', 'NSE:SBICARD', 'NSE:SUNPHARMA', 'NSE:SUNTV', 'NSE:TATACHEM', 'NSE:TATACOMM', 'NSE:TATAMOTORS', 'NSE:TITAN', 'NSE:TORNTPOWER', 'NSE:TRENT', 'NSE:TVSMOTOR', 'NSE:UPL', 'NSE:WHIRLPOOL', 'NSE:WIPRO', 'NSE:ZEEL', 'NSE:ADANIPORTS', 'NSE:HINDALCO', 'NSE:AARTIIND', 'NSE:AMBUJACEM', 'NSE:INDIGO', 'NSE:AUROPHARMA', 'NSE:BAJAJFINSV', 'NSE:JSWSTEEL', 'NSE:AUBANK',  'NSE:COFORGE', 'NSE:CROMPTON', 'NSE:DABUR', 'NSE:DALBHARAT', 'NSE:DELTACORP', 'NSE:DIXON', 'NSE:EICHERMOT', 'NSE:GUJGASLTD', 'NSE:HAVELLS', 'NSE:HCLTECH', 'NSE:NATIONALUM', 'NSE:PERSISTENT', 'NSE:HINDUNILVR', 'NSE:HONAUT', 'NSE:INDHOTEL', 'NSE:SAIL', 'NSE:INDUSINDBK', 'NSE:TATASTEEL', 'NSE:IRCTC', 'NSE:JINDALSTEL', 'NSE:TORNTPHARM', 'NSE:LTTS', 'NSE:UBL', 'NSE:METROPOLIS', 'NSE:ALKEM', 'NSE:MUTHOOTFIN', 'NSE:DEEPAKNTR', 'NSE:POWERGRID', 'NSE:GNFC', 'NSE:SBILIFE', 'NSE:SHREECEM', 'NSE:SIEMENS', 'NSE:ICICIGI', 'NSE:SYNGENE', 'NSE:TATACONSUM', 'NSE:VOLTAS', 'NSE:INDUSTOWER', 'NSE:ITC', 'NSE:PIIND', 'NSE:ABB', 'NSE:BEL', 'NSE:CHOLAFIN', 'NSE:DRREDDY', 'NSE:MARUTI', 'NSE:HINDCOPPER', 'NSE:M&M', 'NSE:RAMCOCEM', 'NSE:NTPC', 'NSE:ULTRACEMCO', 'NSE:VEDL', 'NSE:NMDC', 'NSE:TCS']



token_to_symbol = {1793: 'NSE:AARTIIND', 3329: 'NSE:ABB', 4583169: 'NSE:ABBOTINDIA', 5533185: 'NSE:ABCAPITAL', 7707649: 'NSE:ABFRL', 5633: 'NSE:ACC', 6401: 'NSE:ADANIENT', 3861249: 'NSE:ADANIPORTS', 2995969: 'NSE:ALKEM', 25601: 'NSE:AMARAJABAT', 325121: 'NSE:AMBUJACEM', 40193: 'NSE:APOLLOHOSP', 41729: 'NSE:APOLLOTYRE', 54273: 'NSE:ASHOKLEY', 60417: 'NSE:ASIANPAINT', 3691009: 'NSE:ASTRAL', 67329: 'NSE:ATUL', 5436929: 'NSE:AUBANK', 70401: 'NSE:AUROPHARMA', 1510401: 'NSE:AXISBANK', 4267265: 'NSE:BAJAJ-AUTO', 4268801: 'NSE:BAJAJFINSV', 81153: 'NSE:BAJFINANCE', 85761: 'NSE:BALKRISIND', 87297: 'NSE:BALRAMCHIN', 579329: 'NSE:BANDHANBNK', 1195009: 'NSE:BANKBARODA', 94977: 'NSE:BATAINDIA', 98049: 'NSE:BEL', 103425: 'NSE:BERGEPAINT', 108033: 'NSE:BHARATFORG', 2714625: 'NSE:BHARTIARTL', 112129: 'NSE:BHEL', 2911489: 'NSE:BIOCON', 558337: 'NSE:BOSCHLTD', 134657: 'NSE:BPCL', 140033: 'NSE:BRITANNIA', 1790465: 'NSE:BSOFT', 2763265: 'NSE:CANBK', 149249: 'NSE:CANFINHOME', 163073: 'NSE:CHAMBLFERT', 175361: 'NSE:CHOLAFIN', 177665: 'NSE:CIPLA', 5215745: 'NSE:COALINDIA', 2955009: 'NSE:COFORGE', 3876097: 'NSE:COLPAL', 1215745: 'NSE:CONCOR', 189185: 'NSE:COROMANDEL', 4376065: 'NSE:CROMPTON', 1459457: 'NSE:CUB', 486657: 'NSE:CUMMINSIND', 197633: 'NSE:DABUR', 2067201: 'NSE:DALBHARAT', 5105409: 'NSE:DEEPAKNTR', 3851265: 'NSE:DELTACORP', 2800641: 'NSE:DIVISLAB', 5552641: 'NSE:DIXON', 3771393: 'NSE:DLF', 225537: 'NSE:DRREDDY', 232961: 'NSE:EICHERMOT', 245249: 'NSE:ESCORTS', 173057: 'NSE:EXIDEIND', 261889: 'NSE:FEDERALBNK', 3661825: 'NSE:FSL', 1207553: 'NSE:GAIL', 1895937: 'NSE:GLENMARK', 3463169: 'NSE:GMRINFRA', 300545: 'NSE:GNFC', 2585345: 'NSE:GODREJCP', 4576001: 'NSE:GODREJPROP', 3039233: 'NSE:GRANULES', 315393: 'NSE:GRASIM', 3378433: 'NSE:GSPL', 2713345: 'NSE:GUJGASLTD', 589569: 'NSE:HAL', 2513665: 'NSE:HAVELLS', 1850625: 'NSE:HCLTECH', 340481: 'NSE:HDFC', 1086465: 'NSE:HDFCAMC', 341249: 'NSE:HDFCBANK', 119553: 'NSE:HDFCLIFE', 345089: 'NSE:HEROMOTOCO', 348929: 'NSE:HINDALCO', 4592385: 'NSE:HINDCOPPER', 359937: 'NSE:HINDPETRO', 356865: 'NSE:HINDUNILVR', 874753: 'NSE:HONAUT', 7712001: 'NSE:IBULHSGFIN', 1270529: 'NSE:ICICIBANK', 5573121: 'NSE:ICICIGI', 4774913: 'NSE:ICICIPRULI', 3677697: 'NSE:IDEA', 3060993: 'NSE:IDFC', 2863105: 'NSE:IDFCFIRSTB', 56321: 'NSE:IEX', 2883073: 'NSE:IGL', 387073: 'NSE:INDHOTEL', 387841: 'NSE:INDIACEM', 2745857: 'NSE:INDIAMART', 2865921: 'NSE:INDIGO', 1346049: 'NSE:INDUSINDBK', 7458561: 'NSE:INDUSTOWER', 408065: 'NSE:INFY', 1517057: 'NSE:INTELLECT', 415745: 'NSE:IOC', 418049: 'NSE:IPCALAB', 3484417: 'NSE:IRCTC', 424961: 'NSE:ITC', 1723649: 'NSE:JINDALSTEL', 3397121: 'NSE:JKCEMENT', 3001089: 'NSE:JSWSTEEL', 4632577: 'NSE:JUBLFOOD', 492033: 'NSE:KOTAKBANK', 6386689: 'NSE:L&TFH', 2983425: 'NSE:LALPATHLAB', 4923905: 'NSE:LAURUSLABS', 511233: 'NSE:LICHSGFIN', 2939649: 'NSE:LT', 4561409: 'NSE:LTI', 4752385: 'NSE:LTTS', 2672641: 'NSE:LUPIN', 519937: 'NSE:M&M', 3400961: 'NSE:M&MFIN', 4879617: 'NSE:MANAPPURAM', 1041153: 'NSE:MARICO', 2815745: 'NSE:MARUTI', 2674433: 'NSE:MCDOWELL-N', 7982337: 'NSE:MCX', 2452737: 'NSE:METROPOLIS', 548353: 'NSE:MFSL', 4488705: 'NSE:MGL', 3675137: 'NSE:MINDTREE', 1076225: 'NSE:MOTHERSON', 1152769: 'NSE:MPHASIS', 582913: 'NSE:MRF', 6054401: 'NSE:MUTHOOTFIN', 91393: 'NSE:NAM-INDIA', 1629185: 'NSE:NATIONALUM', 3520257: 'NSE:NAUKRI', 3756033: 'NSE:NAVINFLUOR', 8042241: 'NSE:NBCC', 4598529: 'NSE:NESTLEIND', 3924993: 'NSE:NMDC', 2977281: 'NSE:NTPC', 5181953: 'NSE:OBEROIRLTY', 2748929: 'NSE:OFSS', 633601: 'NSE:ONGC', 3689729: 'NSE:PAGEIND', 617473: 'NSE:PEL', 4701441: 'NSE:PERSISTENT', 2905857: 'NSE:PETRONET', 3660545: 'NSE:PFC', 681985: 'NSE:PIDILITIND', 6191105: 'NSE:PIIND', 2730497: 'NSE:PNB', 2455041: 'NSE:POLYCAB', 3834113: 'NSE:POWERGRID', 3365633: 'NSE:PVR', 3926273: 'NSE:RAIN', 523009: 'NSE:RAMCOCEM', 4708097: 'NSE:RBLBANK', 3930881: 'NSE:RECLTD', 738561: 'NSE:RELIANCE', 758529: 'NSE:SAIL', 4600577: 'NSE:SBICARD', 5582849: 'NSE:SBILIFE', 779521: 'NSE:SBIN', 794369: 'NSE:SHREECEM', 806401: 'NSE:SIEMENS', 837889: 'NSE:SRF', 1102337: 'NSE:SRTRANSFIN', 857857: 'NSE:SUNPHARMA', 3431425: 'NSE:SUNTV', 2622209: 'NSE:SYNGENE', 871681: 'NSE:TATACHEM', 952577: 'NSE:TATACOMM', 878593: 'NSE:TATACONSUM', 884737: 'NSE:TATAMOTORS', 877057: 'NSE:TATAPOWER', 895745: 'NSE:TATASTEEL', 2953217: 'NSE:TCS', 3465729: 'NSE:TECHM', 897537: 'NSE:TITAN', 900609: 'NSE:TORNTPHARM', 3529217: 'NSE:TORNTPOWER', 502785: 'NSE:TRENT', 2170625: 'NSE:TVSMOTOR', 4278529: 'NSE:UBL', 2952193: 'NSE:ULTRACEMCO', 2889473: 'NSE:UPL', 784129: 'NSE:VEDL', 951809: 'NSE:VOLTAS', 4610817: 'NSE:WHIRLPOOL', 969473: 'NSE:WIPRO', 975873: 'NSE:ZEEL', 2029825: 'NSE:ZYDUSLIFE'}
symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}

#NIFTYFNO=['ABB', 'HONAUT', 'DALBHARAT', 'GODREJCP', 'BAJFINANCE', 'BAJAJFINSV', 'BRITANNIA', 'AUBANK', 'TRENT', 'GUJGASLTD', 'INTELLECT', 'HINDUNILVR', 'ESCORTS', 'DIXON', 'BATAINDIA', 'ICICIGI', 'CONCOR', 'APOLLOTYRE', 'WHIRLPOOL', 'EICHERMOT', 'RAMCOCEM', 'HINDPETRO', 'M&MFIN', 'SIEMENS', 'HEROMOTOCO', 'SBICARD', 'IDEA', 'ASIANPAINT', 'IEX', 'GODREJPROP', 'ZEEL', 'HAVELLS', 'CUMMINSIND', 'TITAN', 'MARUTI', 'UBL', 'COROMANDEL', 'ABBOTINDIA', 'BERGEPAINT', 'PERSISTENT', 'JKCEMENT', 'ABCAPITAL', 'LTTS', 'DELTACORP', 'AARTIIND', 'MRF', 'KOTAKBANK', 'BOSCHLTD', 'INDIACEM', 'TATACONSUM', 'LICHSGFIN', 'COLPAL', 'SHREECEM', 'BPCL', 'PAGEIND', 'SUNTV', 'RBLBANK', 'FSL', 'BAJAJ-AUTO', 'PIIND', 'GLENMARK', 'BIOCON', 'NAUKRI', 'M&M', 'ADANIPORTS', 'MGL', 'HDFCAMC', 'DLF', 'VOLTAS', 'OBEROIRLTY', 'IBULHSGFIN', 'L&TFH', 'MCDOWELL-N', 'NESTLEIND', 'INDUSTOWER', 'PIDILITIND', 'DABUR', 'MPHASIS', 'GMRINFRA', 'IPCALAB', 'MFSL', 'CANBK', 'OFSS', 'APOLLOHOSP', 'PETRONET', 'COFORGE', 'POLYCAB', 'ICICIPRULI', 'GRASIM', 'SBIN', 'BHEL', 'MINDTREE', 'LTI', 'TVSMOTOR', 'CROMPTON', 'AUROPHARMA', 'INDUSINDBK', 'BANDHANBNK', 'MARICO', 'ULTRACEMCO', 'IDFCFIRSTB', 'MOTHERSON', 'INDIGO', 'AMARAJABAT', 'TORNTPOWER', 'ALKEM', 'TCS', 'INDIAMART', 'LAURUSLABS', 'ACC', 'ASHOKLEY', 'METROPOLIS', 'IRCTC', 'HDFCBANK', 'NBCC', 'DEEPAKNTR', 'DIVISLAB', 'TATACOMM', 'HINDCOPPER', 'AXISBANK', 'NATIONALUM', 'JUBLFOOD', 'BHARTIARTL', 'IGL', 'TATAMOTORS', 'IDFC', 'ABFRL', 'ZYDUSLIFE', 'ICICIBANK', 'TATACHEM', 'INFY', 'BANKBARODA', 'RECLTD', 'UPL', 'ADANIENT', 'HDFC', 'BEL', 'TECHM', 'JINDALSTEL', 'GNFC', 'BALKRISIND', 'PEL', 'CIPLA', 'NAM-INDIA', 'NAVINFLUOR', 'FEDERALBNK', 'ITC', 'PNB', 'CANFINHOME', 'MANAPPURAM', 'WIPRO', 'EXIDEIND', 'MCX', 'TATAPOWER', 'CHAMBLFERT', 'HCLTECH', 'JSWSTEEL', 'SBILIFE', 'ASTRAL', 'AMBUJACEM', 'INDHOTEL', 'SUNPHARMA', 'SRF', 'TORNTPHARM', 'GSPL', 'LALPATHLAB', 'CUB', 'SRTRANSFIN', 'CHOLAFIN', 'GAIL', 'SAIL', 'LUPIN', 'RAIN', 'DRREDDY', 'PFC', 'TATASTEEL', 'MUTHOOTFIN', 'PVR', 'BHARATFORG', 'LT', 'SYNGENE', 'COALINDIA', 'GRANULES', 'HAL', 'ATUL', 'RELIANCE', 'NTPC', 'HDFCLIFE', 'HINDALCO', 'VEDL', 'BSOFT', 'IOC', 'POWERGRID', 'NMDC', 'BALRAMCHIN', 'ONGC']


def get_first_last_date_prev_month():
    dateList=[]
    dateListModify=[]
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("month")
    currentMonth = datetime.now().month
    currentDateList=[]
    prevMonth = currentMonth-1
    if currentMonth == 1:
        prevMonth = 12
    candle = kite.historical_data(symbol_to_token["NSE:ASIANPAINT"], from_date, to_date,"day" , continuous=False, oi=False)
    for i in candle:
        date=str(i["date"]).split()[0]
        if "-"+str(prevMonth)+"-" in date:
            dateList.append(date)
    for i in dateList:
        currentDate=i.split("-")[2]
        currentDateList.append(currentDate)
    baseDate=dateList[0].split("-")[0]+"-"+dateList[1].split("-")[1]
    currentDateList.sort()
    fromDate=baseDate+"-"+str(currentDateList[0])
    toDate=baseDate+"-"+str(currentDateList[-1])
    return fromDate,toDate

def get_month_cpr(symbol):
    fromDate,toDate=get_first_last_date_prev_month()
    #print(symbol)
    tmpDate=fromDate.split("-")
    #fromDate=tmpDate[0]+"-"+tmpDate[1]+"-"+"0"+str(int(tmpDate[2])-1)
    #fromDate=fromDate+" 08:00:00"
    fromDate = fromDate+" 09:15:00"
    toDate=toDate+" 15:35:00"
    lowList=[]
    highList=[]
    #print(fromDate)
    #print(toDate)
    candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"day" , continuous=False, oi=False)
    for i in candle:
        lowList.append(i["low"])
        highList.append(i["high"])
    l=min(lowList)
    h=max(highList)
    c=candle[-1]["close"]
    center_pivot = (h+l+c)/3
    S1 =  (2 * center_pivot) - h
    S2 =  center_pivot - (h - l)
    R1 =  (2 * center_pivot) - l
    R2 =  center_pivot + (h - l)
    return R1,R2,center_pivot,S1,S2


def get_single_dic(symbol):
    # r1, r2 , cpr , s1 , s2 , 20ma , 40ma , 200ma
    imp_price = {}
    r1,r2,cpr,s1,s2=get_month_cpr(symbol)
    sma20,sma40,sma200 = get_ma(symbol,"day")
    imp_price["r1"]=r1
    imp_price["r2"]=r2
    imp_price["cpr"]=cpr
    imp_price["s1"]=s1
    imp_price["s2"]=s2
    imp_price["sma20"]=sma20
    imp_price["sma40"]=sma40
    imp_price["sma200"]=sma200

    return imp_price


def get_important_price_dictionary():
    # r1, r2 , cpr , s1 , s2 , 20ma , 40ma , 200ma
    important_price={}
    for symbol in NIFTYFNO:
        print(symbol)
        important_price[symbol]=get_single_dic(symbol)
    #print(important_price)
    return important_price 

def create_important_price_dic_file():
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename="important_price_"+str(date)
    if os.path.isfile(filename):
        update_important_price_dic_file(filename)
    else:
        os.system("rm important_price_*")
        imp_price_dic=get_important_price_dictionary()
        save_structure_to_file_wrapper(filename,imp_price_dic)

def get_microsec_to_wait():
    i=round(time.time() * 1000)
    j=i
    while True:
        j=j+1
        if j%1000 == 0:
            return (j-i)/1000

def handle_max_request():
    global gNumOfCall
    if gNumOfCall == 0:
        gNumOfCall=1
    elif gNumOfCall > 3:
        '''
        oTime = datetime.now()
        oTimeSec=oTime.second
        while True:
            nTime = datetime.now()
            nTimeSec=nTime.second
            if nTimeSec>oTimeSec:
                break
        '''
        oTime = datetime.now()
        oTimeSec=oTime.second
        print(oTimeSec)
        time.sleep(get_microsec_to_wait())
        nTime = datetime.now()
        nTimeSec=nTime.second
        print(nTimeSec)
        gNumOfCall=1
    else:
        gNumOfCall = gNumOfCall+1


def bull_bear_ma_order(lst):
    to_date=datetime.today().strftime('%Y-%m-%d')
    to_date=to_date+" 15:35:00"
    week_ago_2 = datetime.today() - relativedelta(days=14)
    from_date = week_ago_2.strftime('%Y-%m-%d') + " 00:00:00"
    sma_list=[]
    global global_high_low
    global mutex
    bull_bear_ma_order=[]
    for symbol in lst:
        print(symbol)
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
        mutex.acquire()
        handle_max_request()
        for i in candle:
            c=i["close"]
            sma_list.append(c)
        sma200 = sum(sma_list[-200:])/200
        sma40 = sum(sma_list[-40:])/40
        sma20 = sum(sma_list[-20:])/20
        if sma20>sma40>sma200 or sma20<sma40<sma200:
            if symbol not in global_high_low:
                bull_bear_ma_order.append(symbol)
        mutex.release()
    return bull_bear_ma_order 

def multithread_ma_order():
    base_index=0
    ma_order=[]
    NIFTYFNO_TOKEN=[]
    THREAD_LIST=[]
    global global_high_low
    while True:
        NIFTYFNO_TOKEN.append(NIFTYFNO[base_index:base_index+10])
        base_index=base_index+10
        if base_index>len(NIFTYFNO):
            #print(len(NIFTYFNO_TOKEN))
            break
    with concurrent.futures.ThreadPoolExecutor() as executor:
        time.sleep(get_microsec_to_wait())
        for token in NIFTYFNO_TOKEN:
            #THREAD_LIST.append(threading.Thread(target=print_historic_data, args=(token,)))
            THREAD_LIST.append(executor.submit(bull_bear_ma_order,token))
        for t in THREAD_LIST:
            return_value = t.result()
            ma_order.extend(return_value)
            t.done()
    #print(ma_order)
    if len(global_high_low) == 0:
        global_high_low.extend(ma_order)
        return []
    return ma_order

def get_update_dic():
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename_imp_price="important_price_"+str(date)
    base_ma_price="base_ma_"+str(date)
    imp_price_dic = load_structure_from_file(filename_imp_price)
    base_ma_dic = load_structure_from_file(base_ma_price)
    #print(base_ma_dic)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        c=ltp_dict[symbol]["last_price"]
        sma20 = (base_ma_dic[symbol]["sma19"]*19+c)/20
        sma40 = (base_ma_dic[symbol]["sma39"]*39+c)/40
        sma200 = (base_ma_dic[symbol]["sma199"]*199+c)/200
        imp_price_dic[symbol]["sma20"]=sma20
        imp_price_dic[symbol]["sma40"]=sma40
        imp_price_dic[symbol]["sma200"]=sma200
    return imp_price_dic

def update_important_price_dictionary():
    time = datetime.now()
    global old_minute
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename_imp_price="important_price_"+str(date)
    m=time.minute
    if os.path.isfile(filename_imp_price) == False:
        create_important_price_dic_file()
    elif  m != old_minute and m%15==0:
        date=date=datetime.today().strftime('%Y-%m-%d')
        filename="base_ma_"+str(date)
        filename_imp_price="important_price_"+str(date)
        if os.path.isfile(filename):
            updated_dic = get_update_dic()
            os.system("rm important_price_*")
            save_structure_to_file_wrapper(filename_imp_price,updated_dic)
            old_minute=m
        else:
            os.system("rm base_ma_*")
            create_base_ma_file()
            update_important_price_dictionary()

def get_n_day_ago_date(timeframe):
    if timeframe == "5minute":
        week_ago_2 = datetime.today() - relativedelta(days=14)
        from_date = week_ago_2.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "day":
        day_ago_400 = datetime.today() - relativedelta(days=400)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "hour":
        day_ago_400 = datetime.today() - relativedelta(days=400)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date
    elif timeframe == "month":
        day_ago_400 = datetime.today() - relativedelta(months=4)
        from_date = day_ago_400.strftime('%Y-%m-%d') + " 00:00:00"
        return from_date

def create_base_ma_file():
    timeframe="day"
    date=datetime.today().strftime('%Y-%m-%d')
    filename="base_ma_"+date
    base_ma_dic={}
    ma_dic={}
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date(timeframe)
    for symbol in NIFTYFNO:
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
        sma_list=[]
        for i in candle:
            c=i["close"]
            sma_list.append(c)
        sma199 = sum(sma_list[-199:])/199
        sma39 = sum(sma_list[-39:])/39
        sma19 = sum(sma_list[-19:])/19
        ma_dic["sma19"]=sma19
        ma_dic["sma39"]=sma39
        ma_dic["sma199"]=sma199
        base_ma_dic[symbol]=ma_dic
    #print(base_ma_dic)
    save_structure_to_file_wrapper(filename,base_ma_dic)

def last_3_day_red(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("5minute")
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"day", continuous=False, oi=False)
    if candle[-2]["close"] < candle[-2]["open"] and candle[-3]["close"] < candle[-3]["open"] and candle[-4]["close"] < candle[-4]["open"] :
        return True
    else:
        return False

def last_3_day_green(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("5minute")
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"day", continuous=False, oi=False)
    if candle[-2]["close"] > candle[-2]["open"] and candle[-3]["close"] > candle[-3]["open"] and candle[-4]["close"] > candle[-4]["open"] :
        return True
    else:
        return False

def top_gainer_modified():
    topg=top_gainer()
    lst = []
    for symbol in topg:
        if last_3_day_red(symbol) == True:
           lst.append(symbol) 
    return lst

def top_looser_modified():
    topl=top_looser()
    lst = []
    for symbol in topl:
        if last_3_day_green(symbol) == True:
           lst.append(symbol) 
    return lst

def new_day_high_modified():
    newh=new_day_high(NIFTYFNO)
    lst = []
    for symbol in newh:
        if last_3_day_red(symbol) == True:
           lst.append(symbol)
    return lst

def new_day_low_modified():
    newl=new_day_low(NIFTYFNO)
    lst = []
    for symbol in newl:
        if last_3_day_green(symbol) == True:
           lst.append(symbol)
    return lst


def test():
    for symbol in NIFTYFNO:
        if last_3_day_green(symbol) == True:
            print(symbol)


def get_ma(symbol,timeframe):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date(timeframe)
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200:])/200
    sma40 = sum(sma_list[-40:])/40
    sma20 = sum(sma_list[-20:])/20
    return sma20,sma40,sma200

def get_ma_candle(candle):
    '''
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date(timeframe)
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
    '''
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200:])/200
    #sma40 = sum(sma_list[-40:])/40
    sma20 = sum(sma_list[-20:])/20
    return sma20,sma200


def get_ma_flash(symbol,ltp_dict):
    #ltp_dict=get_ltp_dict(NIFTYFNO)
    c=ltp_dict[symbol]["last_price"]
    ma20 = ((sma19[symbol]*19)+c)/20
    ma200 = ((sma199[symbol]*199)+c)/200
    return ma20,ma200

def secondary_check_ma20_bull(symbol):
    ma20,h1,l1,c1,h2,l2=yesterday_20ma_ohlc(symbol)
    if c1>ma20 and l1>l2 and h1>h2:
        return True
def secondary_check_ma20_bear(symbol):
    ma20,h1,l1,c1,h2,l2=yesterday_20ma_ohlc(symbol)
    if c1<ma20 and l1<l2 and h1<h2:
        return True
def secondary_check_ma200_bull(symbol):
    ma200,h1,l1,c1,h2,l2=yesterday_200ma_ohlc(symbol)
    if c1>ma200 and l1>l2 and h1>h2:
        return True
def secondary_check_ma200_bear(symbol):
    ma200,h1,l1,c1,h2,l2=yesterday_20ma_ohlc(symbol)
    if c1<ma200 and l1<l2 and h1<h2:
        return True

def algo_trade():
    ltp_dict=get_ltp_dict(NIFTYFNO)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    lst=[]
    for symbol in NIFTYFNO:
        sma20,sma200=get_ma_flash(symbol,ltp_dict)
        l=ohlc_dict[symbol]["ohlc"]["low"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        c=ltp_dict[symbol]["last_price"]
        if c<=sma20 and h>=sma20 and ((sma20-h)/sma20)*100 >= -0.05 and ((c-sma20)/sma20)*100>=-0.2:
            print(symbol)
            print(sma20)
            #if secondary_check_ma20_bear(symbol) == True:
            lst.append(symbol)
        if c>=sma20 and l<=sma20 and ((sma20-l)/sma20)*100 <= 0.05 and ((c-sma20)/sma20)*100<=0.2:
            print(symbol)
            print(sma20)
            #if secondary_check_ma20_bull(symbol) == True:
            lst.append(symbol)
        if c<=sma200 and h>=sma200 and ((sma200-h)/sma200)*100 >= -0.05 and ((c-sma200)/sma200)*100>=-0.2:
            print(symbol)
            print(sma200)
            #if secondary_check_ma200_bear(symbol) == True:
            lst.append(symbol)
        if c>=sma200 and l<=sma200 and ((sma200-l)/sma200)*100 <= 0.05 and ((c-sma200)/sma200)*100<=0.2:
            print(symbol)
            print(sma200)
            #if secondary_check_ma200_bull(symbol) == True:
            lst.append(symbol)
    return lst

def algo_trade_915():
    ltp_dict=get_ltp_dict(NIFTYFNO)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    lst=[]
    print("1")
    for symbol in NIFTYFNO:
        sma20,sma200=get_ma_flash(symbol,ltp_dict)
        l=ohlc_dict[symbol]["ohlc"]["low"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ltp_dict[symbol]["last_price"]
        if h>sma20 and o>sma20 and l<sma20 and c>o and symbol not in global_high_low:
            lst.append(symbol)
            print("2")
            print(sma20)
        if h>sma200 and o>sma200 and l<sma200 and c>o and symbol not in global_high_low:
            lst.append(symbol)
            print("3")
            print(sma20)
        if l<sma20 and o<sma20 and h>sma20 and c<o and symbol not in global_high_low:
            lst.append(symbol)
            print("4")
            print(sma200)
        if l<sma200 and o<sma200 and h>sma200 and c<o and symbol not in global_high_low:
            lst.append(symbol)
            print("5")
            print(sma200)
    return lst

def yesterday_200ma_ohlc(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("day")
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"day", continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-201:-1])/200
    h1=candle[-2]["high"]
    l1=candle[-2]["low"]
    c1=candle[-2]["close"]
    h2=candle[-3]["high"]
    l2=candle[-3]["low"]
    print(sma200)
    return sma200,h1,l1,c1,h2,l2

def yesterday_20ma_ohlc(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("day")
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"day", continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma20 = sum(sma_list[-21:-1])/20
    h1=candle[-2]["high"]
    l1=candle[-2]["low"]
    c1=candle[-2]["close"]
    h2=candle[-3]["high"]
    l2=candle[-3]["low"]
    print(sma20)
    return sma20,h1,l1,c1,h2,l2

def get_200ma_min5_nCandle_ago(candle,n):
    #date=date=datetime.today().strftime('%Y-%m-%d')
    #to_date=date+" 15:35:00"
    #from_date=get_n_day_ago_date("5minute")
    #candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200-n:0-n])/200
    print(sma200)
    return sma200

def get_20_200ma_min5_nCandle_ago(candle,n):
    #date=date=datetime.today().strftime('%Y-%m-%d')
    #to_date=date+" 15:35:00"
    #from_date=get_n_day_ago_date("5minute")
    #candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200-n:0-n])/200
    sma20 = sum(sma_list[-20-n:0-n])/20
    print(sma200)
    return sma20,sma200


def get_ohlc_min5_nCandle_ago(candle,n):
    #date=date=datetime.today().strftime('%Y-%m-%d')
    #to_date=date+" 15:35:00"
    #from_date=get_n_day_ago_date("5minute")
    #candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
    sma_list=[]
    n=n+1
    o=candle[-n]["open"]
    h=candle[-n]["high"]
    l=candle[-n]["low"]
    c=candle[-n]["close"]
    print(o)
    print(h)
    print(l)
    print(c)
    return o,h,l,c

def past_n_candle_notbw_200ma(candle,n):
    for i in range(n):
        o,h,l,c=get_ohlc_min5_nCandle_ago(candle,i)
        sma200=get_200ma_min5_nCandle_ago(candle,i)
        if l<sma200<h:
            return False
    return True

def price_cross_200ma_min5():
    lst=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    returnlst = []
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("5minute")
    for symbol in lst:
        sma20,sma40,sma200=get_ma(symbol,"5minute")
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
        o=candle[-1]["open"]
        h=candle[-1]["high"]
        l=candle[-1]["low"]
        c=candle[-1]["close"]
        if l<sma200<h:
            if past_n_candle_notbw_200ma(candle,20):
                returnlst.append(symbol)
    return returnlst

def ma_order_bull(lst):
    orderlst=[]
    for symbol in lst:
        ma20,ma40,ma200 = get_ma(symbol,"5minute")
        if ma20>ma40>ma200 and symbol not in global_high_low:
            orderlst.append(symbol)
            print(symbol)
        else:
            continue
    return orderlst

def ma_order_bear(lst):
    orderlst=[]
    for symbol in lst:
        ma20,ma40,ma200 = get_ma(symbol,"5minute")
        if ma20<ma40<ma200 and symbol not in global_high_low:
            orderlst.append(symbol)
            print(symbol)
        else:
            continue
    return orderlst

def new_high_ma():
        symbol_lst = new_day_high(NIFTYFNO)
        tmp_lst = []
        ohlc_dict=get_ohlc_dict(NIFTYFNO)
        for symbol in symbol_lst:
                sma20,sma40,sma200 = get_ma(symbol,"day")
                print(symbol)
                print(sma20)
                print(sma40)
                print(sma200)
                o=ohlc_dict[symbol]["ohlc"]["open"]
                l=ohlc_dict[symbol]["ohlc"]["low"]
                if o>sma20 and l<sma20:
                        tmp_lst.append(symbol)
                if o>sma40 and l<sma40:
                        tmp_lst.append(symbol)
                if o>sma200 and l<sma200:
                        tmp_lst.append(symbol)
        return tmp_lst

def new_low_ma():
        symbol_lst = new_day_low(NIFTYFNO)
        
        tmp_lst = []
        ohlc_dict=get_ohlc_dict(NIFTYFNO)
        for symbol in symbol_lst:
                sma20,sma40,sma200 = get_ma(symbol,"day")
                print(symbol)
                print(sma20)
                print(sma40)
                print(sma200)
                o=ohlc_dict[symbol]["ohlc"]["open"]
                h=ohlc_dict[symbol]["ohlc"]["high"]
                if o<sma20 and h>sma20:
                        tmp_lst.append(symbol)
                if o<sma40 and h>sma40:
                        tmp_lst.append(symbol)
                if o<sma200 and h>sma200:
                        tmp_lst.append(symbol)
        return tmp_lst

def morning_stratagy():
    #new_high=new_day_high(NIFTYFNO)
    new_high,new_low,ohlc_dict,ltp_dict = new_high_low()
    #top_g=top_gainer()
    #top_l=top_looser()
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename="important_price_"+str(date)
    imp_price_dic = load_structure_from_file(filename)
    #print(new_high)
    if len(new_high)>0:
        #ohlc_dict=get_ohlc_dict(new_high)
        #ltp_dict=get_ltp_dict(new_high)
        for symbol in new_high:
            c=ltp_dict[symbol]["last_price"]
            o=ohlc_dict[symbol]["ohlc"]["open"]
            l=ohlc_dict[symbol]["ohlc"]["low"]
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["r1"],c,o,l)
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["r2"],c,o,l)
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["s1"],c,o,l)
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["s2"],c,o,l)
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["cpr"],c,o,l)
            check_bull_buy_signal(symbol,imp_price_dic[symbol]["sma20"],c,o,l)
            #check_bull_buy_signal(symbol,imp_price_dic[symbol]["sma40"],c,o,l)
            check_bull_buy_signal(symbol,imp_price_dic[symbol]["sma200"],c,o,l)
    #new_low=new_day_low(NIFTYFNO)
    #print(new_low)
    if len(new_low)>0:
        #ohlc_dict=get_ohlc_dict(new_low)
        #ltp_dict=get_ltp_dict(new_low)
        for symbol in new_low:
            c=ltp_dict[symbol]["last_price"]
            o=ohlc_dict[symbol]["ohlc"]["open"]
            h=ohlc_dict[symbol]["ohlc"]["high"]
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["r1"],c,o,h)
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["r2"],c,o,h)
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["s1"],c,o,h)
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["s2"],c,o,h)
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["cpr"],c,o,h)
            check_bear_sell_signal(symbol,imp_price_dic[symbol]["sma20"],c,o,h)
            #check_bear_sell_signal(symbol,imp_price_dic[symbol]["sma40"],c,o,h)
            check_bear_sell_signal(symbol,imp_price_dic[symbol]["sma200"],c,o,h)

def backtest():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename="important_price_"+str(date)
    imp_price_dic = load_structure_from_file(filename)
    symbol_list=[]
    for symbol in NIFTYFNO:
        c=ltp_dict[symbol]["last_price"]
        o=ohlc_dict[symbol]["ohlc"]["open"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["r1"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["r2"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["s1"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["s2"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["cpr"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["sma20"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["sma40"],h,l):
            symbol_list.append(symbol)
        if is_price_between_high_low(symbol,imp_price_dic[symbol]["sma200"],h,l):
            symbol_list.append(symbol)
    return list(set(symbol_list))

def is_price_between_high_low(symbol,price,h,l):
    if l<=price<=h:
        return True

def is_ma_between_high_low(symbol,timeframe,o,h,l,c,ltp_dict):
    global global_cross_ma20
    global global_cross_ma200
    global firsttime
    sma20,sma200 = get_ma_flash(symbol,ltp_dict)
    c=ltp_dict[symbol]["last_price"]
    retbool = False
    #print(global_cross_ma20)
    #print(global_cross_ma200)
    if firsttime:
        print("first time")
        if l<=sma20<=h and symbol not in global_cross_ma20:
            global_cross_ma20.append(symbol)
            print(symbol)
            print(sma20)
            save_structure_to_file_wrapper("global_cross_ma20",global_cross_ma20)
            retbool = True
        if l<=sma200<=h and symbol not in global_cross_ma200:
            global_cross_ma200.append(symbol)
            print(symbol)
            print(sma200)
            save_structure_to_file_wrapper("global_cross_ma200",global_cross_ma200)
            retbool = True
    elif l<=sma20<=h and symbol not in global_cross_ma20 and (c-(c/200))<=sma20<=(c+(c/200)):
        print("second time onward")
        if (c>o and redCandle[symbol]>=5) or (c<o and greenCandle[symbol] >= 5):
            global_cross_ma20.append(symbol)
            print(symbol)
            print(sma20)
            save_structure_to_file_wrapper("global_cross_ma20",global_cross_ma20)
            play_sound()
            save_screenshot_stock(symbol)
            exit()
            retbool = True
    elif l<=sma200<=h and symbol not in global_cross_ma200 and (c-(c/200))<=sma200<=(c+(c/200)):
        if (c>o and redCandle[symbol]>=5) or (c<o and greenCandle[symbol] >= 5):
            global_cross_ma200.append(symbol)
            print(symbol)
            print(sma200)
            save_structure_to_file_wrapper("global_cross_ma200",global_cross_ma200)
            play_sound()
            save_screenshot_stock(symbol)
            exit()
            retbool = True
    return retbool 

def is_ma_between_open_close(symbol,timeframe,o,h,l,c,ltp_dict):
    global global_cross_ma20
    global global_cross_ma200
    sma20,sma200 = get_ma_flash(symbol,ltp_dict)
    lst=[]
    retbool = False
    if o<=sma20<=c and symbol not in global_cross_ma20:
        global_cross_ma20.append(symbol)
        print(symbol)
        print(sma20)
        retbool = True
    if o<=sma200<=c and symbol not in global_cross_ma200:
        global_cross_ma200.append(symbol)
        print(symbol)
        print(sma200)
        retbool = True
    return retbool

def check_bull_buy_signal(symbol,imp_price,ltp,open_price,low):
    #only for stock made new high
    if low > (ltp - (ltp/100)) and low<=imp_price<=ltp and open_price>=imp_price and  symbol not in global_high_low :
        print(symbol)
        print("yes")
        global_high_low.append(symbol)

def check_bear_sell_signal(symbol,imp_price,ltp,open_price,high):
    #only for stock made new high
    if high < (ltp + (ltp/100)) and ltp<=imp_price<=high and open_price<=imp_price and symbol not in global_high_low:
        print(symbol)
        global_high_low.append(symbol)
        print("yes")

def stock_crossed_ma():
    stockList = []
    global firsttime
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    global globa_cross_ma20
    global globa_cross_ma200
    #if len(global_cross_ma20)==0 or len(global_cross_ma200)==0:
    if firsttime==True:
        print("in if case")
        for symbol in NIFTYFNO:
            o=ohlc_dict[symbol]["ohlc"]["open"]
            h=ohlc_dict[symbol]["ohlc"]["high"]
            l=ohlc_dict[symbol]["ohlc"]["low"]
            #c=ohlc_dict[symbol]["ohlc"]["close"]
            c=ltp_dict[symbol]["last_price"]
            if is_ma_between_high_low(symbol,"day",o,h,l,c,ltp_dict)==True:
                stockList.append(symbol)
        #return stockList
        firsttime=False
        return []
    else:
        print("in else case")
        for symbol in NIFTYFNO:
            o=ohlc_dict[symbol]["ohlc"]["open"]
            h=ohlc_dict[symbol]["ohlc"]["high"]
            l=ohlc_dict[symbol]["ohlc"]["low"]
            #c=ohlc_dict[symbol]["ohlc"]["close"]
            c=ltp_dict[symbol]["last_price"]
            if is_ma_between_high_low(symbol,"day",o,h,l,c,ltp_dict) ==  True:
                stockList.append(symbol)
        return stockList

def stock_form_bw_ma():
    stockList = []
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    global globa_cross_ma20
    global globa_cross_ma200
    if len(global_cross_ma20)==0 or len(global_cross_ma200)==0:
        for symbol in NIFTYFNO:
            o=ohlc_dict[symbol]["ohlc"]["open"]
            h=ohlc_dict[symbol]["ohlc"]["high"]
            l=ohlc_dict[symbol]["ohlc"]["low"]
            #c=ohlc_dict[symbol]["ohlc"]["close"]
            c=ltp_dict[symbol]["last_price"]
            if is_ma_between_high_low(symbol,"day",o,h,l,c,ltp_dict)==True:
                stockList.append(symbol)
    return stockList

def is_5min_day_high(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    from_date=date+" 00:00:00"
    to_date=date+" 15:35:00"
    high_list=[]
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute" , continuous=False, oi=False)
    for i in candle:
        h=i["high"]
        high_list.append(h)
    if h == max(high_list):
        return True
    else:
        return False

def is_5min_day_low(symbol):
    date=date=datetime.today().strftime('%Y-%m-%d')
    from_date=date+" 00:00:00"
    to_date=date+" 15:35:00"
    low_list=[]
    candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute" , continuous=False, oi=False)
    for i in candle:
        l=i["low"]
        low_list.append(l)
    if l == min(low_list):
        return True
    else:
        return False

def custom_sleep(n):
    while n:
        custom_sleep_1sec()
        n=n-1

def custom_sleep_1sec():
    i=10
    while i:
        pyautogui.click(400,120)
        time.sleep(0.1)
        i=i-1

def get_ohlc_dict(fnolist):
    '''
    fnolistnse = []
    for i in fnolist:
        tmp_symbol="NSE:"+i
        fnolistnse.append(tmp_symbol)
    #print(fnolistnse)
    '''
    ohlc_dict=kite.ohlc(fnolist)
    #print(ohlc_dict)
    return ohlc_dict

def get_ltp_dict(fnolist):
    '''
    fnolistnse = []
    for i in fnolist:
        tmp_symbol="NSE:"+i
        fnolistnse.append(tmp_symbol)
    #print(fnolistnse)
    '''
    ltp_dict=kite.ltp(fnolist)
    #print(ohlc_dict)
    return ltp_dict

def sentiment():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    total=len(NIFTYFNO)
    cnt=0
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #print(c)
        #print(o)
        if c>o:
            #print(symbol)
            cnt=cnt+1
            #print(cnt)
    fraction=cnt/total
    fraction=(int(fraction*100)/100)
    print("sentiment")
    print(fraction)
    return fraction

def is_trading_near_day_low(symbol):
    ohlc_dict = get_ohlc_dict(list(symbol))
    o=ohlc_dict[symbol]["ohlc"]["open"]
    l=ohlc_dict[symbol]["ohlc"]["low"]
    c=ohlc_dict[symbol]["last_price"]

    if c<(l-(l/10)):
        return True

def get_list_trading_near_day_xxx():
    trading_near={}
    trading_near_day_high=[]
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        trading_near[symbol]=(c/h)
    x=sorted(trading_near.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    trading_near_day_high=new_list[:10]
    trading_near_day_low=new_list[-10:]
    return trading_near_day_high,trading_near_day_low

def change_timeframe():
    time.sleep(1)
    pyautogui.click(760,127)
    time.sleep(1)
    pyautogui.click(750,280)
    time.sleep(3)
    pyautogui.click(760,127)
    time.sleep(3)
    pyautogui.click(760,410)
    time.sleep(3)

def get_list_trading_near_day_high():
    trading_near_day_high=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        if c>h-((h-l)/10) and is_5min_day_high(symbol) == False:
            trading_near_day_high.append(symbol)

    return trading_near_day_high

def get_list_trading_near_day_low():
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        if c<l+((h-l)/10) and is_5min_day_low(symbol) == False:
            trading_near_day_low.append(symbol)
    return trading_near_day_low

    '''
    ohlc_dict = get_ohlc_dict(list(symbol))
    o=ohlc_dict[symbol]["ohlc"]["open"]
    l=ohlc_dict[symbol]["ohlc"]["low"]
    c=ohlc_dict[symbol]["last_price"]

    if c>(h-(h/10)):
        return True
    '''

'''
def stock_trading_near_day_low():
def stock_trading_near_day_high():
'''

def close_eq_low():
    trading_near_day_low=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if c==l:
            trading_near_day_low.append(symbol)
        return trading_near_day_low

def close_eq_high():
    trading_near_day_high=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if c==h:
            trading_near_day_high.append(symbol)
        return trading_near_day_high

def stock_after_correction():
    new_day_high(NIFTYFNO)
    new_day_low(NIFTYFNO)
    time.sleep(60)
    first_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    time.sleep(60)
    second_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    new_fno_list = list(set(first_list) - set(second_list))
    time.sleep(60)
    second_list=new_day_high(new_fno_list)+new_day_low(new_fno_list)
    print(second_list)

def new_day_high(NIFTYFNO):
    new_day_high_list=[]
    new_day_high_per_change={}
    global golbal_high_low
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    if bool(new_day_high_dic) == False:
        for symbol in NIFTYFNO:
            new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
    else:
        for symbol in NIFTYFNO:
            #print(symbol)
            #print(new_day_high_dic[symbol])
            #print(ohlc_dict[symbol]["ohlc"]["high"])
            if new_day_high_dic[symbol]<ohlc_dict[symbol]["ohlc"]["high"] and symbol not in global_high_low:
                new_day_high_list.append(symbol)
                new_day_high_per_change[symbol]= ((ohlc_dict[symbol]["ohlc"]["close"] - new_day_high_dic[symbol])/new_day_high_dic[symbol])
                new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
    
    x=sorted(new_day_high_per_change.items(), key=lambda item: item[1])
    #print(x)
    new_list = [ seq[0] for seq in x ]
    new_list.reverse()
    top_day_high_by_change=new_list[0:5]
    #print(new_day_high_list)
    #x=is_ma_order_bull(top_day_high_by_change)
    #return x
    #return top_day_high_by_change
    return new_day_high_list

def new_day_low(NIFTYFNO):
    new_day_low_list=[]
    new_day_low_per_change={}
    global golbal_high_low
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    if bool(new_day_low_dic) == False:
        for symbol in NIFTYFNO:
            new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
    else:
        for symbol in NIFTYFNO:
            if new_day_low_dic[symbol]>ohlc_dict[symbol]["ohlc"]["low"] and symbol not in global_high_low:
                new_day_low_list.append(symbol)
                new_day_low_per_change[symbol]= ((ohlc_dict[symbol]["ohlc"]["close"] - new_day_low_dic[symbol])/new_day_low_dic[symbol])
                new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
   
    y=sorted(new_day_low_per_change.items(), key=lambda item: item[1])
    #print(x)
    new_list = [ seq[0] for seq in y ]
    #new_list.reverse()
    top_day_low_by_change=new_list[0:5]
    #x=is_ma_order_bear(top_day_low_by_change)
    #return x
    return new_day_low_list


def get_list_top_day_moribozu():
    day_moribozu_dict={}
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        day_moribozu_dict[symbol]=(abs(c-o)/(h-l))
    x=sorted(day_moribozu_dict.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    new_list.reverse()
    top_day_moribozu=new_list[0:10]
    print(top_day_moribozu)
    return top_day_moribozu

def get_list_top_day_moribozu_by_thersold():
    day_moribozu_dict={}
    day_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        factor=(abs(c-o)/(h-l))
        if factor > 0.97 and factor < 0.99:
            day_moribozu_list.append(symbol)
    return day_moribozu_list

def bull_side_moribozu():
    bull_moribozu_dict={}
    bull_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    top_g=top_gainer()
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #if c>o  and ((c-o)/(h-o))>0.9 and ((c-o)/(h-o))<0.99 and symbol in top_g:
        if c>o  and ((c-o)/(h-o))>0.97 and ((c-o)/(h-o))<0.998 and symbol not in global_high_low:
            bull_moribozu_list.append(symbol)
    return bull_moribozu_list

def bear_side_moribozu():
    bear_moribozu_dict={}
    bear_moribozu_list=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    top_l=top_looser()
    for symbol in NIFTYFNO:
        print(symbol)
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        #if o>c  and ((o-c)/(o-l))>0.9 and ((o-c)/(o-l))<0.99 and symbol in top_l:
        if o>c  and ((o-c)/(o-l))>0.97 and ((o-c)/(o-l))<0.998 and symbol not in global_high_low :
            bear_moribozu_list.append(symbol)
    return bear_moribozu_list


def get_per_change_dic_abs(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=(abs(c-o)/o)*100
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change


def get_per_change_dic(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change

def get_per_change_dic_morning(ohlc_dict):
    per_change={}
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            if per>1 or per<1:
                per=0
            per_change[symbol]=per
        except:
            continue

        #print(ohlc_dict[symbol])
    return per_change

def less_than_by_n_per(n):
    lst=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            if per<n:
                lst.append(symbol)
        except:
            continue
    return lst

def greater_than_by_n_per(n):
    lst=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["last_price"]
        try:
            per=((c-o)/o)*100
            if per>n:
                lst.append(symbol)
        except:
            continue
    return lst

def common_element(lst1,lst2):
    return list(set(lst1)&set(lst2))

def momentum_gainer():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    top_plus=[]
    top_minus=[]
    old_price={}
    momentum_dic={}
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        old_price[symbol]=c

    time.sleep(5)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        if old_price[symbol]/c > 1.002:
            top_plus.append(symbol)            		
        if old_price[symbol]/c < 0.008:
            top_plus.append(symbol)            		
    
    return top_plus+top_minus

def top_momentum():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    old_price={}
    momentum_dic={}
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        old_price[symbol]=c

    time.sleep(5)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in ohlc_dict.keys():
        #o=ohlc_dict[symbol]["ohlc"]["open"]
        #h=ohlc_dict[symbol]["ohlc"]["high"]
        #l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["last_price"]
        momentum_dic[symbol]= (old_price[symbol]/c)
   
    x=sorted(momentum_dic.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    top_plus=new_list[:2]
    top_minus=new_list[-2:]

    print(top_plus)
    print(top_minus)

        #print(ohlc_dict[symbol])
    return top_plus+top_minus

def top_gainer():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    res = nlargest(20, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res

def top_gainer_looser():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic_abs(kite_ohlc_dict)
    res = nlargest(20, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res


def manual_wait(stock):
    with keyboard.Events() as events:
        event = events.get(300.0)
        if str(event) == "Press(key='e')":
            os._exit(1)
        if str(event) == "Press(key='c')":
            print(stock)

def top_looser():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic(kite_ohlc_dict)
    #print(per_change)
    res = nsmallest(20, per_change, key = per_change.get)
    #res.reverse()
    return res

def top_gainer_morning():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic_morning(kite_ohlc_dict)
    res = nlargest(10, per_change, key = per_change.get)
    #res.reverse()
    #print(res)
    return res

def top_looser_morning():
    kite_ohlc_dict=get_ohlc_dict(NIFTYFNO)
    per_change=get_per_change_dic_morning(kite_ohlc_dict)
    #print(per_change)
    res = nsmallest(5, per_change, key = per_change.get)
    #res.reverse()
    return res


def monitor_top_gainer():
    global already_top_gainer
    if len(already_top_gainer) == 0:
        already_top_gainer = top_gainer()
    new_top_gainer = top_gainer()
    new_element_enter = list(set(new_top_gainer) - set(already_top_gainer))
    print(new_element_enter)
    if len(new_element_enter) > 0:
        already_top_gainer.clear()
        already_top_gainer = new_top_gainer[:]
        print('buy signal...')
        print(datetime.datetime.now().time())
        print(new_element_enter[-1])
        return True
    return False

def monitor_top_looser():
    global already_top_looser
    if len(already_top_looser) == 0:
        already_top_looser = top_looser()
    new_top_looser = top_looser()
    new_element_enter = list(set(new_top_looser) - set(already_top_looser))
    print('already top looser...')
    print(already_top_looser)
    print('new top looser...')
    print(new_top_looser)
    print(new_element_enter)
    if len(new_element_enter) > 0:
        already_top_looser.clear()
        already_top_looser = new_top_looser[:]
        if is_trading_near_day_low(new_element_enter[-1]):
            print('sell signal...')
            print(datetime.datetime.now().time())
            print(new_element_enter[-1])
            return True
    return False

def save_screenshot_stock(stock):
    pyautogui.moveTo(166,122)
    pyautogui.click(clicks=2)
    if "HDFC" in stock:
        stock = stock.replace('NSE:','')
        time.sleep(2)
        print(stock)
        #custom_sleep(2)
    if "ICICIGI" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        time.sleep(2)
        #custom_sleep(2)
    if "CUB" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        time.sleep(2)
        #custom_sleep(2)
    if "RAIN" in stock:
        stock = stock.replace('NSE:','')
        time.sleep(2)
        print(stock)
        #custom_sleep(2)
    if "LT" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        time.sleep(2)
        #custom_sleep(2)
    if "INDIGO" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        #custom_sleep(2)
        time.sleep(2)
    print(stock)
    time.sleep(1)
    pyautogui.typewrite(stock)
    #custom_sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(167,206)
    #pyautogui.typewrite(["enter"])
    time.sleep(1)
    now = datetime.now()
    timenow = now.strftime("%H:%M:%S")
    #time.sleep(2)
    #play_sound()
    #custom_sleep(1)
    #call_option,put_option=get_call_put_option(stock.replace('NSE:',''),"25-Aug-2022","AUG","22")
    #print(call_option)
    #print(put_option)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("/home/pankaj/Pictures/"+stock+"_"+timenow+".png", image)
    #change_timeframe()

def save_screenshot(top_list):
    for stock in top_list:
        save_screenshot_stock(stock)
        #save_screenshot_zebro(stock)
        time.sleep(1)
        '''
        pyautogui.click(645,118)

        with keyboard.Events() as events:
            event = events.get(300.0)
            if event is None:
                continue
            else:
                if str(event) == "Press(key='e')":
                    os._exit(1)
                if str(event) == "Press(key='c')":
                    continue

        '''
        '''
        pyautogui.click(470,45)
        save_screenshot_stock(stock)
        time.sleep(2)
        pyautogui.click(295,40)
        pyautogui.click(166,122)
        if "HDFC" in stock:
            stock = stock.replace('NSE:','')
            time.sleep(1)
            print(stock)
            #custom_sleep(2)
        if "ICICIGI" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            time.sleep(2)
            #custom_sleep(2)
        if "CUB" in stock:
            time.sleep(1)
            stock = stock.replace('NSE:','')
            print(stock)
            time.sleep(2)
            custom_sleep(2)
        if "RAIN" in stock:
            stock = stock.replace('NSE:','')
            time.sleep(2)
            print(stock)
            custom_sleep(2)
        if "LT" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            custom_sleep(2)
            time.sleep(2)
        print(stock)
        time.sleep(1)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #custom_sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(1)
        #custom_sleep(1)
        #call_option,put_option=get_call_put_option(stock.replace('NSE:',''),"25-Aug-2022","AUG","22")
        #print(call_option)
        #print(put_option)
        #image = pyautogui.screenshot()
        #image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        #cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)
        #change_timeframe()
        '''

def get_time_to_wait():
    time = datetime.now()
    s=time.second
    m=time.minute
    r=0

    while m%5 != 0:
        m=m+1

    if time.minute>=m-1 and time.minute<m:
        print("in first case")
        r=(60-time.second) + 240
        return r
    else:
        print("in second case")
        r=(((m-time.minute)-2)*60 + (60-time.second))
        return r

def wait_for_5min():
    time = datetime.now()
    s=time.second
    m=time.minute
    curm=m
    if m%5==0:
        m=m+1
    while m%5 != 0:
        m=m+1
    m=(m-curm)-1
    sleft = 60-s
    mleft = m*60
    tleft = sleft+mleft
    print(tleft)
    return tleft

def wait_for_1min():
    time = datetime.now()
    s=time.second
    sleft = 60-s
    return sleft

def get_time_to_wait_roc():
    time = datetime.now()
    s=time.second
    m=time.minute
    r=0

    while m%5 != 0:
        m=m+1

    if time.minute>=m-1 and time.minute<m:
        print("in first case")
        r=(60-time.second) + 240
        return r
    else:
        print("in second case")
        r=(((m-time.minute)-2)*60 + (60-time.second))
        return r


def save_screenshot_zebro(stock):
    pyautogui.click(1450,93)
    pyautogui.typewrite(stock)
    time.sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(1470,180)
    #pyautogui.typewrite(["enter"])
    time.sleep(2)


def is_nifty_green():
    nifty_dict = kite.ohlc('NSE:NIFTY 50')
    print(nifty_dict)
    o=nifty_dict['NSE:NIFTY 50']["ohlc"]["open"]
    h=nifty_dict['NSE:NIFTY 50']["ohlc"]["high"]
    l=nifty_dict['NSE:NIFTY 50']["ohlc"]["low"]
    c=kite.ltp('NSE:NIFTY 50')['NSE:NIFTY 50']["last_price"]

    if c>o:
        return True
    else:
        return False

def play_sound():
    duration = 0.2  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    time.sleep(3)

def clear_global_list():
    time = datetime.now()
    global global_high_low_flag
    m=time.minute

    if m%3 == 0 and global_high_low_flag == 0:
        global_high_low.clear()
        global_high_low_flag = 1
    if m%3 != 0 and global_high_low_flag == 1:
        global_high_low_flag = 0

def new_high_with_20ma():
    lst=[]
    new_high=new_day_high(NIFTYFNO)
    sma20,sma40,sma200 = get_ma(symbol,"day")
    ohlc_dict=get_ohlc_dict(NIFTYFNO)

    for symbol in new_high:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o>sma20 and l<sma20:
            lst.append(symbol)

    return lst

def new_low_with_20ma():
    lst=[]
    new_low=new_day_low(NIFTYFNO)
    sma20,sma40,sma200 = get_ma(symbol,"day")
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in new_high:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o<sma20 and h>sma20:
            lst.append(symbol)
    return lst

def top_gainer_with_20ma():
    lst=[]
    topg=top_gainer()
    sma20,sma40,sma200 = get_ma(symbol,"day")
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in new_high:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o>sma20 and l<sma20:
            lst.append(symbol)
    return lst

def top_looser_with_20ma():
    lst=[]
    sma20,sma40,sma200 = get_ma(symbol,"day")
    topl=top_looser()
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in new_high:
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o<sma20 and h>sma20:
            lst.append(symbol)
    return lst

def manual_create_dic():
    date=date=datetime.today().strftime('%Y-%m-%d')
    filename="important_price_"+str(date)
    if os.path.isfile("base_ma_"+date) == False:
        os.system("rm base_ma_*")
        create_base_ma_file()
    if os.path.isfile("important_price_"+date) == False:
        os.system("rm important_price_*")
        #create_base_ma_file()
        imp_price_dic=get_important_price_dictionary()
        save_structure_to_file_wrapper(filename,imp_price_dic)

def new_high_low_old():
    bull_trend=sentiment()
    if bull_trend>0.6:
        return new_day_high(NIFTYFNO)
    elif bull_trend<0.4:
        return new_day_low(NIFTYFNO)
    else:
        print("#### DONT TRADE RANGING MARKET ####")
        return []

def new_high_low():
    new_day_high_list=[]
    new_day_low_list=[]
    global golbal_high_low
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    if bool(new_day_high_dic) == False and bool(new_day_low_dic) == False:
        for symbol in NIFTYFNO:
            new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
            new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
    else:
        for symbol in NIFTYFNO:
            if new_day_high_dic[symbol]<ohlc_dict[symbol]["ohlc"]["high"] and symbol not in global_high_low:
                new_day_high_list.append(symbol)
                new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
        for symbol in NIFTYFNO:
            if new_day_low_dic[symbol]<ohlc_dict[symbol]["ohlc"]["low"] and symbol not in global_high_low:
                new_day_low_list.append(symbol)
                new_day_low_dic[symbol]=ohlc_dict[symbol]["ohlc"]["low"]
    ltp_dict=get_ohlc_dict(NIFTYFNO)

    return new_day_high_list,new_day_low_list,ohlc_dict,ltp_dict

def new_5min_high_with_20ma(symbol):
    date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("5minute")
    if bool(min5_ohlc_dic) == False:
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
        o=candle[-1]["open"]
        h=candle[-1]["high"]
        l=candle[-1]["low"]
        c=candle[-1]["close"]
        min5_ohlc_dic[symbol]=(o,h,l,c)
    else:
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,timeframe, continuous=False, oi=False)
        o=candle[-1]["open"]
        h=candle[-1]["high"]
        l=candle[-1]["low"]
        c=candle[-1]["close"]
        sma_list=[]
        for i in candle:
            c=i["close"]
            sma_list.append(c)
            sma20 = sum(sma_list[-20:])/20
        ohlc=min5_ohlc_dic[symbol]
        po=ohlc[0]
        ph=ohlc[1]
        pl=ohlc[2]
        pc=ohlc[3]

        if o>sma20 and l<sma20 and h>sma20 and c>sma20 and h>ph:
            play_sound()
        if o<sma20 and h>sma20 and l<sma20 and c<sma20 and l>pl:
            play_sound()
        min5_ohlc_dic[symbol]=(o,h,l,c)

def ma20_stock():
    lst=[]
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        sma20,sma40,sma200 = get_ma(symbol,"day")
        o=ohlc_dict[symbol]["ohlc"]["open"]
        h=ohlc_dict[symbol]["ohlc"]["high"]
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o<sma20 and h>sma20 and c<o:
            lst.append(symbol)
            print(symbol)
            print(sma20)
        if o>sma20 and l<sma20 and c>o:
            lst.append(symbol)
            print(symbol)
            print(sma20)
    return lst

def fabulus_four():
    per_dic={}
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in NIFTYFNO:
        sma20,sma40,sma200 = get_ma(symbol,"5minute")
        c=ltp_dict[symbol]["last_price"]
        min_price=min(sma20,sma40,sma200,c)
        max_price=max(sma20,sma40,sma200,c)
        per = (max_price - min_price) / min_price
        per_dic[symbol]=per
    res = nsmallest(30, per_dic, key = per_dic.get)
    return res

def reversal():
    rev_dic = {}
    new_high=new_day_high(NIFTYFNO)
    new_low=new_day_low(NIFTYFNO)
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    ltp_dict=get_ltp_dict(NIFTYFNO)
    for symbol in new_high:
        h=ohlc_dict[symbol]["ohlc"]["high"]
        c=ltp_dict[symbol]["last_price"]
        rev_dic[symbol]=(h-c)/c
    for symbol in new_low:
        l=ohlc_dict[symbol]["ohlc"]["low"]
        c=ltp_dict[symbol]["last_price"]
        rev_dic[symbol]=(c-l)/l
    res = nlargest(5, rev_dic, key = rev_dic.get)
    return res
    
def current_tf_near_high_low():
    to_date=datetime.today().strftime('%Y-%m-%d')
    toDate=to_date+" 15:35:00"
    week_ago_1 = datetime.today() - relativedelta(days=7)
    fromDate = week_ago_1.strftime('%Y-%m-%d') + " 00:00:00"

    lst = []

    for symbol in NIFTYFNO:
        candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"hour" , continuous=False, oi=False)
        #print(candle[-1]["high"])
        h = candle[-1]["high"]
        o = candle[-1]["open"]
        l = candle[-1]["low"]
        c = candle[-1]["close"]
        o1 = candle[-2]["open"]
        c1 = candle[-2]["close"]

        if c > h - ( (h-l)/10) and o1>c1:
            lst.append(symbol)
            print(symbol)
        if c < l + ( (h-l)/10) and o1<c1:
            lst.append(symbol)
            print(symbol)
    return lst

def at_hour_20ma():
    to_date=datetime.today().strftime('%Y-%m-%d')
    toDate=to_date+" 15:35:00"
    week_ago_1 = datetime.today() - relativedelta(days=14)
    fromDate = week_ago_1.strftime('%Y-%m-%d') + " 00:00:00"

    lst = []

    for symbol in NIFTYFNO:
        candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"hour" , continuous=False, oi=False)
        sma20,sma40,sma200 = get_ma(symbol,"hour")
        #print(candle[-1]["high"])
        h = candle[-1]["high"]
        o = candle[-1]["open"]
        l = candle[-1]["low"]
        c = candle[-1]["close"]

        if l<sma20 and o>sma20 and c>o:
            print(symbol)
            lst.append(symbol)
        if h>sma20 and o<sma20 and c<o:
            print(symbol)
            lst.append(symbol)
    return lst

def is_ohlc_betwee_20_200ma():
    global ohlc_bw_20_200ma
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    lst_ret=[]
    if bool(ohlc_bw_20_200ma) == False:
        for symbol in NIFTYFNO:
            sma20,sma40,sma200 = get_ma(symbol,"day")
            l=ohlc_dict[symbol]["ohlc"]["low"]
            h=ohlc_dict[symbol]["ohlc"]["high"]
            if l<sma20<h or l<sma200<h:
                ohlc_bw_20_200ma.append(symbol)
        return []
    else:
        lst=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
        print(lst)
        for symbol in lst:
            if symbol not in ohlc_bw_20_200ma:
                sma20,sma40,sma200 = get_ma(symbol,"day")
                l=ohlc_dict[symbol]["ohlc"]["low"]
                h=ohlc_dict[symbol]["ohlc"]["high"]
                if l<=sma20<=h or l<=sma200<=h:
                    print(symbol)
                    lst_ret.append(symbol)
                    ohlc_bw_20_200ma.append(symbol)
    return lst_ret

def roc():
    per_dic={}
    global roc_dic
    global old_ltp_dict
    ltp_dict=get_ltp_dict(NIFTYFNO)
    if bool(old_ltp_dict) == False:
        for symbol in NIFTYFNO:
            old_ltp_dict[symbol]=ltp_dict[symbol]["last_price"]
        return []
    else:
        for symbol in NIFTYFNO:
            roc_dic[symbol] = abs (old_ltp_dict[symbol] -ltp_dict[symbol]["last_price"])/old_ltp_dict[symbol]
            old_ltp_dict[symbol]=ltp_dict[symbol]["last_price"]
    res = nlargest(5, roc_dic, key = roc_dic.get)
    return res

def narrow_range():
    lst=[]
    ltp_dict=get_ltp_dict(NIFTYFNO)
    date=date=datetime.today().strftime('%Y-%m-%d')
    toDate=date+" 15:35:00"
    fromDate=get_n_day_ago_date("5minute")
    for symbol in NIFTYFNO:
        candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"hour" , continuous=False, oi=False)
        sma20,sma40,sma200 = get_ma(symbol,"5minute")
        c=ltp_dict[symbol]["last_price"]
        min_price=min(sma20,sma40,sma200,c)
        max_price=max(sma20,sma40,sma200,c)
        per_change=((max_price-min_price)/min_price)*100
        if sma20>sma40>sma200 and per_change<0.3 and symbol not in global_high_low:
            print(symbol)
            lst.append(symbol)
        if sma20<sma40<sma200 and per_change<0.3 and symbol not in global_high_low:
            print(symbol)
            lst.append(symbol)
    return lst

def oc_bw_ma20():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    lst_ret=[]
    for symbol in NIFTYFNO:
        sma20,sma40,sma200 = get_ma(symbol,"day")
        o=ohlc_dict[symbol]["ohlc"]["open"]
        c=ohlc_dict[symbol]["ohlc"]["close"]
        if o<=sma20<=c or c<=sma20<=o:
            lst_ret.append(symbol)
            print(symbol)
    return lst_ret

def hl_bw_ma20():
    ohlc_dict=get_ohlc_dict(NIFTYFNO)
    lst_ret=[]
    for symbol in NIFTYFNO:
        sma20,sma40,sma200 = get_ma(symbol,"day")
        h=ohlc_dict[symbol]["ohlc"]["open"]
        l=ohlc_dict[symbol]["ohlc"]["close"]
        if h<=sma20<=l or l<=sma20<=h:
            lst_ret.append(symbol)
            print(symbol)
    return lst_ret

def ma_crossover_20_200_min5():
    lst=[]
    date=date=datetime.today().strftime('%Y-%m-%d')
    to_date=date+" 15:35:00"
    from_date=get_n_day_ago_date("5minute")
    for symbol in NIFTYFNO:
        candle = kite.historical_data(symbol_to_token[symbol], from_date, to_date,"5minute", continuous=False, oi=False)
        ma20Now,ma200Now=get_ma_candle(candle)
        ma20TwoCAgo,ma200TwoCAgo=get_20_200ma_min5_nCandle_ago(candle,2)
        if ma20Now>ma200Now and ma20TwoCAgo<ma200TwoCAgo and symbol not in global_high_low:
            lst.append(symbol)
        if ma20Now<ma200Now and ma20TwoCAgo>ma200TwoCAgo and symbol not in global_high_low:
            lst.append(symbol)
    return lst

def main_function(watchlist):
    final_list=[]
    global global_high_low
    print(global_high_low)
    #new_high,new_low,ohlc_dict,ltp_dict=new_high_low()
    #manual_create_dic()
    #update_important_price_dictionary()
    #morning_stratagy()
    #final_list=backtest()
    final_list=stock_crossed_ma()
    #final_list=stock_form_bw_ma()
    #final_list=get_list_top_day_moribozu()+top_gainer()+top_looser()+watchlist
    #final_list = get_list_trading_near_day_low()+get_list_trading_near_day_high()
    #final_list=top_gainer()+top_looser()+watchlist
    #final_list=ma20_stock()
    #final_list=fabulus_four()
    #final_list=get_list_top_day_moribozu()
    #final_list=ma_order_bull(NIFTYFNO)+ma_order_bear(NIFTYFNO)
    #final_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    #final_list=is_ohlc_betwee_20_200ma()
    #print(get_200ma_min5_nCandle_ago("NSE:KOTAKBANK"))
    #get_ohlc_min5_nCandle_ago("NSE:KOTAKBANK")
    #final_list=price_cross_200ma_min5()
    #final_list=top_gainer()+top_looser()
    #final_list=narrow_range()
    #final_list=top_gainer_looser()
    #final_list=algo_trade_915()
    #final_list=algo_trade()
    #final_list=reversal()
    #final_list=roc()
    #final_list=multithread_ma_order()
    #final_list=current_tf_near_high_low()
    #final_lst=at_hour_20ma()
    #final_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    #final_list=top_gainer_modified()+top_looser_modified()
    #final_list=top_gainer_with_20ma()+top_looser_with_20ma()
    #print(top_gainer())
    #print(top_looser())
    #final_list=momentum_gainer()
    #final_list=close_eq_low()+close_eq_high()
    #final_list=close_eq_low()
    #final_list=top_looser()
    #final_list=get_list_top_day_moribozu()
    #final_list=get_list_top_day_moribozu_by_thersold()
    #final_list=top_momentum()
    #final_list=bull_side_moribozu()+bear_side_moribozu()
    #final_list=list(set(final_list))
    #final_list=ma_crossover_20_200_min5()
    #day_high,day_low=get_list_trading_near_day_xxx()
    #final_list=get_list_trading_near_day_high()+get_list_trading_near_day_low()
    #print(day_high)
    #print(day_low)
    #final_list=day_high+day_low
    #final_list=top_gainer_morning()+top_looser_morning()
    #final_list=top_gainer()+top_looser()
    #print(final_list)
    #final_list=new_day_high_modified()+new_day_low_modified()
    #final_list=new_high_ma()+new_low_ma()
    #final_list=common_element(new_day_high(NIFTYFNO),less_than_by_n_per(0.1))+common_element(new_day_low(NIFTYFNO),greater_than_by_n_per(-0.1))
    #final_list=new_high_low()
    #final_list=new_high_low()
    if len(final_list) > 0:
        play_sound()
        time.sleep(2)
    sentiment()
    #global_high_low.extend(final_list)
    #global_high_low = list(set(global_high_low))
    #clear_global_list()
    #final_list=top_looser()
    #final_list=top_gainer()
    #final_list=day_high+day_low
    #final_set=set(final_list)
    #final_list=list(final_set)
    #shutil.rmtree("/home/pankaj/Pictures")
    #os.mkdir("/home/pankaj/Pictures")
    #print(final_list)
    try:
        save_screenshot(final_list)
        #print("#############################################")
    except:
        exit()
    save_structure_to_file(global_high_low)
    #save_screenshot(top_looser())
    #while monitor_top_gainer() == False:
    #print(top_looser())
    #print(top_gainer())
    #save_screenshot(top_looser())
    #save_screenshot(top_gainer())
    '''
    while monitor_top_looser() == False:
        print("... NO SIGNAL...")
        time.sleep(60)
     '''
while True:
    wl=[]
    #t=wait_for_5min()
    #if os.path.getsize("watchlist") > 0:
    #    wl=load_structure_from_file("watchlist")
    main_function(wl)
    t=wait_for_1min()
    #t=wait_for_5min()
    time.sleep(1)
    #t=get_time_to_wait()
    #custom_sleep(2)
    #break

