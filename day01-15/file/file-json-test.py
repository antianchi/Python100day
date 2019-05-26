#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: antch
@Email: atc00@foxmail.com
@Date: 2019-05-26 21:57:19
@LastEditors: antch
@LastEditTime: 2019-05-26 22:00:58
@Description: JSON文件操作.
'''

import json

def main():

    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('data.json','w',encoding='utf-8') as f:
            json.dump(mydict,f)
    except IOError as ex:
        print(ex)
        print("写JSON文件出错")
    print("保存数据完成")

if __name__=='__main__':
    main()