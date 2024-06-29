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

current_month = "JUN"
current_year  = "24"
lot_size={'EURINR': 1, 'GBPINR': 1, 'JPYINR': 1, 'USDINR': 1, 'BANKEX': 15, 'SENSEX': 10, 'SENSEX50': 25, '664GS2035': 1, '667GS2035': 1, '710GS2034': 1, '718GS2033': 1, '718GS2037': 1, '723GS2039': 1, '726GS2032': 1, '726GS2033': 1, '741GS2036': 1, '754GS2036': 1, '91DTB': 1, 'ONMIBOR': 1, 'ALUMINI': 1, 'ALUMINIUM': 1, 'COPPER': 1, 'COTTONCNDY': 1, 'CRUDEOIL': 1, 'CRUDEOILM': 1, 'GOLD': 1, 'GOLDGUINEA': 1, 'GOLDM': 1, 'GOLDPETAL': 1, 'KAPAS': 1, 'LEAD': 1, 'LEADMINI': 1, 'MCXBULLDEX': 1, 'MCXMETLDEX': 1, 'MENTHAOIL': 1, 'NATGASMINI': 1, 'NATURALGAS': 1, 'NICKEL': 1, 'SILVER': 1, 'SILVERM': 1, 'SILVERMIC': 1, 'STEELREBAR': 1, 'ZINC': 1, 'ZINCMINI': 1, 'GOLD1G': 1, 'WTICRUDE': 1, 'WTICRUDEM': 1, 'NIFTY': 25, 'BANKNIFTY': 15, 'AARTIIND': 1000, 'ABB': 125, 'ABBOTINDIA': 20, 'ABCAPITAL': 5400, 'ABFRL': 2600, 'ACC': 300, 'ADANIENT': 300, 'ADANIPORTS': 400, 'ALKEM': 100, 'AMBUJACEM': 900, 'APOLLOHOSP': 125, 'APOLLOTYRE': 1700, 'ASHOKLEY': 5000, 'ASIANPAINT': 200, 'ASTRAL': 367, 'ATUL': 100, 'AUBANK': 1000, 'AUROPHARMA': 550, 'AXISBANK': 625, 'BAJAJ-AUTO': 75, 'BAJAJFINSV': 500, 'BAJFINANCE': 125, 'BALKRISIND': 300, 'BALRAMCHIN': 1600, 'BANDHANBNK': 2800, 'BANKBARODA': 2925, 'BATAINDIA': 375, 'BEL': 2850, 'BERGEPAINT': 1320, 'BHARATFORG': 500, 'BHARTIARTL': 475, 'BHEL': 2625, 'BIOCON': 2500, 'BOSCHLTD': 25, 'BPCL': 900, 'BRITANNIA': 200, 'BSOFT': 1000, 'CANBK': 1350, 'CANFINHOME': 975, 'CHAMBLFERT': 1900, 'CHOLAFIN': 625, 'CIPLA': 650, 'COALINDIA': 2100, 'COFORGE': 150, 'COLPAL': 350, 'CONCOR': 1000, 'COROMANDEL': 700, 'CROMPTON': 1800, 'CUB': 5000, 'CUMMINSIND': 300, 'DABUR': 1250, 'DALBHARAT': 275, 'DEEPAKNTR': 300, 'DIVISLAB': 200, 'DIXON': 100, 'DLF': 825, 'DRREDDY': 125, 'EICHERMOT': 175, 'ESCORTS': 275, 'EXIDEIND': 1800, 'FEDERALBNK': 5000, 'FINNIFTY': 40, 'GAIL': 4575, 'GLENMARK': 725, 'GMRINFRA': 11250, 'GNFC': 1300, 'GODREJCP': 500, 'GODREJPROP': 225, 'GRANULES': 2000, 'GRASIM': 250, 'GUJGASLTD': 1250, 'HAL': 300, 'HAVELLS': 500, 'HCLTECH': 350, 'HDFCAMC': 150, 'HDFCBANK': 550, 'HDFCLIFE': 1100, 'HEROMOTOCO': 150, 'HINDALCO': 1400, 'HINDCOPPER': 2650, 'HINDPETRO': 1350, 'HINDUNILVR': 300, 'ICICIBANK': 700, 'ICICIGI': 500, 'ICICIPRULI': 1500, 'IDEA': 40000, 'IDFC': 5000, 'IDFCFIRSTB': 7500, 'IEX': 3750, 'IGL': 1375, 'INDHOTEL': 1000, 'INDIACEM': 2900, 'INDIAMART': 300, 'INDIGO': 300, 'INDUSINDBK': 500, 'INDUSTOWER': 3400, 'INFY': 400, 'IOC': 4875, 'IPCALAB': 650, 'IRCTC': 875, 'ITC': 1600, 'JINDALSTEL': 625, 'JKCEMENT': 125, 'JSWSTEEL': 675, 'JUBLFOOD': 1250, 'KOTAKBANK': 400, 'LALPATHLAB': 300, 'LAURUSLABS': 1700, 'LICHSGFIN': 1000, 'LT': 150, 'LTF': 4462, 'LTIM': 150, 'LTTS': 100, 'LUPIN': 425, 'M&M': 350, 'M&MFIN': 2000, 'MANAPPURAM': 3000, 'MARICO': 1200, 'MARUTI': 50, 'MCDOWELL-N': 700, 'MCX': 200, 'METROPOLIS': 400, 'MFSL': 800, 'MGL': 400, 'MIDCPNIFTY': 75, 'MOTHERSON': 7100, 'MPHASIS': 275, 'MRF': 5, 'MUTHOOTFIN': 550, 'NATIONALUM': 3750, 'NAUKRI': 150, 'NAVINFLUOR': 175, 'NESTLEIND': 200, 'NIFTYNXT50': 10, 'NMDC': 4500, 'NTPC': 1500, 'OBEROIRLTY': 700, 'OFSS': 100, 'ONGC': 1925, 'PAGEIND': 15, 'PEL': 750, 'PERSISTENT': 200, 'PETRONET': 3000, 'PFC': 1300, 'PIDILITIND': 250, 'PIIND': 250, 'PNB': 8000, 'POLYCAB': 125, 'POWERGRID': 3600, 'PVRINOX': 407, 'RAMCOCEM': 850, 'RBLBANK': 2500, 'RECLTD': 2000, 'RELIANCE': 250, 'SAIL': 4000, 'SBICARD': 800, 'SBILIFE': 375, 'SBIN': 750, 'SHREECEM': 25, 'SHRIRAMFIN': 300, 'SIEMENS': 150, 'SRF': 375, 'SUNPHARMA': 350, 'SUNTV': 1500, 'SYNGENE': 1000, 'TATACHEM': 550, 'TATACOMM': 500, 'TATACONSUM': 450, 'TATAMOTORS': 550, 'TATAPOWER': 1350, 'TATASTEEL': 5500, 'TCS': 175, 'TECHM': 600, 'TITAN': 175, 'TORNTPHARM': 250, 'TRENT': 200, 'TVSMOTOR': 350, 'UBL': 400, 'ULTRACEMCO': 100, 'UPL': 1300, 'VEDL': 2300, 'VOLTAS': 600, 'WIPRO': 1500, 'ZEEL': 3000, 'ZYDUSLIFE': 900}



NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']

symbol_to_token={'NSE:AARTIIND': 1793, 'NSE:ABB': 3329, 'NSE:ABBOTINDIA': 4583169, 'NSE:ABCAPITAL': 5533185, 'NSE:ABFRL': 7707649, 'NSE:ACC': 5633, 'NSE:ADANIENT': 6401, 'NSE:ADANIPORTS': 3861249, 'NSE:ALKEM': 2995969, 'NSE:AMARAJABAT': 25601, 'NSE:AMBUJACEM': 325121, 'NSE:APOLLOHOSP': 40193, 'NSE:APOLLOTYRE': 41729, 'NSE:ASHOKLEY': 54273, 'NSE:ASIANPAINT': 60417, 'NSE:ASTRAL': 3691009, 'NSE:ATUL': 67329, 'NSE:AUBANK': 5436929, 'NSE:AUROPHARMA': 70401, 'NSE:AXISBANK': 1510401, 'NSE:BAJAJ-AUTO': 4267265, 'NSE:BAJAJFINSV': 4268801, 'NSE:BAJFINANCE': 81153, 'NSE:BALKRISIND': 85761, 'NSE:BALRAMCHIN': 87297, 'NSE:BANDHANBNK': 579329, 'NSE:BANKBARODA': 1195009, 'NSE:BATAINDIA': 94977, 'NSE:BEL': 98049, 'NSE:BERGEPAINT': 103425, 'NSE:BHARATFORG': 108033, 'NSE:BHARTIARTL': 2714625, 'NSE:BHEL': 112129, 'NSE:BIOCON': 2911489, 'NSE:BOSCHLTD': 558337, 'NSE:BPCL': 134657, 'NSE:BRITANNIA': 140033, 'NSE:BSOFT': 1790465, 'NSE:CANBK': 2763265, 'NSE:CANFINHOME': 149249, 'NSE:CHAMBLFERT': 163073, 'NSE:CHOLAFIN': 175361, 'NSE:CIPLA': 177665, 'NSE:COALINDIA': 5215745, 'NSE:COFORGE': 2955009, 'NSE:COLPAL': 3876097, 'NSE:CONCOR': 1215745, 'NSE:COROMANDEL': 189185, 'NSE:CROMPTON': 4376065, 'NSE:CUB': 1459457, 'NSE:CUMMINSIND': 486657, 'NSE:DABUR': 197633, 'NSE:DALBHARAT': 2067201, 'NSE:DEEPAKNTR': 5105409, 'NSE:DELTACORP': 3851265, 'NSE:DIVISLAB': 2800641, 'NSE:DIXON': 5552641, 'NSE:DLF': 3771393, 'NSE:DRREDDY': 225537, 'NSE:EICHERMOT': 232961, 'NSE:ESCORTS': 245249, 'NSE:EXIDEIND': 173057, 'NSE:FEDERALBNK': 261889, 'NSE:FSL': 3661825, 'NSE:GAIL': 1207553, 'NSE:GLENMARK': 1895937, 'NSE:GMRINFRA': 3463169, 'NSE:GNFC': 300545, 'NSE:GODREJCP': 2585345, 'NSE:GODREJPROP': 4576001, 'NSE:GRANULES': 3039233, 'NSE:GRASIM': 315393, 'NSE:GSPL': 3378433, 'NSE:GUJGASLTD': 2713345, 'NSE:HAL': 589569, 'NSE:HAVELLS': 2513665, 'NSE:HCLTECH': 1850625, 'NSE:HDFC': 340481, 'NSE:HDFCAMC': 1086465, 'NSE:HDFCBANK': 341249, 'NSE:HDFCLIFE': 119553, 'NSE:HEROMOTOCO': 345089, 'NSE:HINDALCO': 348929, 'NSE:HINDCOPPER': 4592385, 'NSE:HINDPETRO': 359937, 'NSE:HINDUNILVR': 356865, 'NSE:HONAUT': 874753, 'NSE:IBULHSGFIN': 7712001, 'NSE:ICICIBANK': 1270529, 'NSE:ICICIGI': 5573121, 'NSE:ICICIPRULI': 4774913, 'NSE:IDEA': 3677697, 'NSE:IDFC': 3060993, 'NSE:IDFCFIRSTB': 2863105, 'NSE:IEX': 56321, 'NSE:IGL': 2883073, 'NSE:INDHOTEL': 387073, 'NSE:INDIACEM': 387841, 'NSE:INDIAMART': 2745857, 'NSE:INDIGO': 2865921, 'NSE:INDUSINDBK': 1346049, 'NSE:INDUSTOWER': 7458561, 'NSE:INFY': 408065, 'NSE:INTELLECT': 1517057, 'NSE:IOC': 415745, 'NSE:IPCALAB': 418049, 'NSE:IRCTC': 3484417, 'NSE:ITC': 424961, 'NSE:JINDALSTEL': 1723649, 'NSE:JKCEMENT': 3397121, 'NSE:JSWSTEEL': 3001089, 'NSE:JUBLFOOD': 4632577, 'NSE:KOTAKBANK': 492033, 'NSE:L&TFH': 6386689, 'NSE:LALPATHLAB': 2983425, 'NSE:LAURUSLABS': 4923905, 'NSE:LICHSGFIN': 511233, 'NSE:LT': 2939649, 'NSE:LTI': 4561409, 'NSE:LTTS': 4752385, 'NSE:LUPIN': 2672641, 'NSE:M&M': 519937, 'NSE:M&MFIN': 3400961, 'NSE:MANAPPURAM': 4879617, 'NSE:MARICO': 1041153, 'NSE:MARUTI': 2815745, 'NSE:MCDOWELL-N': 2674433, 'NSE:MCX': 7982337, 'NSE:METROPOLIS': 2452737, 'NSE:MFSL': 548353, 'NSE:MGL': 4488705, 'NSE:MINDTREE': 3675137, 'NSE:MOTHERSON': 1076225, 'NSE:MPHASIS': 1152769, 'NSE:MRF': 582913, 'NSE:MUTHOOTFIN': 6054401, 'NSE:NAM-INDIA': 91393, 'NSE:NATIONALUM': 1629185, 'NSE:NAUKRI': 3520257, 'NSE:NAVINFLUOR': 3756033, 'NSE:NBCC': 8042241, 'NSE:NESTLEIND': 4598529, 'NSE:NMDC': 3924993, 'NSE:NTPC': 2977281, 'NSE:OBEROIRLTY': 5181953, 'NSE:OFSS': 2748929, 'NSE:ONGC': 633601, 'NSE:PAGEIND': 3689729, 'NSE:PEL': 617473, 'NSE:PERSISTENT': 4701441, 'NSE:PETRONET': 2905857, 'NSE:PFC': 3660545, 'NSE:PIDILITIND': 681985, 'NSE:PIIND': 6191105, 'NSE:PNB': 2730497, 'NSE:POLYCAB': 2455041, 'NSE:POWERGRID': 3834113, 'NSE:PVR': 3365633, 'NSE:RAIN': 3926273, 'NSE:RAMCOCEM': 523009, 'NSE:RBLBANK': 4708097, 'NSE:RECLTD': 3930881, 'NSE:RELIANCE': 738561, 'NSE:SAIL': 758529, 'NSE:SBICARD': 4600577, 'NSE:SBILIFE': 5582849, 'NSE:SBIN': 779521, 'NSE:SHREECEM': 794369, 'NSE:SIEMENS': 806401, 'NSE:SRF': 837889, 'NSE:SRTRANSFIN': 1102337, 'NSE:SUNPHARMA': 857857, 'NSE:SUNTV': 3431425, 'NSE:SYNGENE': 2622209, 'NSE:TATACHEM': 871681, 'NSE:TATACOMM': 952577, 'NSE:TATACONSUM': 878593, 'NSE:TATAMOTORS': 884737, 'NSE:TATAPOWER': 877057, 'NSE:TATASTEEL': 895745, 'NSE:TCS': 2953217, 'NSE:TECHM': 3465729, 'NSE:TITAN': 897537, 'NSE:TORNTPHARM': 900609, 'NSE:TORNTPOWER': 3529217, 'NSE:TRENT': 502785, 'NSE:TVSMOTOR': 2170625, 'NSE:UBL': 4278529, 'NSE:ULTRACEMCO': 2952193, 'NSE:UPL': 2889473, 'NSE:VEDL': 784129, 'NSE:VOLTAS': 951809, 'NSE:WHIRLPOOL': 4610817, 'NSE:WIPRO': 969473, 'NSE:ZEEL': 975873, 'NSE:ZYDUSLIFE': 2029825}

token_to_symbol = {1793: 'NSE:AARTIIND', 3329: 'NSE:ABB', 4583169: 'NSE:ABBOTINDIA', 5533185: 'NSE:ABCAPITAL', 7707649: 'NSE:ABFRL', 5633: 'NSE:ACC', 6401: 'NSE:ADANIENT', 3861249: 'NSE:ADANIPORTS', 2995969: 'NSE:ALKEM', 25601: 'NSE:AMARAJABAT', 325121: 'NSE:AMBUJACEM', 40193: 'NSE:APOLLOHOSP', 41729: 'NSE:APOLLOTYRE', 54273: 'NSE:ASHOKLEY', 60417: 'NSE:ASIANPAINT', 3691009: 'NSE:ASTRAL', 67329: 'NSE:ATUL', 5436929: 'NSE:AUBANK', 70401: 'NSE:AUROPHARMA', 1510401: 'NSE:AXISBANK', 4267265: 'NSE:BAJAJ-AUTO', 4268801: 'NSE:BAJAJFINSV', 81153: 'NSE:BAJFINANCE', 85761: 'NSE:BALKRISIND', 87297: 'NSE:BALRAMCHIN', 579329: 'NSE:BANDHANBNK', 1195009: 'NSE:BANKBARODA', 94977: 'NSE:BATAINDIA', 98049: 'NSE:BEL', 103425: 'NSE:BERGEPAINT', 108033: 'NSE:BHARATFORG', 2714625: 'NSE:BHARTIARTL', 112129: 'NSE:BHEL', 2911489: 'NSE:BIOCON', 558337: 'NSE:BOSCHLTD', 134657: 'NSE:BPCL', 140033: 'NSE:BRITANNIA', 1790465: 'NSE:BSOFT', 2763265: 'NSE:CANBK', 149249: 'NSE:CANFINHOME', 163073: 'NSE:CHAMBLFERT', 175361: 'NSE:CHOLAFIN', 177665: 'NSE:CIPLA', 5215745: 'NSE:COALINDIA', 2955009: 'NSE:COFORGE', 3876097: 'NSE:COLPAL', 1215745: 'NSE:CONCOR', 189185: 'NSE:COROMANDEL', 4376065: 'NSE:CROMPTON', 1459457: 'NSE:CUB', 486657: 'NSE:CUMMINSIND', 197633: 'NSE:DABUR', 2067201: 'NSE:DALBHARAT', 5105409: 'NSE:DEEPAKNTR', 3851265: 'NSE:DELTACORP', 2800641: 'NSE:DIVISLAB', 5552641: 'NSE:DIXON', 3771393: 'NSE:DLF', 225537: 'NSE:DRREDDY', 232961: 'NSE:EICHERMOT', 245249: 'NSE:ESCORTS', 173057: 'NSE:EXIDEIND', 261889: 'NSE:FEDERALBNK', 3661825: 'NSE:FSL', 1207553: 'NSE:GAIL', 1895937: 'NSE:GLENMARK', 3463169: 'NSE:GMRINFRA', 300545: 'NSE:GNFC', 2585345: 'NSE:GODREJCP', 4576001: 'NSE:GODREJPROP', 3039233: 'NSE:GRANULES', 315393: 'NSE:GRASIM', 3378433: 'NSE:GSPL', 2713345: 'NSE:GUJGASLTD', 589569: 'NSE:HAL', 2513665: 'NSE:HAVELLS', 1850625: 'NSE:HCLTECH', 340481: 'NSE:HDFC', 1086465: 'NSE:HDFCAMC', 341249: 'NSE:HDFCBANK', 119553: 'NSE:HDFCLIFE', 345089: 'NSE:HEROMOTOCO', 348929: 'NSE:HINDALCO', 4592385: 'NSE:HINDCOPPER', 359937: 'NSE:HINDPETRO', 356865: 'NSE:HINDUNILVR', 874753: 'NSE:HONAUT', 7712001: 'NSE:IBULHSGFIN', 1270529: 'NSE:ICICIBANK', 5573121: 'NSE:ICICIGI', 4774913: 'NSE:ICICIPRULI', 3677697: 'NSE:IDEA', 3060993: 'NSE:IDFC', 2863105: 'NSE:IDFCFIRSTB', 56321: 'NSE:IEX', 2883073: 'NSE:IGL', 387073: 'NSE:INDHOTEL', 387841: 'NSE:INDIACEM', 2745857: 'NSE:INDIAMART', 2865921: 'NSE:INDIGO', 1346049: 'NSE:INDUSINDBK', 7458561: 'NSE:INDUSTOWER', 408065: 'NSE:INFY', 1517057: 'NSE:INTELLECT', 415745: 'NSE:IOC', 418049: 'NSE:IPCALAB', 3484417: 'NSE:IRCTC', 424961: 'NSE:ITC', 1723649: 'NSE:JINDALSTEL', 3397121: 'NSE:JKCEMENT', 3001089: 'NSE:JSWSTEEL', 4632577: 'NSE:JUBLFOOD', 492033: 'NSE:KOTAKBANK', 6386689: 'NSE:L&TFH', 2983425: 'NSE:LALPATHLAB', 4923905: 'NSE:LAURUSLABS', 511233: 'NSE:LICHSGFIN', 2939649: 'NSE:LT', 4561409: 'NSE:LTI', 4752385: 'NSE:LTTS', 2672641: 'NSE:LUPIN', 519937: 'NSE:M&M', 3400961: 'NSE:M&MFIN', 4879617: 'NSE:MANAPPURAM', 1041153: 'NSE:MARICO', 2815745: 'NSE:MARUTI', 2674433: 'NSE:MCDOWELL-N', 7982337: 'NSE:MCX', 2452737: 'NSE:METROPOLIS', 548353: 'NSE:MFSL', 4488705: 'NSE:MGL', 3675137: 'NSE:MINDTREE', 1076225: 'NSE:MOTHERSON', 1152769: 'NSE:MPHASIS', 582913: 'NSE:MRF', 6054401: 'NSE:MUTHOOTFIN', 91393: 'NSE:NAM-INDIA', 1629185: 'NSE:NATIONALUM', 3520257: 'NSE:NAUKRI', 3756033: 'NSE:NAVINFLUOR', 8042241: 'NSE:NBCC', 4598529: 'NSE:NESTLEIND', 3924993: 'NSE:NMDC', 2977281: 'NSE:NTPC', 5181953: 'NSE:OBEROIRLTY', 2748929: 'NSE:OFSS', 633601: 'NSE:ONGC', 3689729: 'NSE:PAGEIND', 617473: 'NSE:PEL', 4701441: 'NSE:PERSISTENT', 2905857: 'NSE:PETRONET', 3660545: 'NSE:PFC', 681985: 'NSE:PIDILITIND', 6191105: 'NSE:PIIND', 2730497: 'NSE:PNB', 2455041: 'NSE:POLYCAB', 3834113: 'NSE:POWERGRID', 3365633: 'NSE:PVR', 3926273: 'NSE:RAIN', 523009: 'NSE:RAMCOCEM', 4708097: 'NSE:RBLBANK', 3930881: 'NSE:RECLTD', 738561: 'NSE:RELIANCE', 758529: 'NSE:SAIL', 4600577: 'NSE:SBICARD', 5582849: 'NSE:SBILIFE', 779521: 'NSE:SBIN', 794369: 'NSE:SHREECEM', 806401: 'NSE:SIEMENS', 837889: 'NSE:SRF', 1102337: 'NSE:SRTRANSFIN', 857857: 'NSE:SUNPHARMA', 3431425: 'NSE:SUNTV', 2622209: 'NSE:SYNGENE', 871681: 'NSE:TATACHEM', 952577: 'NSE:TATACOMM', 878593: 'NSE:TATACONSUM', 884737: 'NSE:TATAMOTORS', 877057: 'NSE:TATAPOWER', 895745: 'NSE:TATASTEEL', 2953217: 'NSE:TCS', 3465729: 'NSE:TECHM', 897537: 'NSE:TITAN', 900609: 'NSE:TORNTPHARM', 3529217: 'NSE:TORNTPOWER', 502785: 'NSE:TRENT', 2170625: 'NSE:TVSMOTOR', 4278529: 'NSE:UBL', 2952193: 'NSE:ULTRACEMCO', 2889473: 'NSE:UPL', 784129: 'NSE:VEDL', 951809: 'NSE:VOLTAS', 4610817: 'NSE:WHIRLPOOL', 969473: 'NSE:WIPRO', 975873: 'NSE:ZEEL', 2029825: 'NSE:ZYDUSLIFE'}

def get_quantity(stock):
    return lot_size[stock.upper()] 

def symbol_to_fnosymbol(symbol):
    print(current_month)
    return symbol.upper()+current_year+current_month+"FUT"

def buy_fno_symbol(symbol,n):
    quantity = get_quantity(symbol)
    symbol=symbol_to_fnosymbol(symbol)
    print(symbol)
    quantity=int(quantity)*n
    print(quantity)

    kite.place_order(variety='regular', exchange='NFO', tradingsymbol=symbol,
            transaction_type='BUY', quantity=quantity, product='NRML', order_type='MARKET', price=None, validity='DAY',
            disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
    print(symbol + " buy order executed")
    os.system('spd-say "buy order executed"')
    exit()

buy_fno_symbol(sys.argv[1],1)
#python3 buy_future.py wipro
