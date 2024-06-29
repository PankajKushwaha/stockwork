from kiteconnect import KiteConnect
from set_token import *
import pickle
import time
from operator import itemgetter
kite=set_token()


NIFTYFNO=['NSE:ABB','NSE:HONAUT','NSE:DALBHARAT','NSE:GODREJCP','NSE:BAJFINANCE','NSE:BAJAJFINSV','NSE:BRITANNIA','NSE:AUBANK','NSE:TRENT','NSE:GUJGASLTD','NSE:INTELLECT','NSE:HINDUNILVR','NSE:ESCORTS','NSE:DIXON','NSE:BATAINDIA','NSE:ICICIGI','NSE:CONCOR','NSE:APOLLOTYRE','NSE:WHIRLPOOL','NSE:EICHERMOT','NSE:RAMCOCEM','NSE:HINDPETRO','NSE:M&MFIN','NSE:SIEMENS','NSE:HEROMOTOCO','NSE:SBICARD','NSE:IDEA','NSE:ASIANPAINT','NSE:IEX','NSE:GODREJPROP','NSE:ZEEL','NSE:HAVELLS','NSE:CUMMINSIND','NSE:TITAN','NSE:MARUTI','NSE:UBL','NSE:COROMANDEL','NSE:ABBOTINDIA','NSE:BERGEPAINT','NSE:PERSISTENT','NSE:JKCEMENT','NSE:ABCAPITAL','NSE:LTTS','NSE:DELTACORP','NSE:AARTIIND','NSE:MRF','NSE:KOTAKBANK','NSE:BOSCHLTD','NSE:INDIACEM','NSE:TATACONSUM','NSE:LICHSGFIN','NSE:COLPAL','NSE:SHREECEM','NSE:BPCL','NSE:PAGEIND','NSE:SUNTV','NSE:RBLBANK','NSE:FSL','NSE:BAJAJ-AUTO','NSE:PIIND','NSE:GLENMARK','NSE:BIOCON','NSE:NAUKRI','NSE:M&M','NSE:ADANIPORTS','NSE:MGL','NSE:HDFCAMC','NSE:DLF','NSE:VOLTAS','NSE:OBEROIRLTY','NSE:IBULHSGFIN','NSE:L&TFH','NSE:MCDOWELL-N','NSE:NESTLEIND','NSE:INDUSTOWER','NSE:PIDILITIND','NSE:DABUR','NSE:MPHASIS','NSE:GMRINFRA','NSE:IPCALAB','NSE:MFSL','NSE:CANBK','NSE:OFSS','NSE:APOLLOHOSP','NSE:PETRONET','NSE:COFORGE','NSE:POLYCAB','NSE:ICICIPRULI','NSE:GRASIM','NSE:SBIN','NSE:BHEL','NSE:MINDTREE','NSE:LTI','NSE:TVSMOTOR','NSE:CROMPTON','NSE:AUROPHARMA','NSE:INDUSINDBK','NSE:BANDHANBNK','NSE:MARICO','NSE:ULTRACEMCO','NSE:IDFCFIRSTB','NSE:MOTHERSON','NSE:INDIGO','NSE:AMARAJABAT','NSE:TORNTPOWER','NSE:ALKEM','NSE:TCS','NSE:INDIAMART','NSE:LAURUSLABS','NSE:ACC','NSE:ASHOKLEY','NSE:METROPOLIS','NSE:IRCTC','NSE:HDFCBANK','NSE:NBCC','NSE:DEEPAKNTR','NSE:DIVISLAB','NSE:TATACOMM','NSE:HINDCOPPER','NSE:AXISBANK','NSE:NATIONALUM','NSE:JUBLFOOD','NSE:BHARTIARTL','NSE:IGL','NSE:TATAMOTORS','NSE:IDFC','NSE:ABFRL','NSE:ZYDUSLIFE','NSE:ICICIBANK','NSE:TATACHEM','NSE:INFY','NSE:BANKBARODA','NSE:RECLTD','NSE:UPL','NSE:ADANIENT','NSE:HDFC','NSE:BEL','NSE:TECHM','NSE:JINDALSTEL','NSE:GNFC','NSE:BALKRISIND','NSE:PEL','NSE:CIPLA','NSE:NAM-INDIA','NSE:NAVINFLUOR','NSE:FEDERALBNK','NSE:ITC','NSE:PNB','NSE:CANFINHOME','NSE:MANAPPURAM','NSE:WIPRO','NSE:EXIDEIND','NSE:MCX','NSE:TATAPOWER','NSE:CHAMBLFERT','NSE:HCLTECH','NSE:JSWSTEEL','NSE:SBILIFE','NSE:ASTRAL','NSE:AMBUJACEM','NSE:INDHOTEL','NSE:SUNPHARMA','NSE:SRF','NSE:TORNTPHARM','NSE:GSPL','NSE:LALPATHLAB','NSE:CUB','NSE:SRTRANSFIN','NSE:CHOLAFIN','NSE:GAIL','NSE:SAIL','NSE:LUPIN','NSE:RAIN','NSE:DRREDDY','NSE:PFC','NSE:TATASTEEL','NSE:MUTHOOTFIN','NSE:PVR','NSE:BHARATFORG','NSE:LT','NSE:SYNGENE','NSE:COALINDIA','NSE:GRANULES','NSE:HAL','NSE:ATUL','NSE:RELIANCE','NSE:NTPC','NSE:HDFCLIFE','NSE:HINDALCO','NSE:VEDL','NSE:BSOFT','NSE:IOC','NSE:POWERGRID','NSE:NMDC','NSE:BALRAMCHIN','NSE:ONGC']


#token_to_symbol = {4278529: 'NSE:UBL',3675137: 'NSE:MINDTREE',2983425: 'NSE:LALPATHLAB',4632577: 'NSE:JUBLFOOD',2452737: 'NSE:METROPOLIS',112129: 'NSE:BHEL',2995969: 'NSE:ALKEM',232961: 'NSE:EICHERMOT',189185: 'NSE:COROMANDEL',2952193: 'NSE:ULTRACEMCO',1459457: 'NSE:CUB',2763265: 'NSE:CANBK',5633: 'NSE:ACC',2955009: 'NSE:COFORGE',325121: 'NSE:AMBUJACEM',81153: 'NSE:BAJFINANCE',523009: 'NSE:RAMCOCEM',5573121: 'NSE:ICICIGI',94977: 'NSE:BATAINDIA',3484417: 'NSE:IRCTC',900609: 'NSE:TORNTPHARM',3861249: 'NSE:ADANIPORTS',315393: 'NSE:GRASIM',4268801: 'NSE:BAJAJFINSV',502785: 'NSE:TRENT',7458561: 'NSE:INDUSTOWER',676609: 'NSE:PFIZER',3529217: 'NSE:TORNTPOWER',6401: 'NSE:ADANIENT',4598529: 'NSE:NESTLEIND',1215745: 'NSE:CONCOR',878593: 'NSE:TATACONSUM',2911489: 'NSE:BIOCON',3756033: 'NSE:NAVINFLUOR',582913: 'NSE:MRF',486657: 'NSE:CUMMINSIND',2513665: 'NSE:HAVELLS',3691009: 'NSE:ASTRAL',1041153: 'NSE:MARICO',140033: 'NSE:BRITANNIA',1102337: 'NSE:SRTRANSFIN',1195009: 'NSE:BANKBARODA',2863105: 'NSE:IDFCFIRSTB',1793: 'NSE:AARTIIND',177665: 'NSE:CIPLA',794369: 'NSE:SHREECEM',3520257: 'NSE:NAUKRI',3689729: 'NSE:PAGEIND',119553: 'NSE:HDFCLIFE',3771393: 'NSE:DLF',681985: 'NSE:PIDILITIND',415745: 'NSE:IOC',4488705: 'NSE:MGL',5105409: 'NSE:DEEPAKNTR',2953217: 'NSE:TCS',738561: 'NSE:RELIANCE',2889473: 'NSE:UPL',197633: 'NSE:DABUR',3930881: 'NSE:RECLTD',103425: 'NSE:BERGEPAINT',4774913: 'NSE:ICICIPRULI',1086465: 'NSE:HDFCAMC',91393: 'NSE:NAM-INDIA',356865: 'NSE:HINDUNILVR',424961: 'NSE:ITC',897537: 'NSE:TITAN',2905857: 'NSE:PETRONET',1152769: 'NSE:MPHASIS',3463169: 'NSE:GMRINFRA',2800641: 'NSE:DIVISLAB',6386689: 'NSE:L&TFH',617473: 'NSE:PEL',359937: 'NSE:HINDPETRO',519937: 'NSE:M&M',3465729: 'NSE:TECHM',951809: 'NSE:VOLTAS',857857: 'NSE:SUNPHARMA',4752385: 'NSE:LTTS',3660545: 'NSE:PFC',6054401: 'NSE:MUTHOOTFIN',558337: 'NSE:BOSCHLTD',25601: 'NSE:AMARAJABAT',4561409: 'NSE:LTI',341249: 'NSE:HDFCBANK',2585345: 'NSE:GODREJCP',261889: 'NSE:FEDERALBNK',387073: 'NSE:INDHOTEL',1895937: 'NSE:GLENMARK',173057: 'NSE:EXIDEIND',7707649: 'NSE:ABFRL',2672641: 'NSE:LUPIN',225537: 'NSE:DRREDDY',3400961: 'NSE:M&MFIN',895745: 'NSE:TATASTEEL',134657: 'NSE:BPCL',2939649: 'NSE:LT',877057: 'NSE:TATAPOWER',60417: 'NSE:ASIANPAINT',408065: 'NSE:INFY',345089: 'NSE:HEROMOTOCO',5215745: 'NSE:COALINDIA',2977281: 'NSE:NTPC',633601: 'NSE:ONGC',871681: 'NSE:TATACHEM',2714625: 'NSE:BHARTIARTL',779521: 'NSE:SBIN',2865921: 'NSE:INDIGO',3924993: 'NSE:NMDC',2815745: 'NSE:MARUTI',3365633: 'NSE:PVR',6191105: 'NSE:PIIND',1887745: 'NSE:STAR',1510401: 'NSE:AXISBANK',511233: 'NSE:LICHSGFIN',2883073: 'NSE:IGL',175361: 'NSE:CHOLAFIN',41729: 'NSE:APOLLOTYRE',1850625: 'NSE:HCLTECH',3001089: 'NSE:JSWSTEEL',85761: 'NSE:BALKRISIND',969473: 'NSE:WIPRO',2713345: 'NSE:GUJGASLTD',54273: 'NSE:ASHOKLEY',340481: 'NSE:HDFC',4708097: 'NSE:RBLBANK',1076225: 'NSE:MOTHERSUMI',108033: 'NSE:BHARATFORG',3876097: 'NSE:COLPAL',4576001: 'NSE:GODREJPROP',6483969: 'NSE:APLLTD',579329: 'NSE:BANDHANBNK',3431425: 'NSE:SUNTV',975873: 'NSE:ZEEL',1346049: 'NSE:INDUSINDBK',3039233: 'NSE:GRANULES',806401: 'NSE:SIEMENS',2170625: 'NSE:TVSMOTOR',5436929: 'NSE:AUBANK',758529: 'NSE:SAIL',1207553: 'NSE:GAIL',548353: 'NSE:MFSL',98049: 'NSE:BEL',837889: 'NSE:SRF',3834113: 'NSE:POWERGRID',2730497: 'NSE:PNB',884737: 'NSE:TATAMOTORS',70401: 'NSE:AUROPHARMA',245249: 'NSE:ESCORTS',5582849: 'NSE:SBILIFE',1723649: 'NSE:JINDALSTEL',1270529: 'NSE:ICICIBANK',4879617: 'NSE:MANAPPURAM',348929: 'NSE:HINDALCO',492033: 'NSE:KOTAKBANK',40193: 'NSE:APOLLOHOSP',784129: 'NSE:VEDL',1629185: 'NSE:NATIONALUM',7712001: 'NSE:IBULHSGFIN'}
#symbol_to_token = {'NSE:UBL': 4278529,'NSE:NSE:MINDTREE': 3675137,'NSE:NSE:LALPATHLAB': 2983425,'NSE:NSE:JUBLFOOD': 4632577,'NSE:NSE:METROPOLIS': 2452737,'NSE:NSE:BHEL': 112129,'NSE:NSE:ALKEM': 2995969,'NSE:NSE:EICHERMOT': 232961,'NSE:NSE:COROMANDEL': 189185,'NSE:NSE:ULTRACEMCO': 2952193,'NSE:NSE:CUB': 1459457,'NSE:NSE:CANBK': 2763265,'NSE:NSE:ACC': 5633,'NSE:NSE:COFORGE': 2955009,'NSE:NSE:AMBUJACEM': 325121,'NSE:NSE:BAJFINANCE': 81153,'NSE:NSE:RAMCOCEM': 523009,'NSE:NSE:ICICIGI': 5573121,'NSE:NSE:BATAINDIA': 94977,'NSE:NSE:IRCTC': 3484417,'NSE:NSE:TORNTPHARM': 900609,'NSE:NSE:ADANIPORTS': 3861249,'NSE:NSE:GRASIM': 315393,'NSE:NSE:BAJAJFINSV': 4268801,'NSE:NSE:TRENT': 502785,'NSE:NSE:INDUSTOWER': 7458561,'NSE:NSE:PFIZER': 676609,'NSE:NSE:TORNTPOWER': 3529217,'NSE:NSE:ADANIENT': 6401,'NSE:NSE:NESTLEIND': 4598529,'NSE:NSE:CONCOR': 1215745,'NSE:NSE:TATACONSUM': 878593,'NSE:NSE:BIOCON': 2911489,'NSE:NSE:NAVINFLUOR': 3756033,'NSE:NSE:MRF': 582913,'NSE:NSE:CUMMINSIND': 486657,'NSE:NSE:HAVELLS': 2513665,'NSE:NSE:ASTRAL': 3691009,'NSE:NSE:MARICO': 1041153,'NSE:NSE:BRITANNIA': 140033,'NSE:NSE:SRTRANSFIN': 1102337,'NSE:NSE:BANKBARODA': 1195009,'NSE:NSE:IDFCFIRSTB': 2863105,'NSE:NSE:AARTIIND': 1793,'NSE:NSE:CIPLA': 177665,'NSE:NSE:SHREECEM': 794369,'NSE:NSE:NAUKRI': 3520257,'NSE:NSE:PAGEIND': 3689729,'NSE:NSE:HDFCLIFE': 119553,'NSE:NSE:DLF': 3771393,'NSE:NSE:PIDILITIND': 681985,'NSE:NSE:IOC': 415745,'NSE:NSE:MGL': 4488705,'NSE:NSE:DEEPAKNTR': 5105409,'NSE:NSE:TCS': 2953217,'NSE:NSE:RELIANCE': 738561,'NSE:NSE:UPL': 2889473,'NSE:NSE:DABUR': 197633,'NSE:NSE:RECLTD': 3930881,'NSE:NSE:BERGEPAINT': 103425,'NSE:NSE:ICICIPRULI': 4774913,'NSE:NSE:HDFCAMC': 1086465,'NSE:NSE:NAM-INDIA': 91393,'NSE:NSE:HINDUNILVR': 356865,'NSE:NSE:ITC': 424961,'NSE:NSE:TITAN': 897537,'NSE:NSE:PETRONET': 2905857,'NSE:NSE:MPHASIS': 1152769,'NSE:NSE:GMRINFRA': 3463169,'NSE:NSE:DIVISLAB': 2800641,'NSE:NSE:L&TFH': 6386689,'NSE:NSE:PEL': 617473,'NSE:NSE:HINDPETRO': 359937,'NSE:NSE:M&M': 519937,'NSE:NSE:TECHM': 3465729,'NSE:NSE:VOLTAS': 951809,'NSE:NSE:SUNPHARMA': 857857,'NSE:NSE:LTTS': 4752385,'NSE:NSE:PFC': 3660545,'NSE:NSE:MUTHOOTFIN': 6054401,'NSE:NSE:BOSCHLTD': 558337,'NSE:NSE:AMARAJABAT': 25601,'NSE:NSE:LTI': 4561409,'NSE:NSE:HDFCBANK': 341249,'NSE:NSE:GODREJCP': 2585345,'NSE:NSE:FEDERALBNK': 261889,'NSE:NSE:INDHOTEL': 387073,'NSE:NSE:GLENMARK': 1895937,'NSE:NSE:EXIDEIND': 173057,'NSE:NSE:ABFRL': 7707649,'NSE:NSE:LUPIN': 2672641,'NSE:NSE:DRREDDY': 225537,'NSE:NSE:M&MFIN': 3400961,'NSE:NSE:TATASTEEL': 895745,'NSE:NSE:BPCL': 134657,'NSE:NSE:LT': 2939649,'NSE:NSE:TATAPOWER': 877057,'NSE:NSE:ASIANPAINT': 60417,'NSE:NSE:INFY': 408065,'NSE:NSE:HEROMOTOCO': 345089,'NSE:NSE:COALINDIA': 5215745,'NSE:NSE:NTPC': 2977281,'NSE:NSE:ONGC': 633601,'NSE:NSE:TATACHEM': 871681,'NSE:NSE:BHARTIARTL': 2714625,'NSE:NSE:SBIN': 779521,'NSE:NSE:INDIGO': 2865921,'NSE:NSE:NMDC': 3924993,'NSE:NSE:MARUTI': 2815745,'NSE:NSE:PVR': 3365633,'NSE:NSE:PIIND': 6191105,'NSE:NSE:STAR': 1887745,'NSE:NSE:AXISBANK': 1510401,'NSE:NSE:LICHSGFIN': 511233,'NSE:NSE:IGL': 2883073,'NSE:NSE:CHOLAFIN': 175361,'NSE:NSE:APOLLOTYRE': 41729,'NSE:NSE:HCLTECH': 1850625,'NSE:NSE:JSWSTEEL': 3001089,'NSE:NSE:BALKRISIND': 85761,'NSE:NSE:WIPRO': 969473,'NSE:NSE:GUJGASLTD': 2713345,'NSE:NSE:ASHOKLEY': 54273,'NSE:NSE:HDFC': 340481,'NSE:NSE:RBLBANK': 4708097,'NSE:NSE:MOTHERSUMI': 1076225,'NSE:NSE:BHARATFORG': 108033,'NSE:NSE:COLPAL': 3876097,'NSE:NSE:GODREJPROP': 4576001,'NSE:NSE:APLLTD': 6483969,'NSE:NSE:BANDHANBNK': 579329,'NSE:NSE:SUNTV': 3431425,'NSE:NSE:ZEEL': 975873,'NSE:NSE:INDUSINDBK': 1346049,'NSE:NSE:GRANULES': 3039233,'NSE:NSE:SIEMENS': 806401,'NSE:NSE:TVSMOTOR': 2170625,'NSE:NSE:AUBANK': 5436929,'NSE:NSE:SAIL': 758529,'NSE:NSE:GAIL': 1207553,'NSE:NSE:MFSL': 548353,'NSE:NSE:BEL': 98049,'NSE:NSE:SRF': 837889,'NSE:NSE:POWERGRID': 3834113,'NSE:NSE:PNB': 2730497,'NSE:NSE:TATAMOTORS': 884737,'NSE:NSE:AUROPHARMA': 70401,'NSE:NSE:ESCORTS': 245249,'NSE:NSE:SBILIFE': 5582849,'NSE:NSE:JINDALSTEL': 1723649,'NSE:NSE:ICICIBANK': 1270529,'NSE:NSE:MANAPPURAM': 4879617,'NSE:NSE:HINDALCO': 348929,'NSE:NSE:KOTAKBANK': 492033,'NSE:NSE:APOLLOHOSP': 40193,'NSE:NSE:VEDL': 784129,'NSE:NSE:NATIONALUM': 1629185,'NSE:NSE:IBULHSGFIN': 7712001}

def is_00_between(l,h):
    il=int(l)
    ih=int(h)
    while True:
        if il%1000 == 0:
            return True
        il = il+1
        if il==ih:
            break
    return False

def get_ltp_dict(fnolist):
    token_to_symbol={}
    symbol_to_token={}
    ltp_dict=kite.ltp(fnolist)
    for i in ltp_dict:
        print(i)
        print(ltp_dict[i]["instrument_token"])
        token_to_symbol[ltp_dict[i]["instrument_token"]]=i
        symbol_to_token[i]=ltp_dict[i]["instrument_token"]
    print(token_to_symbol)
    print(symbol_to_token)

get_ltp_dict(NIFTYFNO)
#print(kite.instruments())
'''
list_to_monitor=[]
ohlc=kite.ohlc(fnolist)
for symbol in fnolist:
    print(symbol)
    candle = kite.historical_data(symbol_to_token[symbol],"2022-07-04 00:00:00","2022-07-07 15:15:00","5minute",continuous=False,oi=False)
    #print(candle)
    #print(kite.historical_data(symbol_to_token[symbol],"2022-03-02 00:00:00","2022-03-02 15:15:00","hour",continuous=False,oi=False))
    sma_list=[]
    for i in candle:
        o=i["open"]
        h=i["high"]
        l=i["low"]
        c=i["close"]
        sma_list.append(c)
    sma200 = sum(sma_list[-200:])/200
    sma40 = sum(sma_list[-40:])/40
    sma20 = sum(sma_list[-20:])/20
    if sma20>sma40 and sma40>sma200 and c > sma20:
        list_to_monitor.append(symbol)
    if sma20<sma40 and sma40<sma200 and c < sma20:
        list_to_monitor.append(symbol)

print(list_to_monitor)
'''
