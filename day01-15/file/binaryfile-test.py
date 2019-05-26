#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: antch
@Email: atc00@foxmail.com
@Date: 2019-05-26 21:47:33
@LastEditors: antch
@LastEditTime: 2019-05-26 21:53:39
@Description: 读写二进制文件.
'''

def main():
    try:
        with open('1.png','rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('2.png','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as ex:
        print(ex)
        print('指定的文件无法打开')
    except IOError as ex:
        print(ex)
        print('读取文件时出错')
    print('操作完毕！！')

if __name__=='__main__':
    main()
