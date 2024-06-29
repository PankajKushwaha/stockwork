from set_token import *
from myLib import *
import pandas as pd

NIFTY_FNO=get_fno_list_new()
base_df = pd.DataFrame()
print(NIFTY_FNO)

time.sleep(wait_for_5min())
write_current_time_to_file()
print(get_token_to_instrument(NIFTY_FNO))
print(get_instrument_to_token(NIFTY_FNO))

for symbol in NIFTY_FNO:
    print(symbol)
    hist_df=pd.DataFrame(get_candle(symbol,"5minute"))
    hist_df=hist_df[-500:-1]
    #hist_df = hist_df.drop(['date','volume'], axis=1)
    hist_df = hist_df.drop(['volume'], axis=1)
    hist_df = hist_df.rename(columns={'date': 'Timestamp'})
    #hist_df = hist_df.rename(columns={'open': symbol+'_open'})
    #hist_df = hist_df.rename(columns={'high': symbol+'_high'})
    #hist_df = hist_df.rename(columns={'low': symbol+'_low'})
    #hist_df = hist_df.rename(columns={'close': symbol+'_close'})
    #print(hist_df)
    hist_df['Timestamp'] = hist_df['Timestamp'].dt.tz_localize(None)
    hist_df.insert(0, 'Instrument', symbol)
    base_df = pd.concat([base_df, hist_df], axis=0)
    print(base_df)

base_df.rename(columns={'Instrument': 'instrument'}, inplace=True)
base_df.rename(columns={'Timestamp': 'timestamp'}, inplace=True)
base_df.to_csv('base_df.csv', index=False)

