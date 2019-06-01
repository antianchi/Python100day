#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-31 16:51:28
LastEditors: antch
LastEditTime: 2019-05-31 16:51:28
Description: 常用算法.

'''


def a1():
    """
    穷举法 - 又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。
    例子：
    公鸡5元一只 母鸡3元一只 小鸡1元三只
    用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
    """
    for x in range(20):
        for y in range(33):
            # Z 表示只数
            z = 100 -x -y
         
            if 5 * x + 3 * y +  z // 3 == 100 and z % 3 == 0:
                print(x,y,z)


if __name__=='__main__':
    a1()