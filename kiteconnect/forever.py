#!/usr/local/lib/python3.7
from subprocess import Popen
import sys
import os
import time
import urllib.request

filename = sys.argv[1]

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def play_sound():
    duration = 0.2  # seconds
    freq = 440  # Hz
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    time.sleep(30)

while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()

    if connect():
        time.sleep(1)
    else:
        time.sleep(300)
    #play_sound()
