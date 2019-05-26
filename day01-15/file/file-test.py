#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: antch
@Email: atc00@foxmail.com
@Date: 2019-05-26 19:39:20
@LastEditors: antch
@LastEditTime: 2019-05-26 21:35:05
@Description: .
'''


def main():
    
    # 方式一，使用finally块来释放资源
    f = None
    try:
        f = open('致橡树.txt','r',encoding="utf-8")
        
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f :
            f.close()
    
    # 方式二：使用try-with来释放资源
    try:
        with open("致橡树.txt",'r',encoding='UTF-8') as f:
            print(f.read)
    except FileNotFoundError:
        print('2无法打开指定的文件')
    except LookupError:
        print('2指定了未知的编码')
    except UnicodeDecodeError:
        print('2读取文件时解码错误')

if __name__=='__main__':
    main()
