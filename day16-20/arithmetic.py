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

