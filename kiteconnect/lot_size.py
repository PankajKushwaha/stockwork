from nsepython import *
from set_token import *
#print(nse_get_fno_lot_sizes("pnb"))

lst=kite.instruments()
lot_size = {}


def get_lot_size()
    for i in lst:
        if i["tradingsymbol"][-3:] == "FUT":
            #print(i)
            print(i["tradingsymbol"])
            lot_size[i["name"]]=i["lot_size"]
    return lot_size
