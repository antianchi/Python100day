#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-06-03 09:48:36
LastEditors: antch
LastEditTime: 2019-06-03 09:48:36
Description: 函数使用.
将函数视为“一等公民”

-》函数可以赋值给变量
-》函数可以作为函数的参数
-》函数可以作为函数的返回值

#高阶函数的用法（filter、map以及它们的替代品）
items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
items2 = [x ** 2 for x in range(1, 10) if x % 2]


闭包和作用域问题：
Python搜索变量的LEGB顺序（Local --> Embedded --> Global --> Built-in）

global和nonlocal关键字的作用

-》global：声明或定义全局变量（要么直接使用现有的全局作用域的变量，要么定义一个变量放到全局作用域）。

-》nonlocal：声明使用嵌套作用域的变量（嵌套作用域必须存在该变量，否则报错）。


装饰器函数（使用装饰器和取消装饰器）：
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前
提下增加额外功能，装饰器的返回值也是一个函数对象。
装饰器经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验
等场景。

概括的讲，装饰器的作用就是为已经存在的函数或对象添加额外的功能。


'''
from time import time,sleep
from functools import wraps
import random
from threading import Lock


def record_time(func):
    """自定义  装饰函数  的 装饰器"""
    # @wraps(func)
    def wrapper(*args, **kwargs): 
        start = time()
        print("传入的参数的值：",*args)
        result = func(*args, **kwargs)
        print(f'{func.__name__} : {time()-start}秒')
        return result
    return wrapper

@record_time
def a(n):
    print(n)
    num = n -2
    print(num)
    print(num)
    print(num)
    print(num)
    print(num)
    print(f"yuan原始的n{n}")
    print(f"hello{num}")
    return n ** 3

def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print("hello {}!".format(something))

@debug
def say2(h):
    print(f'say2,cansdhu{h}')


# 高级装饰器
# 带参数的装饰器
def logging(level):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args,**kwargs):
            print(f"[{level}]:eneter function {func.__name__}")
            return func(*args,**kwargs)
        return inner_wrapper
    return wrapper

@logging("INFO-MYINFO")
def haha(something):
    print(f"我就是想说一些事情，看能不能具有INFO级别的日志,某个人说的事情：{something}")



#  函数定义顺序会影响解释器的执行，若haha2_test，定义在
# haha2 = logging("DEBUG")(haha2_test)之后就会报错

def haha2_test(s):
    print(f"参数{s}")

# 没有使用@语法
haha2 = logging("DEBUG")(haha2_test)







def record(output):
    """自定义带参数的装饰器"""
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **k):
            start = time()
            result = func(*args, **k)
            output(func.__name__, time - start)
            return result
        return wrapper
    return decorate


class Record():
    """自定义装饰器类(通过__call__魔术方法使得对象可以当成函数调用)"""

    def __init__(self, output):
        self.output = output

    def __call__(self, func):

        @wraps(func)
        def wrapper(*a, **k):
            start = time()
            result = func(*a, **k)
            self.output(func.__name__, time() - start)
            return result
        return wrapper


def outer(func):  # 将index的地址传递给func
    def inner():
        start_time = time()
        func()   # fun = index  即func保存了外部index函数的地址
        end_time = time()
        print("运行时间为%s"%(end_time - start_time))
    return inner  # 返回inner的地址


def index():
    sleep(random.randrange(1, 2))
    print("welcome to index page")


# 用装饰器来实现单例模式
def singleton(clc):
    """
    非线程安全
    """
    """装饰类的装饰器"""
    instances={}

    @wraps(clc)
    def wrapper(*args,**kwargs):
        if clc not in instances:
            instances[clc] = clc(*args,**kwargs)
        return instances[clc]
    return wrapper

@singleton
class President():
    """总统（单例类）"""
    pass

def singleton2(cls):
    """线程安全的单例装饰器"""
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                   instances[cls] =cls(*args,**kwargs)
        return instances[cls]
    return wrapper



if __name__ == '__main__':
    print('------------无参数装饰器--------------')
    index = outer(index)  # 这里返回的是inner的地址，并重新赋值给index

    index()


    print("-----------装饰器测试---------")
    # d = record_time(a)
    print('5的5次方：', a(5))

    print("-----------装饰器，网上例子---------")
    say("hahahahahah1233455")
    say2("-------000000000000-------929374982347vhxjkv fdv")


    print()

    print("---------------测试装饰器的高级模式-------------")
    haha("nihao你好，我是哈哈，是使用@ 模式的")
    print('---')
    haha2("nihao你好》》》》》》》")

    print("------------单例模式----------")
    p1 = President()
    p2 = President()

    print("p1.id:",id(p1))
    print("p2.id:",id(p2))
    

