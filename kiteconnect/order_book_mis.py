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
from pynse import *


lot_size={'ABB': 250, 'HONAUT': 15, 'DALBHARAT': 500, 'GODREJCP': 1000, 'BAJFINANCE': 125, 'BAJAJFINSV': 500, 'BRITANNIA': 200, 'AUBANK': 1000, 'TRENT': 725, 'GUJGASLTD': 1250, 'INTELLECT': 750, 'HINDUNILVR': 300, 'ESCORTS': 550, 'DIXON': 125, 'BATAINDIA': 275, 'ICICIGI': 425, 'CONCOR': 1000, 'APOLLOTYRE': 3500, 'WHIRLPOOL': 350, 'EICHERMOT': 350, 'RAMCOCEM': 850, 'HINDPETRO': 2700, 'M&MFIN': 4000, 'SIEMENS': 275, 'HEROMOTOCO': 300, 'SBICARD': 800, 'ASIANPAINT': 200, 'IEX': 3750, 'GODREJPROP': 325, 'ZEEL': 3000, 'HAVELLS': 500, 'CUMMINSIND': 600, 'TITAN': 375, 'MARUTI': 100, 'UBL': 400, 'COROMANDEL': 700, 'ABBOTINDIA': 40, 'BERGEPAINT': 1100, 'PERSISTENT': 150, 'JKCEMENT': 250, 'ABCAPITAL': 5400, 'LTTS': 200, 'DELTACORP': 2300, 'AARTIIND': 850, 'MRF': 10, 'KOTAKBANK': 400, 'BOSCHLTD': 50, 'INDIACEM': 2900, 'TATACONSUM': 900, 'LICHSGFIN': 2000, 'COLPAL': 350, 'SHREECEM': 25, 'BPCL': 1800, 'PAGEIND': 15, 'SUNTV': 1500, 'RBLBANK': 5000, 'FSL': 5200, 'BAJAJ-AUTO': 250, 'PIIND': 250, 'GLENMARK': 1450, 'BIOCON': 2300, 'NAUKRI': 125, 'M&M': 700, 'ADANIPORTS': 1250, 'MGL': 800, 'HDFCAMC': 300, 'DLF': 1650, 'VOLTAS': 500, 'OBEROIRLTY': 700, 'IBULHSGFIN': 4000, 'L&TFH': 8924, 'MCDOWELL-N': 625, 'NESTLEIND': 40, 'INDUSTOWER': 2800, 'PIDILITIND': 250, 'DABUR': 1250, 'MPHASIS': 175, 'GMRINFRA': 22500, 'IPCALAB': 650, 'MFSL': 650, 'CANBK': 2700, 'OFSS': 200, 'APOLLOHOSP': 125, 'PETRONET': 3000, 'COFORGE': 150, 'POLYCAB': 300, 'ICICIPRULI': 1500, 'GRASIM': 475, 'SBIN': 1500, 'BHEL': 10500, 'MINDTREE': 200, 'LTI': 150, 'TVSMOTOR': 1400, 'CROMPTON': 1500, 'AUROPHARMA': 1000, 'INDUSINDBK': 900, 'BANDHANBNK': 1800, 'MARICO': 1200, 'ULTRACEMCO': 100, 'IDFCFIRSTB': 15000, 'MOTHERSON': 4500, 'INDIGO': 300, 'AMARAJABAT': 1000, 'TORNTPOWER': 1500, 'ALKEM': 200, 'TCS': 175, 'INDIAMART': 150, 'LAURUSLABS': 900, 'ACC': 250, 'ASHOKLEY': 5000, 'METROPOLIS': 300, 'IRCTC': 875, 'HDFCBANK': 550, 'DEEPAKNTR': 250, 'DIVISLAB': 150, 'TATACOMM': 500, 'HINDCOPPER': 4300, 'AXISBANK': 1200, 'NATIONALUM': 4250, 'JUBLFOOD': 1250, 'BHARTIARTL': 950, 'IGL': 1375, 'TATAMOTORS': 1425, 'IDFC': 10000, 'ABFRL': 2600, 'ZYDUSLIFE': 1800, 'ICICIBANK': 1375, 'TATACHEM': 1000, 'INFY': 300, 'BANKBARODA': 5850, 'RECLTD': 8000, 'UPL': 1300, 'ADANIENT': 500, 'HDFC': 300, 'BEL': 11400, 'TECHM': 600, 'JINDALSTEL': 1250, 'GNFC': 1300, 'BALKRISIND': 300, 'PEL': 275, 'CIPLA': 650, 'NAVINFLUOR': 225, 'FEDERALBNK': 10000, 'ITC': 3200, 'PNB': 16000, 'CANFINHOME': 975, 'MANAPPURAM': 6000, 'WIPRO': 1000, 'EXIDEIND': 3600, 'TATAPOWER': 3375, 'CHAMBLFERT': 1500, 'HCLTECH': 700, 'JSWSTEEL': 1350, 'SBILIFE': 750, 'ASTRAL': 275, 'AMBUJACEM': 1800, 'INDHOTEL': 4022, 'SUNPHARMA': 700, 'SRF': 375, 'TORNTPHARM': 500, 'GSPL': 2500, 'LALPATHLAB': 250, 'CUB': 5000, 'SRTRANSFIN': 600, 'CHOLAFIN': 1250, 'GAIL': 9150, 'SAIL': 6000, 'LUPIN': 850, 'RAIN': 3500, 'DRREDDY': 125, 'PFC': 6200, 'TATASTEEL': 4250, 'MUTHOOTFIN': 375, 'PVR': 407, 'BHARATFORG': 1000, 'LT': 300, 'SYNGENE': 1000, 'COALINDIA': 4200, 'GRANULES': 2000, 'HAL': 475, 'ATUL': 75, 'RELIANCE': 250, 'NTPC': 5700, 'HDFCLIFE': 1100, 'HINDALCO': 1075, 'VEDL': 1550, 'BSOFT': 2000, 'IOC': 9750, 'POWERGRID': 2700, 'NMDC': 3350, 'BALRAMCHIN': 1600, 'ONGC': 3850}

#lot_size = {'BANKNIFTY': 25, 'NIFTY': 50,'BALRAMCHIN': 1600, 'FINNIFTY': 40, 'ASTRAL': 275, 'AARTIIND': 850, 'ABBOTINDIA': 25, 'ACC': 250, 'ADANIENT': 500, 'ALKEM': 200, 'AMARAJABAT': 1000, 'AMBUJACEM': 1500, 'APLLTD': 550, 'APOLLOHOSP': 125, 'ASHOKLEY': 4500, 'AUBANK': 500, 'ATUL': 75, 'AUROPHARMA': 650, 'ADANIPORTS': 1250, 'BAJAJFINSV': 75, 'BAJFINANCE': 125, 'BALKRISIND': 300, 'BANDHANBNK': 1800, 'BATAINDIA': 550, 'BEL': 3800, 'BHARTIARTL': 1886, 'BHEL': 10500, 'BIOCON': 2300, 'AXISBANK': 1200, 'BPCL': 1800, 'CADILAHC': 1100, 'CANFINHOME': 975, 'CHOLAFIN': 1250, 'CIPLA': 650, 'COFORGE': 100, 'CUB': 3100, 'ASIANPAINT': 200, 'DABUR': 1250, 'DEEPAKNTR': 250, 'DIVISLAB': 100, 'DRREDDY': 125, 'GLENMARK': 1150, 'GODREJCP': 500, 'GODREJPROP': 325, 'GRANULES': 1550, 'GRASIM': 475, 'BSOFT': 2000, 'CANBK': 5400, 'HAL': 475, 'HAVELLS': 500, 'HCLTECH': 700, 'HDFCAMC': 300, 'HDFCBANK': 550, 'HINDALCO': 1075, 'CHAMBLFERT': 1500, 'HINDUNILVR': 300, 'BHARATFORG': 750, 'ICICIGI': 425, 'ICICIPRULI': 750, 'IDFCFIRSTB': 9500, 'BOSCHLTD': 50, 'IEX': 1250, 'INDHOTEL': 4022, 'EICHERMOT': 350, 'BRITANNIA': 200, 'FSL': 2600, 'INDIGO': 250, 'INFY': 300, 'IPCALAB': 225, 'GSPL': 1700, 'IRCTC': 1625, 'JSWSTEEL': 1350, 'JUBLFOOD': 1250, 'KOTAKBANK': 400, 'COALINDIA': 4200, 'L&TFH': 8924, 'LALPATHLAB': 125, 'LT': 575, 'LTI': 150, 'LTTS': 200, 'CROMPTON': 1100, 'MANAPPURAM': 3000, 'MARICO': 1000, 'CUMMINSIND': 600, 'MCDOWELL-N': 1250, 'METROPOLIS': 200, 'MGL': 600, 'DELTACORP': 2300, 'MINDTREE': 200, 'MPHASIS': 175, 'MRF': 10, 'MUTHOOTFIN': 375, 'NATIONALUM': 8500, 'ITC': 3200, 'DIXON': 125, 'NAUKRI': 125, 'NAVINFLUOR': 225, 'NESTLEIND': 25, 'OFSS': 125, 'ONGC': 7700, 'PAGEIND': 30, 'PFC': 6200, 'PIIND': 250, 'LAURUSLABS': 900, 'POLYCAB': 300, 'POWERGRID': 5333, 'GAIL': 6100, 'PVR': 407, 'RAMCOCEM': 850, 'RECLTD': 6000, 'RELIANCE': 250, 'SAIL': 4750, 'GMRINFRA': 22500, 'SBILIFE': 750, 'SHREECEM': 25, 'GUJGASLTD': 1250, 'SRF': 625, 'SRTRANSFIN': 400, 'STAR': 675, 'SUNPHARMA': 700, 'TATAMOTORS': 2850, 'TATAPOWER': 6750, 'TCS': 150, 'HDFC': 300, 'TORNTPHARM': 250, 'TORNTPOWER': 1500, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 3100, 'VOLTAS': 500, 'HDFCLIFE': 1100, 'IBULHSGFIN': 3100, 'ICICIBANK': 1375, 'ABFRL': 2600, 'JKCEMENT': 250, 'RBLBANK': 2900, 'LUPIN': 850, 'M&MFIN': 4000, 'SBICARD': 500, 'MARUTI': 100,'TVSMOTOR': 1400, 'WHIRLPOOL': 250, 'OBEROIRLTY': 700, 'PEL': 275, 'PERSISTENT': 150, 'PFIZER': 125, 'BANKBARODA': 11700, 'BERGEPAINT': 1100, 'TATACONSUM': 675, 'TRENT': 400, 'COLPAL': 350, 'CONCOR': 1563, 'COROMANDEL': 625, 'DLF': 1650, 'ESCORTS': 550, 'EXIDEIND': 3600, 'FEDERALBNK': 10000, 'HEROMOTOCO': 300, 'HINDPETRO': 2700, 'APOLLOTYRE': 2500, 'IGL': 1375, 'INDIAMART': 75, 'IOC': 6500, 'JINDALSTEL': 2500, 'LICHSGFIN': 2000, 'DALBHARAT': 250, 'M&M': 700, 'MCX': 350, 'MFSL': 650, 'MOTHERSUMI': 3500, 'SUNTV': 1500, 'NMDC': 6700, 'NTPC': 5700, 'PETRONET': 3000, 'PIDILITIND': 250, 'PNB': 16000, 'SBIN': 1500, 'SIEMENS': 275, 'INDIACEM': 2900, 'SYNGENE': 850, 'TATASTEEL': 425, 'TECHM': 600, 'TITAN': 375, 'UBL': 350, 'ZEEL': 3000, 'TATACHEM': 1000, 'BAJAJ-AUTO': 250, 'INDUSTOWER': 2800, 'IDEA': 70000, 'WIPRO': 800, 'INDUSINDBK': 900}

NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}

token_to_symbol = {1793: 'NSE:AARTIIND', 3329: 'NSE:ABB', 4583169: 'NSE:ABBOTINDIA', 5533185: 'NSE:ABCAPITAL', 7707649: 'NSE:ABFRL', 5633: 'NSE:ACC', 6401: 'NSE:ADANIENT', 3861249: 'NSE:ADANIPORTS', 2995969: 'NSE:ALKEM', 25601: 'NSE:AMARAJABAT', 325121: 'NSE:AMBUJACEM', 40193: 'NSE:APOLLOHOSP', 41729: 'NSE:APOLLOTYRE', 54273: 'NSE:ASHOKLEY', 60417: 'NSE:ASIANPAINT', 3691009: 'NSE:ASTRAL', 67329: 'NSE:ATUL', 5436929: 'NSE:AUBANK', 70401: 'NSE:AUROPHARMA', 1510401: 'NSE:AXISBANK', 4267265: 'NSE:BAJAJ-AUTO', 4268801: 'NSE:BAJAJFINSV', 81153: 'NSE:BAJFINANCE', 85761: 'NSE:BALKRISIND', 87297: 'NSE:BALRAMCHIN', 579329: 'NSE:BANDHANBNK', 1195009: 'NSE:BANKBARODA', 94977: 'NSE:BATAINDIA', 98049: 'NSE:BEL', 103425: 'NSE:BERGEPAINT', 108033: 'NSE:BHARATFORG', 2714625: 'NSE:BHARTIARTL', 112129: 'NSE:BHEL', 2911489: 'NSE:BIOCON', 558337: 'NSE:BOSCHLTD', 134657: 'NSE:BPCL', 140033: 'NSE:BRITANNIA', 1790465: 'NSE:BSOFT', 2763265: 'NSE:CANBK', 149249: 'NSE:CANFINHOME', 163073: 'NSE:CHAMBLFERT', 175361: 'NSE:CHOLAFIN', 177665: 'NSE:CIPLA', 5215745: 'NSE:COALINDIA', 2955009: 'NSE:COFORGE', 3876097: 'NSE:COLPAL', 1215745: 'NSE:CONCOR', 189185: 'NSE:COROMANDEL', 4376065: 'NSE:CROMPTON', 1459457: 'NSE:CUB', 486657: 'NSE:CUMMINSIND', 197633: 'NSE:DABUR', 2067201: 'NSE:DALBHARAT', 5105409: 'NSE:DEEPAKNTR', 3851265: 'NSE:DELTACORP', 2800641: 'NSE:DIVISLAB', 5552641: 'NSE:DIXON', 3771393: 'NSE:DLF', 225537: 'NSE:DRREDDY', 232961: 'NSE:EICHERMOT', 245249: 'NSE:ESCORTS', 173057: 'NSE:EXIDEIND', 261889: 'NSE:FEDERALBNK', 3661825: 'NSE:FSL', 1207553: 'NSE:GAIL', 1895937: 'NSE:GLENMARK', 3463169: 'NSE:GMRINFRA', 300545: 'NSE:GNFC', 2585345: 'NSE:GODREJCP', 4576001: 'NSE:GODREJPROP', 3039233: 'NSE:GRANULES', 315393: 'NSE:GRASIM', 3378433: 'NSE:GSPL', 2713345: 'NSE:GUJGASLTD', 589569: 'NSE:HAL', 2513665: 'NSE:HAVELLS', 1850625: 'NSE:HCLTECH', 340481: 'NSE:HDFC', 1086465: 'NSE:HDFCAMC', 341249: 'NSE:HDFCBANK', 119553: 'NSE:HDFCLIFE', 345089: 'NSE:HEROMOTOCO', 348929: 'NSE:HINDALCO', 4592385: 'NSE:HINDCOPPER', 359937: 'NSE:HINDPETRO', 356865: 'NSE:HINDUNILVR', 874753: 'NSE:HONAUT', 7712001: 'NSE:IBULHSGFIN', 1270529: 'NSE:ICICIBANK', 5573121: 'NSE:ICICIGI', 4774913: 'NSE:ICICIPRULI', 3677697: 'NSE:IDEA', 3060993: 'NSE:IDFC', 2863105: 'NSE:IDFCFIRSTB', 56321: 'NSE:IEX', 2883073: 'NSE:IGL', 387073: 'NSE:INDHOTEL', 387841: 'NSE:INDIACEM', 2745857: 'NSE:INDIAMART', 2865921: 'NSE:INDIGO', 1346049: 'NSE:INDUSINDBK', 7458561: 'NSE:INDUSTOWER', 408065: 'NSE:INFY', 1517057: 'NSE:INTELLECT', 415745: 'NSE:IOC', 418049: 'NSE:IPCALAB', 3484417: 'NSE:IRCTC', 424961: 'NSE:ITC', 1723649: 'NSE:JINDALSTEL', 3397121: 'NSE:JKCEMENT', 3001089: 'NSE:JSWSTEEL', 4632577: 'NSE:JUBLFOOD', 492033: 'NSE:KOTAKBANK', 6386689: 'NSE:L&TFH', 2983425: 'NSE:LALPATHLAB', 4923905: 'NSE:LAURUSLABS', 511233: 'NSE:LICHSGFIN', 2939649: 'NSE:LT', 4561409: 'NSE:LTI', 4752385: 'NSE:LTTS', 2672641: 'NSE:LUPIN', 519937: 'NSE:M&M', 3400961: 'NSE:M&MFIN', 4879617: 'NSE:MANAPPURAM', 1041153: 'NSE:MARICO', 2815745: 'NSE:MARUTI', 2674433: 'NSE:MCDOWELL-N', 7982337: 'NSE:MCX', 2452737: 'NSE:METROPOLIS', 548353: 'NSE:MFSL', 4488705: 'NSE:MGL', 3675137: 'NSE:MINDTREE', 1076225: 'NSE:MOTHERSON', 1152769: 'NSE:MPHASIS', 582913: 'NSE:MRF', 6054401: 'NSE:MUTHOOTFIN', 91393: 'NSE:NAM-INDIA', 1629185: 'NSE:NATIONALUM', 3520257: 'NSE:NAUKRI', 3756033: 'NSE:NAVINFLUOR', 8042241: 'NSE:NBCC', 4598529: 'NSE:NESTLEIND', 3924993: 'NSE:NMDC', 2977281: 'NSE:NTPC', 5181953: 'NSE:OBEROIRLTY', 2748929: 'NSE:OFSS', 633601: 'NSE:ONGC', 3689729: 'NSE:PAGEIND', 617473: 'NSE:PEL', 4701441: 'NSE:PERSISTENT', 2905857: 'NSE:PETRONET', 3660545: 'NSE:PFC', 681985: 'NSE:PIDILITIND', 6191105: 'NSE:PIIND', 2730497: 'NSE:PNB', 2455041: 'NSE:POLYCAB', 3834113: 'NSE:POWERGRID', 3365633: 'NSE:PVR', 3926273: 'NSE:RAIN', 523009: 'NSE:RAMCOCEM', 4708097: 'NSE:RBLBANK', 3930881: 'NSE:RECLTD', 738561: 'NSE:RELIANCE', 758529: 'NSE:SAIL', 4600577: 'NSE:SBICARD', 5582849: 'NSE:SBILIFE', 779521: 'NSE:SBIN', 794369: 'NSE:SHREECEM', 806401: 'NSE:SIEMENS', 837889: 'NSE:SRF', 1102337: 'NSE:SRTRANSFIN', 857857: 'NSE:SUNPHARMA', 3431425: 'NSE:SUNTV', 2622209: 'NSE:SYNGENE', 871681: 'NSE:TATACHEM', 952577: 'NSE:TATACOMM', 878593: 'NSE:TATACONSUM', 884737: 'NSE:TATAMOTORS', 877057: 'NSE:TATAPOWER', 895745: 'NSE:TATASTEEL', 2953217: 'NSE:TCS', 3465729: 'NSE:TECHM', 897537: 'NSE:TITAN', 900609: 'NSE:TORNTPHARM', 3529217: 'NSE:TORNTPOWER', 502785: 'NSE:TRENT', 2170625: 'NSE:TVSMOTOR', 4278529: 'NSE:UBL', 2952193: 'NSE:ULTRACEMCO', 2889473: 'NSE:UPL', 784129: 'NSE:VEDL', 951809: 'NSE:VOLTAS', 4610817: 'NSE:WHIRLPOOL', 969473: 'NSE:WIPRO', 975873: 'NSE:ZEEL', 2029825: 'NSE:ZYDUSLIFE'}





max_pnl = {}

def get_quantity(stock):
    return nse_get_fno_lot_sizes()[stock.split("24")[0]]

def get_open_position_price_dic(fnosymbol):
    open_position_list = []
    open_position_price_dic = {}
    pos = kite.positions()
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        open_position_list.append("NFO:"+dic['tradingsymbol'])
    if len(open_position_list) == 0:
        open_position_list.append(fnosymbol)
    ltp_list=kite.ltp(open_position_list)
    #print(kite.ltp(open_position_list))
    for symbol in ltp_list:
        open_position_price_dic[symbol.replace("NFO:","")]=ltp_list[symbol]['last_price']

    return open_position_price_dic

def track_sl():
    open_position_list = []
    pos = kite.positions()
    '''
    for dic in pos['net']:
        #if dic['quantity'] > 0:
        #print(dic['tradingsymbol'])
        #print(dic['quantity'])
        #print(int(dic['pnl']))
        #pnl=int(dic['pnl'])

        if dic['quantity']>0:
            ltp_dic=get_open_position_price_dic()
            
            pnl=(ltp_dic[dic['tradingsymbol']]*dic['quantity']) - (dic['quantity']*dic['average_price'])
            #print(pnl)
            global max_pnl
            if dic['tradingsymbol'] not in max_pnl:
                max_pnl[dic['tradingsymbol']] =  pnl
            
            if pnl > max_pnl[dic['tradingsymbol']]:
                max_pnl[dic['tradingsymbol']] = pnl
            
            if max_pnl[dic['tradingsymbol']] > 1000 and pnl < 500 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 1500 and pnl < 800 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 2000 and pnl < 1000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 5000 and pnl < 2000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 7000 and pnl < 5000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 10000 and pnl < 7000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
            if max_pnl[dic['tradingsymbol']] > 15000 and pnl < 12000 :
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])


            if pnl < -500 or pnl > 10000:
                sell_fno_symbol(dic['tradingsymbol'],ltp_dic[dic['tradingsymbol']])
                time.sleep(5)
    '''

def get_ltp_dict(NIFTYFNO):
    ltp_dict=kite.ltp(NIFTYFNO)
    #print(ohlc_dict)
    return ltp_dict

def ltp_fno_symbo(symbol):
    print(symbol)
    ltp_dict=kite.ltp([symbol])
    c=ltp_dict[symbol]["last_price"]
    return c

def buy_fno_symbol(symbol,n,fno_symbol):
    c=ltp_fno_symbo(symbol)
    quantity=open_position_quantity(symbol,n)
    #quantity = get_quantity(symbol)
    print(c)
    print(type(n))
    print(quantity)
    print(symbol)
    symbol=symbol[4:]
    #quantity=n

    kite.place_order(variety='regular', exchange='NSE', tradingsymbol=symbol,
            transaction_type='BUY', quantity=quantity, product='MIS', order_type='MARKET', price=c+3, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    os.system('spd-say "buy order executed"')
    update_self(fno_symbol)
    exit()

def sell_fno_symbol(symbol,c,n,fno_symbol):
    #c=ltp_fno_symbo(symbol)
    #quantity = get_quantity(symbol)
    quantity= n
    symbol=symbol[4:]
    quantity=open_position_quantity(symbol,n)
    print("quantity")
    print(n)

    kite.place_order(variety='regular', exchange='NSE', tradingsymbol=symbol,
            transaction_type='SELL', quantity=quantity, product='MIS', order_type='MARKET', price=c-2, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    update_self(fno_symbol)
    os.system('spd-say "sell order executed"')
    exit()

def list_of_open_position():
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        if dic['quantity'] > 0:
            open_position_list.append(dic['tradingsymbol'])
    return open_position_list

def open_position_quantity(symbol,n):
    open_position_list = []
    pos = kite.positions()
    for dic in pos['net']:
        if dic['quantity'] > 0 and dic['tradingsymbol']==symbol:
            return dic['quantity']
    return n

def order(symbol,condition,price,action,fno_symbol,ltp_dict,n):
    #ltp_dict=get_ltp_dict(NIFTYFNO)
    c=ltp_dict[symbol]["last_price"]

    #if fno_symbol in list_of_open_position():
    #    return None

    if condition == "g":
        if c>price and action == "b":
            buy_fno_symbol(symbol,n,fno_symbol)
            update_self(fno_symbol)
        if c>price and action == "s":
            ltp_dic=get_open_position_price_dic(fno_symbol)
            sell_fno_symbol(symbol,ltp_dic[fno_symbol],n,fno_symbol)

    if condition == 'l':
        if c<price and action == "b":
            buy_fno_symbol(symbol,n,fno_symbol)
            update_self(fno_symbol)
        if c<price and action == "s":
            ltp_dic=get_open_position_price_dic(fno_symbol)
            c=ltp_fno_symbo(symbol)
            sell_fno_symbol(symbol,c,n,fno_symbol)

def update_self(symbol):
    with open('order_book_mis.py') as oldfile, open('order_new.py', 'w') as newfile:
        for line in oldfile:
            #print(line)
            if symbol not in line:
                newfile.write(line)
        newfile.close()
    os.system("cp order_new.py order_book_mis.py")
    if os.path.isfile(symbol):
        os.system("mv "+symbol+" readorder.txt")
    os.execv(sys.executable, ['python3'] + sys.argv)
    #os.execv(sys.argv[0], sys.argv)

def get_5min_20ma(symbol):
    toDate=datetime.today().strftime('%Y-%m-%d')
    toDate=toDate+" 15:35:00"
    fromDate = datetime.today() - relativedelta(days=7)
    fromDate = fromDate.strftime('%Y-%m-%d') + " 00:00:00"
    candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"5minute", continuous=False, oi=False)
    sma_list=[]
    for i in candle:
        c=i["close"]
        sma_list.append(c)
    sma20 = sum(sma_list[-20:])/20
    return sma20

def last_5min_ohlc(symbol):
    toDate=datetime.today().strftime('%Y-%m-%d')
    toDate=toDate+" 15:35:00"
    fromDate = datetime.today() - relativedelta(days=7)
    fromDate = fromDate.strftime('%Y-%m-%d') + " 00:00:00"
    candle = kite.historical_data(symbol_to_token[symbol], fromDate, toDate,"5minute", continuous=False, oi=False)
    o=candle[-1]["open"]
    h=candle[-1]["high"]
    l=candle[-1]["low"]
    c=candle[-1]["close"]
    return o,h,l,c

def buy_bull_20ma_5min(symbol,option,n):
    ma20=get_5min_20ma(symbol)
    o,h,l,c=last_5min_ohlc(symbol)
    if l<ma20 and o>ma20 and c>o:
        buy_fno_symbol(option,n)
        print(symbol)
        print("STOPLOSS")
        print(l)
    
def buy_bear_20ma_5min(symbol,option,n):
    ma20=get_5min_20ma(symbol)
    o,h,l,c=last_5min_ohlc(symbol)
    if h>ma20 and o<ma20 and c<o:
        buy_fno_symbol(option,n)
        print(symbol)
        print("STOPLOSS")
        print(h)

def gen_lot_size_dic():
    lot_dic={}
    for stock in NIFTYFNO:
        ls=nse_get_fno_lot_sizes(stock.replace("NSE:",""))
        print(ls)
        lot_dic[stock]=ls
    print(lot_dic)

def read_order():
    if os.path.isfile("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt"):
        selffile = open("/home/pankaj/Documents/stocks/kiteconnect/order_book_mis.py", "a")
        orderfile = open("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt", "r")
        selffile.write(orderfile.read())
        selffile.close()
        orderfile.close()
        os.system("rm readorder.txt")
        os.system("cat order_book_mis.py|tail -1")
        os.execv(sys.executable, ['python3'] + sys.argv)

print("running")
while True:
    time.sleep(0.5)
    read_order()
    ltpdict=get_ltp_dict(NIFTYFNO)
    #print(kite.positions())
    #track_sl()
    #order("NSE:FEDERALBNK","g",124.4,"b","FEDERALBNK22SEP120CE",ltp_dict)
    #order("NSE:IBULHSGFIN","g",177.65,"b","IBULHSGFIN24APRFUT",ltpdict,1)
