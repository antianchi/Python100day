# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 10:21
desc: 双色球选号.
"""

import sys
from random import randrange,randint,sample
reload(sys)
sys.setdefaultencoding('utf8')

def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    for index,ball in enumerate(balls):
        if index == len(balls) -1 :
            print("|")
        print('%02d' % ball)
    print()

def random_select():
    """
    随机选一组号码
    :return:选好的号码
    """
    red_balls = [x for x in range(1,34)]
    selected_balls = []
    # random模块的sample函数来实现从列表中选择不重复的n个元素。
    selected_balls = sample(red_balls,6)
    # selected_balls.sort()
    selected_balls.append(randint(1,6))
    return selected_balls
def main():
    n = int(input('随机选几注：'))
    for _ in range(n):
        display(random_select())
if __name__ == '__main__':
    main()



