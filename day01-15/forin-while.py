# -*- coding: utf-8 -*-
# 不换行，此导入必须放在首行
from __future__ import print_function

import random
import sys

# xun找水仙花数
for i in range(100,1000):
    b = i / 100
    sg = i % 100
    s = sg / 10
    g = sg % 10
    if( i == (b * b * b + s * s * s + g * g * g) ):
        print("水仙花数：")
        print(i)

reload(sys)
sys.setdefaultencoding('utf8')

# 输出九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j))
    print()
for i in range(1,10):
    for k in range(1,i+1):
        print('%d * %d = %d' % (i,k,i*k),end='\t')
    print()


"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
"""

sum = 0
for x in range(101):
    sum += x
print(sum)


print("1-100之间的偶数求和")
sum = 0
for v in range(2,101,2):
    sum += v
print(sum)

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
