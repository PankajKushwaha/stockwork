import argparse
import pandas as pd
from kiteconnect import KiteConnect
from set_token import *


# Initialize Kite Connect API client
kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Function to fetch historical data and save to CSV
def fetch_and_save_ohlc_data(symbol, start_date, end_date, output_file):
    # Define instrument token for the symbol
    instrument_token = kite.ltp("NSE:" + symbol)["NSE:" + symbol]["instrument_token"]

    # Fetch historical data for the specified symbol and time frame
    historical_data = kite.historical_data(
        instrument_token,
        from_date=start_date,
        to_date=end_date,
        interval="5minute",
        continuous=False,
    )

    if not historical_data:
        print("No historical data available.")
        return

    # Convert historical data to a DataFrame
    df = pd.DataFrame(historical_data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

    print(f"OHLC data saved to {output_file}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Fetch and save OHLC data to CSV")
    parser.add_argument("symbol", type=str, help="Symbol name (e.g., INFY)")
    parser.add_argument("start_date", type=str, help="Start date (YYYY-MM-DD)")
    parser.add_argument("end_date", type=str, help="End date (YYYY-MM-DD)")
    parser.add_argument("output_file", type=str, help="Output CSV file name")
    args = parser.parse_args()

    # Call the function to fetch and save OHLC data
    fetch_and_save_ohlc_data(args.symbol, args.start_date, args.end_date, args.output_file)

