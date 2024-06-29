from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save

# Download bhavcopy
#bhavcopy_save(date(2020,1,1), "/home/pankaj/Documents/stocks/fno_bhavcopy")

# Download bhavcopy for futures and options
bhavcopy_fo_save(date(2021,6,28), "/home/pankaj/Documents/stocks/fno_bhavcopy")

# Download stock data to pandas dataframe
