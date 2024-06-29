import yfinance as yf
import pandas as pd
import mplfinance as mpf


file_name = "Acc.csv"
data=pd.read_csv(file_name)
print(data.dtypes)

data.Date = pd.to_datetime(data.Date)
print(data.dtypes)
data.Date =  data.Date.dt.strftime('%d-%m-%y')
data.Date = pd.to_datetime(data.Date)
print(data.dtypes)
#print(data.Date)
data = data.set_index("Date")
mpf.plot(data,figratio=(8,4),type="candle",title="Reliance",mav=(200,20),tight_layout=True,style="yahoo",savefig="Reliance.png",scale_padding=0.2)
