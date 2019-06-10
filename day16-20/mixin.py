#!/usr/bin/env python
# coding=UTF-8
#! python3
'''

Author: antch
Email: atc00@foxmail.com
Date: 2019-06-10 19:44:11
LastEditors: antch
LastEditTime: 2019-06-10 19:44:11
Description: 混入.
自定义字典限制只有在指定的key不存在时才能在字典中设置键值对。
'''

class SetOnceMappingMixin():
    """自定义混入类"""
    __slots__=()

    def __setitem__(self,key,value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)

class SetOnceDict(SetOnceMappingMixin,dict):
    """自定义字典"""
    pass

if __name__=='__main__':
    my_dict = SetOnceDict()

    try:
        my_dict['username'] = 'jackfrued'
        my_dict['username'] = 'hellokitty'ss
    except KeyError as ke:
        pass
    print(my_dict)

