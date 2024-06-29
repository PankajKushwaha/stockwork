import sys


h = float(sys.argv[1])
l = float(sys.argv[2])

max_loss = 900

#print(h-(h/100))

per_loss = ((l-h)*100)/h

print(per_loss)


loss_per_share = h-l

quantity_for_one_rs_loss = 1/loss_per_share
quantity_for_max_loss = quantity_for_one_rs_loss*max_loss
print(int(quantity_for_max_loss))
 
hv = h*int(quantity_for_max_loss) 
#print(hv)
lv=hv-((hv/100)*(abs(per_loss)))
#print(hv-((hv/100)*(abs(per_loss))))

#print(((lv-hv)*100 )/hv)
