from pynse import *
import datetime
import shutil
import os
import pyautogui
import cv2
from datetime import date, timedelta


NIFTYFNO =  ['AUROPHARMA', 'AARTIIND', 'ADANIENT', 'ADANIPORTS', 'AMARAJABAT', 'AMBUJACEM', 'APLLTD', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY', 'ASIANPAINT', 'AUBANK', 'AXISBANK', 'BAJAJFINSV', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHEL', 'BIOCON', 'BRITANNIA', 'CADILAHC', 'CHOLAFIN', 'COALINDIA', 'CONCOR', 'CUMMINSIND', 'BANKBARODA', 'CANBK', 'COFORGE', 'COLPAL', 'DEEPAKNTR', 'DIVISLAB', 'DLF', 'FEDERALBNK', 'DRREDDY', 'EICHERMOT', 'ESCORTS', 'GAIL', 'GLENMARK', 'GODREJCP', 'GODREJPROP', 'GRANULES', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'ICICIBANK', 'ICICIPRULI', 'INDIGO', 'INDUSTOWER', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'KOTAKBANK', 'L&TFH', 'LT', 'LTTS', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARUTI', 'MCDOWELL-N', 'MFSL', 'MGL', 'MOTHERSUMI', 'MPHASIS', 'MRF', 'NAM-INDIA', 'NAUKRI', 'NAVINFLUOR', 'NESTLEIND', 'NTPC', 'ONGC', 'PAGEIND', 'PETRONET', 'PFIZER', 'PIDILITIND', 'PIIND', 'PVR', 'RBLBANK', 'RELIANCE', 'MINDTREE', 'SAIL', 'SBIN', 'SHREECEM', 'SRTRANSFIN', 'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAPOWER', 'TCS', 'TECHM', 'UBL', 'ULTRACEMCO', 'UPL', 'WIPRO', 'ACC', 'ALKEM', 'BAJFINANCE', 'BALKRISIND', 'BANDHANBNK', 'BATAINDIA', 'BHARTIARTL', 'HDFCLIFE', 'CUB', 'EXIDEIND', 'ICICIGI', 'IDFCFIRSTB', 'IGL', 'INDUSINDBK', 'IRCTC', 'LUPIN', 'GUJGASLTD', 'MARICO', 'LICHSGFIN', 'NATIONALUM', 'MUTHOOTFIN', 'NMDC', 'RAMCOCEM', 'SBILIFE', 'SRF', 'TATACONSUM', 'TATASTEEL', 'SIEMENS', 'TITAN', 'TRENT', 'TORNTPHARM', 'TVSMOTOR', 'BOSCHLTD', 'CIPLA', 'HAVELLS', 'INFY', 'LALPATHLAB', 'LTI', 'ZEEL', 'PEL', 'PNB', 'POWERGRID', 'RECLTD', 'BAJAJ-AUTO', 'TORNTPOWER', 'VEDL', 'GMRINFRA', 'PFC', 'VOLTAS', 'BPCL', 'DABUR', 'IBULHSGFIN', 'IDEA', 'ABFRL', 'COROMANDEL', 'INDHOTEL', 'METROPOLIS']

nse = Nse()

def get_bhav(dt):
    df = nse.bhavcopy(dt)
    df.reset_index(inplace=True)
    df =  df[df['SYMBOL'].isin(NIFTYFNO)]
    #date = df["DATE1"].tail(1).to_string(index=False)
    return df

def get_ohlc(symbol,df):
    o = float(df[df["SYMBOL"]==symbol]["OPEN_PRICE"])
    h = float(df[df["SYMBOL"]==symbol]["HIGH_PRICE"])
    l = float(df[df["SYMBOL"]==symbol]["LOW_PRICE"])
    c = float(df[df["SYMBOL"]==symbol]["CLOSE_PRICE"])
    return o,h,l,c 

def save_screenshot(stock_list,dir_name):
    full_dir_path = "/home/pankaj/Pictures/"+dir_name
    if os.path.isdir(full_dir_path):
        shutil.rmtree(full_dir_path)
    os.mkdir(full_dir_path)

    for stock in stock_list:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(1)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite(full_dir_path+"/"+stock+".png", image)

def green_hammer(df1):
    glist = []
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df1)
        if c>o and c>(h-((h-l)/10)) and o< (l+((h-l)/10)*6):
            glist.append(stock)

    #save_screenshot(glist,"green_hammer")

def red_hammer(df1):
    rlist = []
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df1)
        if o>c and c>(l+((h-l)/2)):
            rlist.append(stock)

    save_screenshot(rlist,"red_hammer")

def oel(df1):
    oellist = []
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df1)
        if o==l:
            oellist.append(stock)

    save_screenshot(oellist,"oel")

def big_green(df1):
    biggreen=[]
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df1)

        if c>o and (c-o)/(h-l) > 0.7:
            biggreen.append(stock)
    
    save_screenshot(biggreen,"biggreen")

def turning(df1,df2,df3,df4):
    turning=[]
    for stock in NIFTYFNO:
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        o3,h3,l3,c3 = get_ohlc(stock, df3)
        o4,h4,l4,c4 = get_ohlc(stock, df4)
        
        if l1>l2 and l2<l3 :
            turning.append(stock)
    
    save_screenshot(turning,"turning")


def lower_high(df1,df2,df3):
    lower_high=[]
    for stock in NIFTYFNO:
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        o3,h3,l3,c3 = get_ohlc(stock, df3)
        
        if l1>l2 and l2>l3 :
            lower_high.append(stock)
    save_screenshot(lower_high,"lower_high")

def higher_high(df1,df2,df3):
    higher_high=[]
    for stock in NIFTYFNO:
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        o3,h3,l3,c3 = get_ohlc(stock, df3)
        
        if h1>h2 and h2>h3 and l1>l2 and l2>l3 :
            h_diff = (h1-h2)/(h2-h3)
            l_diff = (l1-l2)/(l2-l3)
            if h_diff >0.4 and h_diff<1.6 and l_diff>0.4 and l_diff < 1.6:
                higher_high.append(stock)
            print(stock)
    save_screenshot(higher_high,"higher_high")

def pin_bar(df):
    pin_bar=[]
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df)

        gap = (h-l)/10
        
        if c>o and (l+3*gap)<o<(l+7*gap) and (l+3*gap)<c<(l+7*gap) :
            pin_bar.append(stock)
    save_screenshot(pin_bar,"pin_bar")

def bullish_engulf(df1,df2):
    bull_engulf=[]
    for stock in NIFTYFNO:
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        
        if o1<c1 and o2>c2 and o1<c2 and c1>o2 :
            bull_engulf.append(stock)
    save_screenshot(bull_engulf,"bull_engulf")

def doji(df):
    doji=[]
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df)
        
        if abs(o-c)<0.1 :
            doji.append(stock)
    save_screenshot(doji,"doji")

def bt(df,df1,df2,df3):
    bt=[]
    bt_dict={}
    for stock in NIFTYFNO:
        o,h,l,c = get_ohlc(stock, df)
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        o3,h3,l3,c3 = get_ohlc(stock, df3)

        if h<l+((l/100)*2) and c>o and (c-o)/(h-l) > 0.4:
            bt.append(stock)
    
    save_screenshot(bt,"bt")

#green after 5 red
def ga5r(df1,df2,df3,df4,df5,df6):
    gar = []
    for stock in NIFTYFNO:
        o1,h1,l1,c1 = get_ohlc(stock, df1)
        o2,h2,l2,c2 = get_ohlc(stock, df2)
        o3,h3,l3,c3 = get_ohlc(stock, df3)
        o4,h4,l4,c4 = get_ohlc(stock, df4)
        o5,h5,l5,c5 = get_ohlc(stock, df5)
        o6,h6,l6,c6 = get_ohlc(stock, df6)
        if c1>o1 and c2<o2 and c3<o3 and c4<o4 and c5<o5 and c6<o6:
            gar.append(stock)

    save_screenshot(gar,"gar")



print(datetime.date(2021,9,23))
dt1=datetime.date(2021,9,22)
dt2=datetime.date(2021,9,21)
dt3=datetime.date(2021,9,20)
df1=get_bhav(dt1)
df2=get_bhav(dt2)
df3=get_bhav(dt3)
higher_high(df1,df2,df3)



'''
#print(get_bhav(datetime.date(2021,7,23)))
df=get_bhav(datetime.date(2021,7,23))
print(get_ohlc("WIPRO",df))

df1=get_bhav(datetime.date(2021,7,29))
df2=get_bhav(datetime.date(2021,7,30))
df3=get_bhav(datetime.date(2021,9,12))
print((df3["DATE1"].tail(1).to_string(index=False)))
df4=get_bhav(datetime.date(2021,7,26))
df5=get_bhav(datetime.date(2021,7,23))
df6=get_bhav(datetime.date(2021,7,22))
#df1 is latest , df2 is one day ago , df3 is three day ago
red_hammer(df1)
oel(df1)
big_green(df1)

turning(df1,df2,df3,df4)
lower_high(df1,df2,df3)
higher_high(df1,df2,df3)
pin_bar(df1)
bullish_engulf(df1,df2)
doji(df1)
'''
#green_hammer(df1)
#pin_bar(df3)

