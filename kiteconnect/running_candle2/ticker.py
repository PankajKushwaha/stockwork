from kiteconnect import KiteTicker
from kiteconnect import KiteConnect
from set_token import *

# Define a callback function to handle the received ticks
def on_ticks(ticks):
    for tick in ticks:
        print("Received Tick:", tick)

# Define a callback function to handle the connection closed event
def on_close(ws, code, reason):
    print("Connection closed:", reason)

# Subscribe to the desired instruments
def subscribe():
    # Instrument tokens for the desired instruments (you can obtain these from the Kite Connect API)
    instruments = [256265, 256265]  # Example instruments
    kws.subscribe(instruments)

# Register the callback functions
kws.on_ticks = on_ticks
kws.on_close = on_close

# Connect to the WebSocket
kws.connect()

# Subscribe to instruments after connecting
subscribe()

