import os

def read_order():
    if os.path.isfile("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt"):
        selffile = open("/home/pankaj/Documents/stocks/kiteconnect/order_book_exp.py", "a")
        orderfile = open("/home/pankaj/Documents/stocks/kiteconnect/readorder.txt", "r")
        selffile.write(orderfile.read()) 
        os.system("rm readorder.txt")
        os.execv(sys.executable, ['python3'] + sys.argv)

read_order()
