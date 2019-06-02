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
            z = 100 - x - y

            if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                print(x, y, z)


def a2():
    # A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
    # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
    # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
    fish = 1
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5


class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self._weight = weight
        self._price = price
        self._name = name

    @property
    def value(self):
        """价格重量比"""
        return self._price / self._weight
    @property
    def weight(self):
        return self._weight
    @property
    def price(self):
        return self._price
    @property
    def name(self):
        return self._name


def a3():
    """
    贪婪算法：在对问题求解时，总是做出在当前看来是最好的选择，
    不追求最优解，快速找到满意解。
    输入：
    20 6
    电脑 200 20
    收音机 20 4
    钟 175 10
    花瓶 50 2
    书 10 1
    油画 90 9
    """
    all_things = []
    all_things.append(Thing("电脑", 200, 20))
    all_things.append(Thing("收音机", 20, 4))
    all_things.append(Thing("钟", 175, 10))
    all_things.append(Thing("花瓶", 50, 2))
    all_things.append(Thing("书", 10, 1))
    all_things.append(Thing("油画", 90, 9))
    all_things.sort(key=lambda x:x.value,reverse=True)

    total_weight = 0
    total_price = 0
    max_weight = 20
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷拿走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price
    print(f"总价ZHI:{total_price}美元！！")

if __name__ == '__main__':
    a1()

    print('-----------分鱼----------')
    a2()

    print('-----------小偷偷东西---------')
    a3()
