
# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 16:52
desc: @property装饰器，提供getter和setter装饰器.
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

class Person(object):
    def __init__(self,name,age):
        self._name = name
        self._age = age

    # 访问器，getter方法
    @property
    def name(self):
        return self._name

    # 访问器，getter方法
    @property
    def age(self):
        return self._age

    # 访问器，修改方法
    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

