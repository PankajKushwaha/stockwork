import yfinance as yf
import pandas as pd
from nsetools import Nse
import mplfinance as mpf
from PIL import Image
from myLib import *
import glob
import img2pdf
import os

NIFTY50 = ["ACC","ADANIPORTS","AMBUJACEM","ASIANPAINT","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BHARTIARTL","BPCL","BOSCHLTD","BRITANNIA","CIPLA","COALINDIA","DIVISLAB","DRREDDY","EICHERMOT","GAIL","GRASIM","HCLTECH","HDFC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDUNILVR","ICICIBANK","INDUSINDBK","INFY","IOC","ITC","JSWSTEEL","KOTAKBANK","LT","M&M","MARUTI","NESTLEIND","NTPC","ONGC","POWERGRID","RELIANCE","SBILIFE","SBIN","SHREECEM","SUNPHARMA","TATAMOTORS","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]


NIFTY5 = ["ACC","ADANIPORTS","ESCORTS"]

for stock in NIFTY5:
    print(stock)
    stock="NSE:"+stock
    candle = get_candle(stock,"5minute")
    data=pd.DataFrame(candle)
    data.set_index('date', inplace=True)
    print(data)
    #data = yf.download(stock+".NS",period="300wk",interval="1wk")
    mpf.plot(data[100:],figratio=(20,12),type="candle",title=stock,mav=(200,20),tight_layout=True,style="yahoo",savefig=stock+".png"    ,xlim=(199,len(data)))

#for stock in NIFTY5:
#    image = Image.open(stock+".png")
#    image.show()

with open("name.pdf","wb") as f:
    f.write(img2pdf.convert(glob.glob("./*.png")))


os.system("mv name.pdf ~/Pictures")
