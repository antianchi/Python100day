#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-31 14:40:34
LastEditors: antch
LastEditTime: 2019-05-31 14:40:34
Description: collections模块工具类.

'''
import os
from collections import Counter

words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

def main():
    """
    找出序列中出现次数最多的元素
    """
    counter = Counter(words)
    print(counter.most_common(3))

if __name__=='__main__':

    main()


