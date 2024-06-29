import sys


low_num = float(sys.argv[1])
high_num = float(sys.argv[2])


if high_num<(low_num+(low_num*0.002)):
    print("True")
else:
    print("False")
