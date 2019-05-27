#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: atch
@Email: atc00@foxmail.com
@Date: 2019-05-27 15:45:08
@LastEditors: antch
@LastEditTime: 2019-05-27 15:56:07
@Description: 多进程下载.
'''

from random import randint
from time import time,sleep
from os import getpid
from multiprocessing import Process

def download_task(filename):
    print('开始下载%s.....' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('[%s]下载完成，耗费了%d秒' % (filename,time_to_download))

def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

def dowanload_task2(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s.....' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('[%s]下载完成，耗费了%d秒' % (filename,time_to_download))

def main2():
    start = time()
    p1 = Process(target=dowanload_task2,args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=dowanload_task2,args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start)) 



if __name__=='__main__':
    main()
    print("-----------")
    main2()

