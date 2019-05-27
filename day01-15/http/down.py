#!/usr/bin/env python
# coding=UTF-8
#! python3
'''
@Author: antch
@Email: atc00@foxmail.com
@Date: 2019-05-27 19:36:19
@LastEditors: antch
@LastEditTime: 2019-05-27 19:48:58
@Description: 使用requests库.
'''

from time import time
from threading import Thread
import requests

class DownloadHandler(Thread):
    """创建自定义线程下载类"""
    def __init__(self,url):
        self._url = url
    
    def run(self):
        filename = self._url[self._url.rfind('/') + 1:]
        resp = requests.get(self._url)
        with open(filename,'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=d8c44ed33b1c5101381bf9be751b7afe&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHandler(url).start()

if __name__=='__main__':
    main()

