# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 16:04
desc: 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。.
"""

import sys
import math

reload(sys)
sys.setdefaultencoding('utf8')


class Point(object):

    def __init__(self,x=0,y=0):
        """
        初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self._x = x
        self._y = y
    def move_to(self,x,y):
        """
        移动到指定的位置
        :param x: 新的横坐标
        :param y: 新的纵坐标
        """
        self._x=x
        self._y=y
    def move_by(self,dx,dy):
        """
        移动指定的增量
        :param dx: 增量横坐标
        :param dy: 增量纵坐标
        """
        self._y += dy
        self._x += dx

    def distance_to(self,other):
        """
        计算一个点与另一个点的距离
        :param other: 另一个点
        :return: 两个点之间的直线距离
        """
        dx = self._x - other._x
        dy = self._y - other._y
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self._x),str(self._y))

def main():
    p1 = Point(3, 4)
    p2 = Point()
    print(p1)
    print(p2)
    print(p1.distance_to(p2))
    p2.move_by(-3, -4)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main()


