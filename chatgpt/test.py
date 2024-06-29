from nsetools import Nse
import sys

def get_option_chain(stock_symbol):
    nse = Nse()
    
    try:
        option_data = nse.get_option_chain(stock_symbol)
    except Exception as e:
        print(f"Error fetching option chain data: {e}")
        return
    
    return option_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <stock_symbol>")
        sys.exit(1)
    
    stock_symbol = sys.argv[1].upper()
    option_chain = get_option_chain(stock_symbol)
    
    if option_chain:
        print(f"Option Chain for {stock_symbol}:")
        print(f"Expiry Date: {option_chain['records']['expiryDates'][0]}")
        print("\nCall Options:")
        for option in option_chain['records']['data'][0]['CE']:
            print(f"Symbol: {option['CE_SYMBOL']}, Strike Price: {option['CE_STRIKE_PRICE']}, Volume: {option['CE_VOL']}, Open Interest: {option['CE_OI']}")
        print("\nPut Options:")
        for option in option_chain['records']['data'][0]['PE']:
            print(f"Symbol: {option['PE_SYMBOL']}, Strike Price: {option['PE_STRIKE_PRICE']}, Volume: {option['PE_VOL']}, Open Interest: {option['PE_OI']}")

