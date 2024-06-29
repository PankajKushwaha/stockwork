import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
from datetime import datetime
from nsetools import Nse

nse = Nse()

conn = sqlite3.connect("stock.db")
cursor = conn.cursor()
disk_engine = create_engine('sqlite:///stock.db')


NIFTY5 = ["ACC","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UPL","WIPRO"]

for stock in NIFTY5:
    date_today = "'"+str(datetime.date(datetime.now()))+"'"
    q = nse.get_quote(stock)
    openPrice = q["open"]
    closePrice = q["lastPrice"]
    highPrice = q["dayHigh"]
    lowPrice = q["dayLow"]
    cursor=conn.execute('select * from '+stock+ ' where `Date` =' + date_today )
    if len(list(cursor)) > 0:
        conn.execute('delete from '+stock+ ' where `Date` =' + date_today )
        query = "INSERT INTO "+ stock +" (Date,Open,High,Low,Close) VALUES ("+date_today+","+str(openPrice)+","+str(highPrice)+","+str(lowPrice)+","+str(closePrice)+")" 
        conn.execute(query)
    else:
        query = "INSERT INTO "+ stock +" (Date,Open,High,Low,Close) VALUES ("+date_today+","+str(openPrice)+","+str(highPrice)+","+str(lowPrice)+","+str(closePrice)+")" 
        conn.execute("delete from "+ stock+ " limit 1")
        conn.execute(query)

for stock in NIFTY5:
    p2 = pd.read_sql('select * from '+stock ,  conn)
    print(p2)
