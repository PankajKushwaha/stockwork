from datetime import date
import os

def getTodayDate():
    today = date.today()
    d = today.strftime("%d%m%Y")
    return d

def makeDateDir():
    d=getTodayDate()
    command1="/home/pankaj/Pictures/"+d+"/scandata"
    command2="/home/pankaj/Pictures/"+d+"/alldata"
    os.makedirs(command1)
    os.makedirs(command2)

def saveScanData():
    d=getTodayDate()
    command="mv /home/pankaj/Pictures/*.png "+"/home/pankaj/Pictures/"+d+"/scandata"
    os.system(command)

def saveAllData():
    d=getTodayDate()
    os.system("python3 /home/pankaj/Documents/stocks/save_screenshot.py")
    command="mv /home/pankaj/Pictures/*.png "+"/home/pankaj/Pictures/"+d+"/alldata"
    os.system(command)

def main_function():
    makeDateDir()
    saveScanData()
    saveAllData()

main_function()


