from datetime import date
import os

def getDateDirName():
    today = date.today()
    d1 = today.strftime("%d%m%Y")
    os.makedirs("/home/pankaj/Pictures/"+d1)
    return "/home/Pictures/"+d1

print(getDateDirName())
