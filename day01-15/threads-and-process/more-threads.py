#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: atch
@Email: atc00@foxmail.com
@Date: 2019-05-27 16:12:23
@LastEditors: antch
@LastEditTime: 2019-05-27 16:51:44
@Description: Python中的多线程.
'''

from random import randint, random
from threading import Thread,Lock
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('[%s]下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    # 直接使用threading模块的Thread类来创建线程
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


class DownloadTask(Thread):
    """
    tong通过继承的方式实现多线程
    """

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('[%s]下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main2():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 闲获得锁喉才能执行后续的代码
        self._lock.acquire()
        try:
            # 计算存款后的余额
            new_balance = self._balance + money
            # 模拟受理存款业务需要的时间0.01
            # random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
            sleep(random())
            # 修改账户余额
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()


    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        print('存钱---')
        self._account.deposit(self._money)


def main3():
    account = Account()
    threads = []
    # 创建100个存款的线程向一个账户存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # 等待所有线程都执行完毕
    for t in threads:
        t.join()

    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main3()
