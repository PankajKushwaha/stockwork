# get list of close prices from symbol_docs. symbol_docs contain 2 min OHLC.
close_list = list(map(lambda a: a['close'], symbol_docs))

# sma20 and 200 calculated using ta-lib 
sma20 = sma(close_list, 20)
sma200 = sma(close_list, 200)  

# call to plot_chart function
plot_chart('TCS', symbol_docs, sma20, sma200)  

def plot_chart(symbol, docs, sma20, sma200):
  df = pd.DataFrame(docs)
  df = df.set_index(['time'])
  df.rename(columns={'open': 'Open', 'close': 'Close', 'high': 'High', 'low': 'Low'},
          inplace=True)
  title = symbol.upper() + ' - 2min'
  file = saved_chart_image_abs_path + symbol + '.png'

  df['sma20'] = sma20
  df['sma200'] = sma200

  df_sliced = df[-60:]
  apmavs = [mpf.make_addplot(df_sliced['sma20']), mpf.make_addplot(df_sliced['sma200'])]

  mpf.plot(df_sliced, type='candle', style='charles',
         title=title,
         ylabel='Price',
         ylabel_lower='Shares \nTraded',
         addplot=apmavs,
         savefig=file)
