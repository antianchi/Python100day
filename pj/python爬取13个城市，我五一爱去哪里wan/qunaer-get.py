#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-06-04 09:44:53
LastEditors: antch
LastEditTime: 2019-06-04 09:44:53
Description: 爬取去哪儿数据.

'''

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


class QuNaEr():
    def __init__(self,keyword,page=1):
        self.keyword = keyword
        self.page = page
    def qne_spider(self):
        url = 'https://piao.qunar.com/ticket/list.htm?keyword=%s&region=&from=mpl_search_suggest&page=%s' % (self.keyword,self.page)
        response = requests.get(url)
        response.encoding= 'utf-8'
        text = response.text
        bs_obj = BeautifulSoup(text,'html.parser')
        arr = bs_obj.find('div',{'class':'result_list'}).contents
        for i in arr:
            info = i.attrs
            # 景区名称
            name  = info.get('data-sight-name')
            # 地址
            address = info.get('data-address')
            # 近期售票数             
            count = info.get('data-sale-count')             
            # 经纬度             
            point = info.get('data-point')    
            # 起始价格            
            price = i.find('span', {'class': 'sight_item_price'})             
            price = price.find_all('em')             
            price = price[0].text

            conn = MongoClient('127.0.0.1',port=27017)
            db = conn.QuNaEr
            table = db.qunaer_51

            table.insert_one({
                "name":name,
                "address":address,
                "count":int(count),
                "point":point,
                "price":float(price),
                "city":self.keyword
            })
if __name__=='__main__':
    citys = ['北京', '上海', '成都', '三亚', '广州', '重庆', '深圳', '西安', '杭州', '厦门', '武汉', '大连', '苏州'] 
    for i in citys:
        for page in range(1,5):
            qne = QuNaEr(i,page)
            qne.qne_spider()



