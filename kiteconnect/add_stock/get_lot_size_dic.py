from nsepython import *
from pynse import *
print(nse_get_fno_lot_sizes()["BSOFT"])
print(list(nse_get_fno_lot_sizes().keys()))
lst = list(nse_get_fno_lot_sizes().keys())
lst_op=[]
for i in lst:
    lst_op.append("NSE:"+i)
print(lst_op)
'''
my_list=list(nse_get_fno_lot_sizes().keys())

new_list = [item for item in my_list if "NIFTY" not in item]
print(new_list)
'''

