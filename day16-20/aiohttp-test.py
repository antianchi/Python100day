#!/usr/bin/env python
# coding=UTF-8
#! python3
'''

Author: antch
Email: atc00@foxmail.com
Date: 2019-06-10 21:19:26
LastEditors: antch
LastEditTime: 2019-06-10 21:19:26
Description: .
Python中有一个名为aiohttp的三方库，它提供了异步的HTTP客户端和服务器，
这个三方库可以跟asyncio模块一起工作，并提供了对Future对象的支持。
Python 3.6中引入了async和await来定义异步执行的函数以及创建异步
上下文，在Python 3.7中它们正式成为了关键字。
下面的代码异步的从5个URL中获取页面并通过正则表达式
的命名捕获组提取了网站的标题。
'''

import asyncio
import re
import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')
# print(r'\<title\>(?P<title>.*)\<\/title\>')

async def fetch_page(session,url):
    async with session.get(url,ssl=False) as resp:
        return await resp.text()

async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))

if __name__=='__main__':
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/',
            'http://www.jikedaohang.com/server/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()