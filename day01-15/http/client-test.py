#!/usr/bin/env python
# coding=UTF-8
#! python3
'''

Author: antch
Email: atc00@foxmail.com
Date: 2019-05-27 20:16:22
LastEditors: antch
LastEditTime: 2019-05-27 20:16:22
Description: socket客户端.

'''

from socket import socket

def main():
    # 1\创建套接字对象，默认使用IPV4和TCP协议
    client = socket()
    client.connect(('127.0.0.1',6666))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__=='__main__':
    main()