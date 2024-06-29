import os
import time
import sys
import shutil
from glob import glob

def getFilesContainSubstr():
    result = [y for x in os.walk("/home/pankaj/Pictures") for y in glob(os.path.join(x[0], '*.png'))]
    matching = [r for r in result if sys.argv[1].upper() in r]
    matchingSort=sorted(matching, key=lambda t: os.stat(t).st_mtime)
    print(matchingSort)
    return matchingSort

def makeReelDir():
    count=1
    path="/home/pankaj/Pictures/reel"
    shutil.rmtree(path)
    os.mkdir(path)
    filelst=getFilesContainSubstr()

    for file in filelst:
        command="cp --preserve=timestamps "+file+" "+path+"/"+str(count)+"_"+sys.argv[1]+".png"
        print(command)
        os.system(command)
        count=count+1
        time.sleep(1)

makeReelDir()

