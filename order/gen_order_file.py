import pickle

# format : symbol = [ "quantity","trigger price","sl","target"]

order = { 
        #"wipro": [2, 483.5,480.1,527.1 ] ,
        "bhartiartl": [9, 553.5,552,568 ] ,
        "ioc": [50, 97.8,97.2,103 ] ,
        "ntpc": [50, 108.6,108.2,113.3 ] ,
        "ongc": [40, 115,114.5,121 ] ,
        "sbilife": [5, 963,960,994 ] 
        }




pickle.dump( order , open( "order.p", "wb" ) )

favorite_color = pickle.load( open( "order.p", "rb" ) )

print(favorite_color)
