import os
import sys

def update_order(symbol):
    with open('orderlist.txt',"a") as oldfile, open('order_new.py', 'w') as newfile:
        for line in oldfile:
                print(line)
                if symbol not in line:
                    newfile.write(line)
        newfile.close()
    os.system("cp order_new.py orderlist.py")

update_order(sys.argv[1])

