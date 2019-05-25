# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/25 12:43
desc:多态 .
"""

import sys
from abc import ABCMeta, abstractmethod

reload(sys)
sys.setdefaultencoding('utf8')


class Pet(object):
    # python 2.7的写法
    __metaclass__ = ABCMeta

    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('汪汪汪----%s' % (self._nickname))


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('喵喵喵----%s' % (self._nickname))


def main():
    pets = [Dog("阿黄"), Cat("笑话秒")]
    for p in pets:
        p.make_voice()


if __name__ == "__main__":
    main()
