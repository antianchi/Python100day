#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-06-03 09:10:28
LastEditors: antch
LastEditTime: 2019-06-03 09:10:28
Description: 费波拉契数列.

'''


def fib(num, tmp={}):
    """
    动态规划1: - 适用于有重叠子问题和最优子结构性质的问题
    使用动态规划方法所耗时间往往远少于朴素解法(用空间换取时间)
    用递归计算Fibonacci数
    """
    if num in (1, 2):
        return 1
    try:
        return tmp[num]
    except KeyError:
        tmp[num] = fib(num-1)+fib(num-2)
        return tmp[num]

def a():
    """
    动态规划2：—— 子列表元素之和的最大值。（使用动态规划可以避免二重循环）
    说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，
    可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：

    输入：1 -2 3 5 -3 2

    输出：8

    输入：0 -2 3 5 -1 2

    输出：9

    输入：-9 -2 -3 -5 -3

    输出：-2

    """
    items = list(map(int,input().split()))
    size = len(items)
    overall,partial = {},{}
    overall[size-1] = partial[size-1]=items[size-1]
    for i in range(size-2,-1,-1):
        print("i=",i,"partial[",i+1,']=',partial[i+1],'],items[',i,']=',items[i])
        partial[i] = max(items[i],partial[i+1]+items[i])
        overall[i] = max(partial[i],overall[i+1])
    print(overall[0])


def main():
    print(fib(4))

if __name__=="__main__":
    print('------费波拉契数列--------')
    num = 3
    print(f'f({num})=',fib(num))
    print('=------动态规划2：')
    a()
