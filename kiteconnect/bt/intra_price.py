from kiteconnect import KiteConnect
from set_token import *

intraday_margin_info = kite.margins(segment="equity", tradingsymbol="RELIANCE")

# Extract intraday margin price
intraday_margin_price = intraday_margin_info['intraday']['enabled']['price']

print("Intraday Margin Price for RELIANCE:", intraday_margin_price)



# Initialize Kite Connect with your API key

# Fetch margin details for a specific stock (e.g., RELIANCE)
margin_details = kite.margins(segment="equity", tradingsymbol="RELIANCE")

# Print the margin details
print("Margin Details for RELIANCE:")
print("===================================")
print("Intraday Margin:")
print("  Enabled:", margin_details['intraday']['enabled'])
print("  Exposure:", margin_details['intraday']['exposure'])
print("  Price:", margin_details['intraday']['enabled']['price'])
print("-----------------------------------")
print("CO Margin:")
print("  Enabled:", margin_details['co']['enabled'])
print("  Exposure:", margin_details['co']['exposure'])
print("  Price:", margin_details['co']['enabled']['price'])
print("-----------------------------------")
print("BO Margin:")
print("  Enabled:", margin_details['bo']['enabled'])
print("  Exposure:", margin_details['bo']['exposure'])
print("  Price:", margin_details['bo']['enabled']['price'])

