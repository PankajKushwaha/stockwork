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

sys.tracebacklimit = None
already_top_gainer = []
already_top_looser = []
new_day_high_dic={}
new_day_low_dic={}
global_high_low = []
global_high_low_flag = 0

nse = Nse()
pd.set_option('display.max_columns', None)

def save_list_to_file(list_name):
    with open("watchlist", 'wb') as handle:
        pickle.dump(list_name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_list_from_file(watchlist):
    if os.path.isfile(watchlist):
        with open(watchlist, 'rb') as handle:
            lst = pickle.load(handle)
            return lst
    else:
        return []

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

#NIFTYFNO=load_list_from_file("listtomonitor")
#print(len(NIFTYFNO))

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

token_to_symbol = {1793: 'NSE:AARTIIND', 3329: 'NSE:ABB', 4583169: 'NSE:ABBOTINDIA', 5533185: 'NSE:ABCAPITAL', 7707649: 'NSE:ABFRL', 5633: 'NSE:ACC', 6401: 'NSE:ADANIENT', 3861249: 'NSE:ADANIPORTS', 2995969: 'NSE:ALKEM', 25601: 'NSE:AMARAJABAT', 325121: 'NSE:AMBUJACEM', 40193: 'NSE:APOLLOHOSP', 41729: 'NSE:APOLLOTYRE', 54273: 'NSE:ASHOKLEY', 60417: 'NSE:ASIANPAINT', 3691009: 'NSE:ASTRAL', 67329: 'NSE:ATUL', 5436929: 'NSE:AUBANK', 70401: 'NSE:AUROPHARMA', 1510401: 'NSE:AXISBANK', 4267265: 'NSE:BAJAJ-AUTO', 4268801: 'NSE:BAJAJFINSV', 81153: 'NSE:BAJFINANCE', 85761: 'NSE:BALKRISIND', 87297: 'NSE:BALRAMCHIN', 579329: 'NSE:BANDHANBNK', 1195009: 'NSE:BANKBARODA', 94977: 'NSE:BATAINDIA', 98049: 'NSE:BEL', 103425: 'NSE:BERGEPAINT', 108033: 'NSE:BHARATFORG', 2714625: 'NSE:BHARTIARTL', 112129: 'NSE:BHEL', 2911489: 'NSE:BIOCON', 558337: 'NSE:BOSCHLTD', 134657: 'NSE:BPCL', 140033: 'NSE:BRITANNIA', 1790465: 'NSE:BSOFT', 2763265: 'NSE:CANBK', 149249: 'NSE:CANFINHOME', 163073: 'NSE:CHAMBLFERT', 175361: 'NSE:CHOLAFIN', 177665: 'NSE:CIPLA', 5215745: 'NSE:COALINDIA', 2955009: 'NSE:COFORGE', 3876097: 'NSE:COLPAL', 1215745: 'NSE:CONCOR', 189185: 'NSE:COROMANDEL', 4376065: 'NSE:CROMPTON', 1459457: 'NSE:CUB', 486657: 'NSE:CUMMINSIND', 197633: 'NSE:DABUR', 2067201: 'NSE:DALBHARAT', 5105409: 'NSE:DEEPAKNTR', 3851265: 'NSE:DELTACORP', 2800641: 'NSE:DIVISLAB', 5552641: 'NSE:DIXON', 3771393: 'NSE:DLF', 225537: 'NSE:DRREDDY', 232961: 'NSE:EICHERMOT', 245249: 'NSE:ESCORTS', 173057: 'NSE:EXIDEIND', 261889: 'NSE:FEDERALBNK', 3661825: 'NSE:FSL', 1207553: 'NSE:GAIL', 1895937: 'NSE:GLENMARK', 3463169: 'NSE:GMRINFRA', 300545: 'NSE:GNFC', 2585345: 'NSE:GODREJCP', 4576001: 'NSE:GODREJPROP', 3039233: 'NSE:GRANULES', 315393: 'NSE:GRASIM', 3378433: 'NSE:GSPL', 2713345: 'NSE:GUJGASLTD', 589569: 'NSE:HAL', 2513665: 'NSE:HAVELLS', 1850625: 'NSE:HCLTECH', 340481: 'NSE:HDFC', 1086465: 'NSE:HDFCAMC', 341249: 'NSE:HDFCBANK', 119553: 'NSE:HDFCLIFE', 345089: 'NSE:HEROMOTOCO', 348929: 'NSE:HINDALCO', 4592385: 'NSE:HINDCOPPER', 359937: 'NSE:HINDPETRO', 356865: 'NSE:HINDUNILVR', 874753: 'NSE:HONAUT', 7712001: 'NSE:IBULHSGFIN', 1270529: 'NSE:ICICIBANK', 5573121: 'NSE:ICICIGI', 4774913: 'NSE:ICICIPRULI', 3677697: 'NSE:IDEA', 3060993: 'NSE:IDFC', 2863105: 'NSE:IDFCFIRSTB', 56321: 'NSE:IEX', 2883073: 'NSE:IGL', 387073: 'NSE:INDHOTEL', 387841: 'NSE:INDIACEM', 2745857: 'NSE:INDIAMART', 2865921: 'NSE:INDIGO', 1346049: 'NSE:INDUSINDBK', 7458561: 'NSE:INDUSTOWER', 408065: 'NSE:INFY', 1517057: 'NSE:INTELLECT', 415745: 'NSE:IOC', 418049: 'NSE:IPCALAB', 3484417: 'NSE:IRCTC', 424961: 'NSE:ITC', 1723649: 'NSE:JINDALSTEL', 3397121: 'NSE:JKCEMENT', 3001089: 'NSE:JSWSTEEL', 4632577: 'NSE:JUBLFOOD', 492033: 'NSE:KOTAKBANK', 6386689: 'NSE:L&TFH', 2983425: 'NSE:LALPATHLAB', 4923905: 'NSE:LAURUSLABS', 511233: 'NSE:LICHSGFIN', 2939649: 'NSE:LT', 4561409: 'NSE:LTI', 4752385: 'NSE:LTTS', 2672641: 'NSE:LUPIN', 519937: 'NSE:M&M', 3400961: 'NSE:M&MFIN', 4879617: 'NSE:MANAPPURAM', 1041153: 'NSE:MARICO', 2815745: 'NSE:MARUTI', 2674433: 'NSE:MCDOWELL-N', 7982337: 'NSE:MCX', 2452737: 'NSE:METROPOLIS', 548353: 'NSE:MFSL', 4488705: 'NSE:MGL', 3675137: 'NSE:MINDTREE', 1076225: 'NSE:MOTHERSON', 1152769: 'NSE:MPHASIS', 582913: 'NSE:MRF', 6054401: 'NSE:MUTHOOTFIN', 91393: 'NSE:NAM-INDIA', 1629185: 'NSE:NATIONALUM', 3520257: 'NSE:NAUKRI', 3756033: 'NSE:NAVINFLUOR', 8042241: 'NSE:NBCC', 4598529: 'NSE:NESTLEIND', 3924993: 'NSE:NMDC', 2977281: 'NSE:NTPC', 5181953: 'NSE:OBEROIRLTY', 2748929: 'NSE:OFSS', 633601: 'NSE:ONGC', 3689729: 'NSE:PAGEIND', 617473: 'NSE:PEL', 4701441: 'NSE:PERSISTENT', 2905857: 'NSE:PETRONET', 3660545: 'NSE:PFC', 681985: 'NSE:PIDILITIND', 6191105: 'NSE:PIIND', 2730497: 'NSE:PNB', 2455041: 'NSE:POLYCAB', 3834113: 'NSE:POWERGRID', 3365633: 'NSE:PVR', 3926273: 'NSE:RAIN', 523009: 'NSE:RAMCOCEM', 4708097: 'NSE:RBLBANK', 3930881: 'NSE:RECLTD', 738561: 'NSE:RELIANCE', 758529: 'NSE:SAIL', 4600577: 'NSE:SBICARD', 5582849: 'NSE:SBILIFE', 779521: 'NSE:SBIN', 794369: 'NSE:SHREECEM', 806401: 'NSE:SIEMENS', 837889: 'NSE:SRF', 1102337: 'NSE:SRTRANSFIN', 857857: 'NSE:SUNPHARMA', 3431425: 'NSE:SUNTV', 2622209: 'NSE:SYNGENE', 871681: 'NSE:TATACHEM', 952577: 'NSE:TATACOMM', 878593: 'NSE:TATACONSUM', 884737: 'NSE:TATAMOTORS', 877057: 'NSE:TATAPOWER', 895745: 'NSE:TATASTEEL', 2953217: 'NSE:TCS', 3465729: 'NSE:TECHM', 897537: 'NSE:TITAN', 900609: 'NSE:TORNTPHARM', 3529217: 'NSE:TORNTPOWER', 502785: 'NSE:TRENT', 2170625: 'NSE:TVSMOTOR', 4278529: 'NSE:UBL', 2952193: 'NSE:ULTRACEMCO', 2889473: 'NSE:UPL', 784129: 'NSE:VEDL', 951809: 'NSE:VOLTAS', 4610817: 'NSE:WHIRLPOOL', 969473: 'NSE:WIPRO', 975873: 'NSE:ZEEL', 2029825: 'NSE:ZYDUSLIFE'}
symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}

#NIFTYFNO=['ABB', 'HONAUT', 'DALBHARAT', 'GODREJCP', 'BAJFINANCE', 'BAJAJFINSV', 'BRITANNIA', 'AUBANK', 'TRENT', 'GUJGASLTD', 'INTELLECT', 'HINDUNILVR', 'ESCORTS', 'DIXON', 'BATAINDIA', 'ICICIGI', 'CONCOR', 'APOLLOTYRE', 'WHIRLPOOL', 'EICHERMOT', 'RAMCOCEM', 'HINDPETRO', 'M&MFIN', 'SIEMENS', 'HEROMOTOCO', 'SBICARD', 'IDEA', 'ASIANPAINT', 'IEX', 'GODREJPROP', 'ZEEL', 'HAVELLS', 'CUMMINSIND', 'TITAN', 'MARUTI', 'UBL', 'COROMANDEL', 'ABBOTINDIA', 'BERGEPAINT', 'PERSISTENT', 'JKCEMENT', 'ABCAPITAL', 'LTTS', 'DELTACORP', 'AARTIIND', 'MRF', 'KOTAKBANK', 'BOSCHLTD', 'INDIACEM', 'TATACONSUM', 'LICHSGFIN', 'COLPAL', 'SHREECEM', 'BPCL', 'PAGEIND', 'SUNTV', 'RBLBANK', 'FSL', 'BAJAJ-AUTO', 'PIIND', 'GLENMARK', 'BIOCON', 'NAUKRI', 'M&M', 'ADANIPORTS', 'MGL', 'HDFCAMC', 'DLF', 'VOLTAS', 'OBEROIRLTY', 'IBULHSGFIN', 'L&TFH', 'MCDOWELL-N', 'NESTLEIND', 'INDUSTOWER', 'PIDILITIND', 'DABUR', 'MPHASIS', 'GMRINFRA', 'IPCALAB', 'MFSL', 'CANBK', 'OFSS', 'APOLLOHOSP', 'PETRONET', 'COFORGE', 'POLYCAB', 'ICICIPRULI', 'GRASIM', 'SBIN', 'BHEL', 'MINDTREE', 'LTI', 'TVSMOTOR', 'CROMPTON', 'AUROPHARMA', 'INDUSINDBK', 'BANDHANBNK', 'MARICO', 'ULTRACEMCO', 'IDFCFIRSTB', 'MOTHERSON', 'INDIGO', 'AMARAJABAT', 'TORNTPOWER', 'ALKEM', 'TCS', 'INDIAMART', 'LAURUSLABS', 'ACC', 'ASHOKLEY', 'METROPOLIS', 'IRCTC', 'HDFCBANK', 'NBCC', 'DEEPAKNTR', 'DIVISLAB', 'TATACOMM', 'HINDCOPPER', 'AXISBANK', 'NATIONALUM', 'JUBLFOOD', 'BHARTIARTL', 'IGL', 'TATAMOTORS', 'IDFC', 'ABFRL', 'ZYDUSLIFE', 'ICICIBANK', 'TATACHEM', 'INFY', 'BANKBARODA', 'RECLTD', 'UPL', 'ADANIENT', 'HDFC', 'BEL', 'TECHM', 'JINDALSTEL', 'GNFC', 'BALKRISIND', 'PEL', 'CIPLA', 'NAM-INDIA', 'NAVINFLUOR', 'FEDERALBNK', 'ITC', 'PNB', 'CANFINHOME', 'MANAPPURAM', 'WIPRO', 'EXIDEIND', 'MCX', 'TATAPOWER', 'CHAMBLFERT', 'HCLTECH', 'JSWSTEEL', 'SBILIFE', 'ASTRAL', 'AMBUJACEM', 'INDHOTEL', 'SUNPHARMA', 'SRF', 'TORNTPHARM', 'GSPL', 'LALPATHLAB', 'CUB', 'SRTRANSFIN', 'CHOLAFIN', 'GAIL', 'SAIL', 'LUPIN', 'RAIN', 'DRREDDY', 'PFC', 'TATASTEEL', 'MUTHOOTFIN', 'PVR', 'BHARATFORG', 'LT', 'SYNGENE', 'COALINDIA', 'GRANULES', 'HAL', 'ATUL', 'RELIANCE', 'NTPC', 'HDFCLIFE', 'HINDALCO', 'VEDL', 'BSOFT', 'IOC', 'POWERGRID', 'NMDC', 'BALRAMCHIN', 'ONGC']

def get_all_ma(symbol):
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
            print(symbol)
            print(new_day_high_dic[symbol])
            print(ohlc_dict[symbol]["ohlc"]["high"])
            if new_day_high_dic[symbol]<ohlc_dict[symbol]["ohlc"]["high"] and symbol not in global_high_low:
                new_day_high_list.append(symbol)
                new_day_high_per_change[symbol]= ((ohlc_dict[symbol]["ohlc"]["close"] - new_day_high_dic[symbol])/new_day_high_dic[symbol])
                new_day_high_dic[symbol]=ohlc_dict[symbol]["ohlc"]["high"]
    
    x=sorted(new_day_high_per_change.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    new_list.reverse()
    top_day_high_by_change=new_list[0:5]
    print(new_day_high_list)
    return top_day_high_by_change
    #return new_day_high_list

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
   
    x=sorted(new_day_low_per_change.items(), key=lambda item: item[1])
    print(x)
    new_list = [ seq[0] for seq in x ]
    #new_list.reverse()
    top_day_low_by_change=new_list[0:5]
    
    return top_day_low_by_change
    #return new_day_low_list


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
    top_day_moribozu=new_list[0:4]
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
        #time.sleep(2)
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
        #time.sleep(2)
        custom_sleep(2)
    if "RAIN" in stock:
        stock = stock.replace('NSE:','')
        #time.sleep(2)
        print(stock)
        custom_sleep(2)
    if ":LT" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        custom_sleep(2)
    if ":INDIGO" in stock:
        stock = stock.replace('NSE:','')
        print(stock)
        custom_sleep(2)
        #time.sleep(2)
    print(stock)
    time.sleep(1)
    pyautogui.typewrite(stock)
    #custom_sleep(1)
    #pyautogui.typewrite(["enter"])
    pyautogui.click(167,206)
    #pyautogui.typewrite(["enter"])
    time.sleep(1)
    #time.sleep(2)
    #play_sound()
    #custom_sleep(1)
    #call_option,put_option=get_call_put_option(stock.replace('NSE:',''),"25-Aug-2022","AUG","22")
    #print(call_option)
    #print(put_option)
    #image = pyautogui.screenshot()
    #image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    #cv2.imwrite("/home/pankaj/Pictures/"+stock+".png", image)
    #change_timeframe()

def save_screenshot(top_list):
    for stock in top_list:
        save_screenshot_stock(stock)
        #save_screenshot_zebro(stock)
        time.sleep(3)
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
            #time.sleep(2)
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
            #time.sleep(2)
            custom_sleep(2)
        if "RAIN" in stock:
            stock = stock.replace('NSE:','')
            #time.sleep(2)
            print(stock)
            custom_sleep(2)
        if ":LT" in stock:
            stock = stock.replace('NSE:','')
            print(stock)
            custom_sleep(2)
            #time.sleep(2)
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
    new_high=new_day_high(NIFTYFNO)
    ma20 = load_list_from_file("listtomonitor_bull")
    return list(set(new_high)&set(ma20))

def new_low_with_20ma():
    new_low=new_day_low(NIFTYFNO)
    ma20 = load_list_from_file("listtomonitor_bear")
    return list(set(new_low)&set(ma20))

def top_gainer_with_20ma():
    topg=top_gainer()
    ma20 = load_list_from_file("listtomonitor_bull")
    return list(set(topg)&set(ma20))

def top_looser_with_20ma():
    topl=top_looser()
    ma20 = load_list_from_file("listtomonitor_bear")
    return list(set(topl)&set(ma20))

def new_high_low():
    bull_trend=sentiment()
    if bull_trend>0.6:
        return new_day_high(NIFTYFNO)
    elif bull_trend<0.4:
        return new_day_low(NIFTYFNO)
    else:
        print("#### DONT TRADE RANGING MARKET ####")
        return []

def main_function(watchlist):
    final_list=[]
    #final_list=get_list_top_day_moribozu()+top_gainer()+top_looser()+watchlist
    #final_list = get_list_trading_near_day_low()+get_list_trading_near_day_high()
    #final_list=top_gainer()+top_looser()+watchlist
    #final_list=top_gainer()+top_looser()
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
    #day_high,day_low=get_list_trading_near_day_xxx()
    #final_list=get_list_trading_near_day_high()+get_list_trading_near_day_low()
    #print(day_high)
    #print(day_low)
    #final_list=day_high+day_low
    #final_list=top_gainer_morning()+top_looser_morning()
    #final_list=top_gainer()+top_looser()
    #print(final_list)
    final_list=new_day_high(NIFTYFNO)+new_day_low(NIFTYFNO)
    #final_list=common_element(new_day_high(NIFTYFNO),less_than_by_n_per(0.1))+common_element(new_day_low(NIFTYFNO),greater_than_by_n_per(-0.1))
    #final_list=new_high_low()
    #final_list=new_high_low()
    '''
    if len(final_list) > 0:
        play_sound()
    '''
    sentiment()
    global_high_low.extend(final_list)
    #clear_global_list()
    #final_list=top_looser()
    #final_list=top_gainer()
    #final_list=day_high+day_low
    #final_set=set(final_list)
    #final_list=list(final_set)
    #shutil.rmtree("/home/pankaj/Pictures")
    #os.mkdir("/home/pankaj/Pictures")
    print(final_list)
    try:
        save_screenshot(final_list)
        print(None)
    except:
        exit()
    save_list_to_file(final_list)
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
    if os.path.getsize("watchlist") > 0:
        wl=load_list_from_file("watchlist")
    main_function(wl)
    #t=get_time_to_wait()
    #time.sleep(10)
    time.sleep(5)
    #custom_sleep(2)
    #break

