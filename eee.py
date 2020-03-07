#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import operator
import csv
import time
import threading
from time import ctime
import os
import shutil

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
def read_file(filpos,i):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    file_name = salt + '.txt'
    f = open(file_name, 'w')
    f.close()

def read_folder(filpos,i):
    file_name = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    os.mkdir(file_name)

threads = []
x=0
for t in range(0,10000):
    t= threading.Thread(target=read_file,args=(basedir,x))
    threads.append(t)
    x+=1

y=0
for t in range(0,100):
    t= threading.Thread(target=read_folder,args=(basedir,y))
    threads.append(t)
    y+=1



#join在里面时候只有第一个子进程结束才能打开第二个进程,if__name__ 调用时不可用
if __name__=="__main__":
    for thr in threads:
        thr.start()
    # thr.join()
    for folderName, subfolders, filenames in os.walk(basedir):
        print(subfolders)
        
        z=0
        j=0
        for filename in filenames:
            if '.txt' in filename:
                print(filename)
                try:
                    shutil.move(folderName + '\\'+filename,subfolders[j])
                    z+=1
                    if z%100==0:
                        z=0
                        j+=1
                except OSError:
                    pass
    print("all over %s"%ctime())