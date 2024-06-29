import glob
import sys
import os
import time

folderName="/home/pankaj/Pictures/"+sys.argv[1]+"/scandata/*"

def getAllSymbol():
    filterLst=[]
    lst=glob.glob(folderName)
    for l in lst:
        filterLst.append(l.split(":")[1].split("_")[0])
    print(filterLst)
    return filterLst

def RunLoop():
    symbolLst=getAllSymbol()
    for symbol in symbolLst:
        os.system("python3 ./listfile.py "+symbol)
        time.sleep(2)
        os.system("python3 ./makereel.py")


RunLoop()
#getAllSymbol()
