# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from random import randint

# 摇色子
def roll_dice(n=2):
    """
    摇色子
    :param n:色子个数，默认2
    :return: 点数之和
    """
    total = 0
    for i in range(0,n):
        total += randint(1,6)
    return total
def add(a=0, b=0, c=0):
    print("c[infun]:",c)

    return a + b + c

add(b=3)
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
# 不定长参数
# 在常熟名前的* 表示是不定长参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
print(add(2,3,4,5,1))

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()

def factory(n):
    """
    计算阶乘
    :param n:非负整数
    :return: 返回n的阶乘
    """
    result = 1
    for n in range(1,n+1):
        result *= n
    return result