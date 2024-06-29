import os
import sys

command = "echo "+ sys.argv[1] + ">>" + "orderlist.txt"
os.system(command)
os.system("cat orderlist.txt")
