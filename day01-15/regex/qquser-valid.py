#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: atch
@Email: atc00@foxmail.com
@Date: 2019-05-27 10:06:03
@LastEditors: antch
@LastEditTime: 2019-05-27 11:05:24
@Description: 验证输入用户名和QQ号是否有效并给出对应的提示信息。
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，
QQ号是5~12的数字且首位不能为0.
'''

import re

def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'\w{6,20}',username)
    m2 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1 :
        print('请输入有效的用户名m1')
    if not m2 :
        print("请输入有效的用户名m2")
    m3 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m3:
        print("请输入有效的ＱＱ号码")

def main2():
    """
    从一段文字中提取出国内手机号码。
    """
    # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    # 更好的匹配国内的手机号正则表达式
    pattern2 = re.compile(r'<?<=\D>(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8}|199\d{8})(?=\D)')

    
    sentence='''
    重要的事情说8130123456789遍，我的手机号是113512346789这个靓号，
    不是15600998765，也不是110或119，王大锤的手机号才是15600998765。
    '''
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern,sentence)
    print('提取到的号码：',mylist)
    print('---------华丽的分割线-----------')
    # 通过迭代器取出匹配对象并获得匹配的内容
    for tem in pattern.finditer(sentence):
        print(tem.group())
    print('---------华丽的分割线-----------')
    # 通过search函数指定搜索位置找出所有的匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())


def main3():
    """替换字符串中的不良内容"""
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*', sentence, flags=re.IGNORECASE)
    print(purified)
    
def main4():
    """拆分字符串"""
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']

if __name__=='__main__':
    # main()
    print("==================|||2|=================")
    main2()
    print("==================|||3|=================")
    main3()
    print("==================|||4|=================")
    main4()



