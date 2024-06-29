import shutil
import os,os.path
import pyautogui
import time
import cv2
import numpy as np
from PIL import Image
from nsepython import *
import pandas as pd
import pickle

def get_niftyfno_list():
    fnolst=fnolist()
    fnolst.remove("NIFTYIT")
    fnolst.remove("BANKNIFTY")
    fnolst.remove("NIFTY")
    fnolst.sort()
    fnolst.insert(0, "NIFTY BANK")
    fnolst.insert(0, "NIFTY 50")
    return fnolst

def get_nifty50_lst():
    URL = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
    df = pd.read_csv(URL)
    dflst = df.Symbol.tolist()
    dflst.insert(0, "NIFTY BANK")
    dflst.insert(0, "NIFTY 50")
    return dflst

def get_list_of_all_file(folder):
    lst=[]
    for path, subdirs, files in os.walk(folder):
        for name in files:
            print(os.path.join(path, name))
            lst.append(os.path.join(path, name))
    return lst

def crop_image(location):
    im = Image.open(location)
    width, height = im.size
    left = 80
    top = 100
    right = width
    bottom = 740
    im1 = im.crop((left, top, right, bottom))
    filename = os.path.basename(location)
    im1.save(location)
    #im1.save(d+"crop_img/"+filename)

def crop_all_image():
    file_list=get_list_of_all_file("/home/pankaj/Pictures/")
    for file in file_list:
        crop_image(file)

def make_fullscreen():
    pyautogui.click(1228,46)

def total_number_of_file(folder):
    lst = os.listdir(folder) # dir is your directory path
    number_files = len(lst)
    return number_files

def rename_file(filename):
    lst = os.listdir("/home/pankaj/Videos") # dir is your directory path
    for i in lst:
        if "Screencast" in i:
            os.rename("/home/pankaj/Videos/"+i,"/home/pankaj/Videos/"+filename)

def open_single_image():
    pyautogui.click(33,317)
    time.sleep(2)
    pyautogui.click(143,280)
    time.sleep(1)
    pyautogui.moveTo(340,105)
    pyautogui.doubleClick()
    time.sleep(1)

def start_stop_recording():
    pyautogui.hotkey('ctrl', 'alt','shift', 'R')

def clean_and_create_folder():
    shutil.rmtree("/home/pankaj/Pictures")
    os.mkdir("/home/pankaj/Pictures")
    os.mkdir("/home/pankaj/Pictures/fno_day_clean")
    os.mkdir("/home/pankaj/Pictures/fno_hour_clean")
    os.mkdir("/home/pankaj/Pictures/fno_day_ma")
    os.mkdir("/home/pankaj/Pictures/fno_hour_ma")
    os.mkdir("/home/pankaj/Pictures/nifty50_day_clean")
    os.mkdir("/home/pankaj/Pictures/nifty50_hour_clean")
    os.mkdir("/home/pankaj/Pictures/nifty50_day_ma")
    os.mkdir("/home/pankaj/Pictures/nifty50_hour_ma")

def copy_nifty50_files(source_folder,list_to_copy,dst):
    for file in list_to_copy:
        shutil.copy("/home/pankaj/Pictures/"+source_folder+"/"+file+".png", "/home/pankaj/Pictures/"+dst)

def change_to_day_clean():
    pyautogui.click(800,125)
    time.sleep(1)
    pyautogui.click(845,370)

def change_to_hour_clean():
    pyautogui.click(800,125)
    time.sleep(1)
    pyautogui.click(840,390)

def change_to_day_ma():
    pyautogui.click(800,125)
    time.sleep(1)
    pyautogui.click(810,416)

def change_to_hour_ma():
    pyautogui.click(800,125)
    time.sleep(1)
    pyautogui.click(826,442)

def save_screenshot(lst,folder_name):
    for stock in lst:
        pyautogui.click(166,122)
        pyautogui.typewrite(stock)
        time.sleep(1)
        #pyautogui.typewrite(["enter"])
        pyautogui.click(167,206)
        #pyautogui.typewrite(["enter"])
        time.sleep(2)
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
        cv2.imwrite("/home/pankaj/Pictures/"+folder_name+"/"+stock+".png", image)

def go_to_proper_folder(folder):
    pyautogui.click(33,317)
    time.sleep(2)
    pyautogui.click(143,280)
    time.sleep(1)
    n=2
    if folder == "fno_day_clean" :
        pyautogui.moveTo(338,103)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        pyautogui.click(1091,83)
    if folder == "fno_day_ma" :
        pyautogui.moveTo(430,103)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        pyautogui.click(1091,83)
    if folder == "fno_hour_clean" :
        pyautogui.moveTo(521,106)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        pyautogui.click(1091,83)
    if folder == "fno_hour_ma" :
        pyautogui.moveTo(620,110)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        pyautogui.click(1091,83)
    if folder == "nifty50_day_clean" :
        pyautogui.moveTo(710,108)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        pyautogui.click(1091,83)
    if folder == "nifty50_day_ma" :
        pyautogui.moveTo(802,103)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(340,105)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        time.sleep(n)
        pyautogui.click(1091,83)
    if folder == "nifty50_hour_clean" :
        pyautogui.moveTo(896,103)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(336,90)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        time.sleep(n)
        pyautogui.click(1091,83)
    if folder == "nifty50_hour_ma" :
        pyautogui.moveTo(991,107)
        pyautogui.doubleClick()
        time.sleep(n)
        pyautogui.moveTo(336,90)
        pyautogui.doubleClick()
        time.sleep(n)
        make_fullscreen()
        time.sleep(n)
        pyautogui.click(1236,252)

def close_folder():
    pyautogui.click(1350,48)

def close_file():
    pyautogui.click(1214,81)

def make_video(folder):
    counter=0
    total_file = total_number_of_file("/home/pankaj/Pictures/"+folder)
    pyautogui.hotkey('ctrl', 'alt','shift', 'R')
    pyautogui.click(1150,385)
    time.sleep(1.5)
    print(counter)
    print(total_file)
    while counter < total_file:
        pyautogui.press('left')
        time.sleep(2)
        counter=counter+1
        print(counter)
    pyautogui.hotkey('ctrl', 'alt','shift', 'R')
    pyautogui.press('esc')
    close_file()
    close_folder()
    rename_file(folder)

def main_function():
    #clean_and_create_folder()
    fnolst = get_niftyfno_list()
    for i in fnolst:
        print(i)
    nifty50lst = get_nifty50_lst()
    #nifty50lst = ["RELIANCE","HCLTECH","WIPRO"]
    #fnolst = ["RELIANCE","HCLTECH","WIPRO","LTTS","ACC"]
    
    #change_to_day_clean()
    #save_screenshot(fnolst,"fno_day_clean")
    
    '''
    change_to_hour_clean()
    save_screenshot(fnolst,"fno_hour_clean")
    change_to_day_ma()
    save_screenshot(fnolst,"fno_day_ma")
    change_to_hour_ma()
    save_screenshot(fnolst,"fno_hour_ma")
    '''
    copy_nifty50_files("fno_day_clean",nifty50lst,"nifty50_day_clean")
    
    #copy_nifty50_files("fno_hour_clean",nifty50lst,"nifty50_hour_clean")
    #copy_nifty50_files("fno_day_ma",nifty50lst,"nifty50_day_ma")
    #copy_nifty50_files("fno_hour_ma",nifty50lst,"nifty50_hour_ma")

    #crop_all_image()
    go_to_proper_folder("fno_day_clean")
    make_video("fno_day_clean")
    '''
    go_to_proper_folder("fno_hour_clean")
    make_video("fno_hour_clean")
    go_to_proper_folder("fno_day_ma")
    make_video("fno_day_ma")
    go_to_proper_folder("fno_hour_ma")
    make_video("fno_hour_ma")
    '''
    go_to_proper_folder("nifty50_day_clean")
    make_video("nifty50_day_clean")
    '''
    go_to_proper_folder("nifty50_hour_clean")
    make_video("nifty50_hour_clean")
    go_to_proper_folder("nifty50_day_ma")
    make_video("nifty50_day_ma")
    go_to_proper_folder("nifty50_hour_ma")
    make_video("nifty50_hour_ma")
    '''

main_function()
