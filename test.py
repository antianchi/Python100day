# -*- coding: utf-8 -*-
import sys
import math
reload(sys)
sys.setdefaultencoding('utf8')

a = 3
b = 1
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

"""
使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串

Version: 0.1
Author: 骆昊
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

# 使用type检查变量的类型
print("检查变量的类型")
print(type(a))
print(type(1 + 5j))
print(type(12.44))

"""
运算符的使用

Version: 0.1
Author: 骆昊
"""
print("运算符的使用")
a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)


print("华氏温度转摄氏温度")
f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print('%.1f华氏温度= %.1f摄氏温度' % (f,c))


print("计算圆的周长和面积")

radius = float(input("请输入圆的半径："))
p = 2 * math.pi * radius
s = math.pi * radius * radius
print("圆的半径：")
print(radius,"周长：",p,"面积：",s)

print("判断是否是闰年")
year = int(input("输入年份："))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
