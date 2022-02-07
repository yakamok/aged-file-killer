#!/usr/bin/env python

import pathlib
from datetime import datetime
import glob
import time
import os
import sys
import shutil

days = sys.argv[1] # age of files to remove in days
WatchedLocation = "/path/dir/files*"

#check input is numeric, reject otherwise
if days.isnumeric():
    print("true")
else:
    print("shite")
    exit(0)

ToLive = int(days) * int(86400)

print(ToLive)
def checkAgeOfFile(filename):
    fname = pathlib.Path(filename)
    
    if (int(time.time()) - fname.stat()[-1:][0]) > ToLive:
        return True
    else: 
        return False


def deleteFilesNFolders(location):
    if os.path.isdir(location):
        print("This is a dir: " + location)
        shutil.rmtree(location)
    if os.path.isfile(location):
        print("This is a file: " + location)
        os.remove(location)


for x in glob.glob(WatchedLocation):
    print(x)
    if checkAgeOfFile(x):
        print(x)
        deleteFilesNFolders(x)
