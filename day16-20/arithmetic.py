#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-28 11:00:59
LastEditors: antch
LastEditTime: 2019-05-28 11:00:59
Description: python进阶，算法.

'''

def select_sort(origin_items,comp=lambda x,y: x<y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) -1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
            items[i],items[min_index] = items[min_index],items[i]
    return items

def main():
    a = [1,3,2,6,4]
    sa = select_sort(a)
    print('原始数组：',a)
    print('已经排序的数组：',sa)

if __name__=='__main__':
    main()

