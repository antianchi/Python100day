#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: atch
@Email: atc00@foxmail.com
@Date: 2019-05-27 16:04:18
@LastEditors: antch
@LastEditTime: 2019-05-27 16:10:06
@Description: 启动两个进程，一个输出Ping，一个输出Pong，两个进程输出的Ping和Pong加起来一共10个.
'''

from multiprocessing import Process
from time import sleep

counter = 0


def sub_task(string):
    global counter
    while counter < 10:
        print(string, end=" ", flush=True)
        counter += 1
        sleep(0.01)


def main():
    Process(target=sub_task, args=('Ping', )).start()
    Process(target=sub_task, args=('Pong', )).start()


if __name__ == '__main__':
    main()
