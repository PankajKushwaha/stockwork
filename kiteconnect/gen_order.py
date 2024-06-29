import sys
from set_token import *
#order("NSE:"+"RBALBANK","g",302.1,"b","RBALBANK22SEP130CE",ltp_dict)
#gen_order.py rblbank g 302.1 b 130 ce

print("python3 gen_order.py  rblbank g 300 b 310 ce")

symbol="NSE:"+sys.argv[1].upper()
fno_symbol="NFO:"+sys.argv[1].upper() + "23MAR"+sys.argv[5]+sys.argv[6].upper()

print(symbol)
print(fno_symbol)

symbol_price=kite.ltp(symbol)
fnosymbol_price=kite.ltp(fno_symbol)

if not bool(symbol_price):
    sys.exit()

if not bool(fnosymbol_price):
    sys.exit()

print(kite.ltp(symbol))
print(kite.ltp(fno_symbol))
print("")
print("")

s = "order(\"NSE:"+sys.argv[1].upper()+"\""+ ",\"" + sys.argv[2] + "\"" + "," + sys.argv[3] + ","+ "\"" + sys.argv[4] +"\"" +"," + "\"" + sys.argv[1].upper() + "23MAR"+sys.argv[5]+sys.argv[6].upper()+"\"" +",ltp_dict," +sys.argv[7]+ ")"

print(s)
print("")
print("")

with open("readorder.txt", "w") as text_file:
    text_file.write("    "+s+"\n")
    print("")
