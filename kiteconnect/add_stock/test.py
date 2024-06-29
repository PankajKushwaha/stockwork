from nsepython import *
from pynse import *
my_list=list(nse_get_fno_lot_sizes().keys())

new_list = [item for item in my_list if "NIFTY" not in item]
print(new_list)
