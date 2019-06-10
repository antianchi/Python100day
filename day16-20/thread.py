#!/usr/bin/env python
# coding=UTF-8
#! python3
'''

Author: antch
Email: atc00@foxmail.com
Date: 2019-06-10 20:04:28
LastEditors: antch
LastEditTime: 2019-06-10 20:04:28
Description: 多线程.
面试题：进程和线程的区别和联系？
进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
线程 - 操作系统分配CPU的基本单位
并发编程（concurrent programming）
1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
**
多线程存在的问题
**
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺乏必要的保护措施就会导致数据错乱
说明：临界资源就是被多个线程竞争的资源
'''


import threading
import time
from random import randint

from concurrent.futures import ThreadPoolExecutor

class Account(object):
    """银行账户"""
    def __init__(self,balance):
        self.balance = balance
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
    
    def withdraw(self,money):
        """取钱"""
        with self.condition:
            while money > self.balance:
                self.condition.wait()
            new_balance = self.balance - money
            time.sleep(0.001)
            self.balance = new_balance
        

    def deposit(self,money):
        # 通过锁保护临界资源
        with self.condition:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance
            self.condition.notify_all()

def add_money(account):
    while True:
        money = randint(5, 10)
        account.deposit(money)
        print(threading.current_thread().name, 
              ':', money, '====>', account.balance)
        time.sleep(0.5)


def sub_money(account):
    while True:
        money = randint(10, 30)
        account.withdraw(money)
        print(threading.current_thread().name, 
              ':', money, '<====', account.balance)
        time.sleep(1)

class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self,account,money):
        self.account = account
        self.money = money
        # 自定义线程的初始化方法中必须调用父类的初始化方法
        super().__init__()
    
    def run(self):
        # 线程启动之后要执行的操作
        self.account.deposit(self.money)
    

def main():
    """主函数"""
    account = Account(10)
    # 创建线程池
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(5):
            pool.submit(add_money,account)
            pool.submit(sub_money,account)
    
   

if __name__ == '__main__':
    main()


