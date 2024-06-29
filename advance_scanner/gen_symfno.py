from nsetools import Nse
nse = Nse()
k=nse.get_fno_lot_sizes().keys()
stl = []
for i in k:
    st = str(i)
    stl.append(st)


print(stl)


