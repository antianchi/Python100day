# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import random

def listtest():
    list1 = [1,3,5,7,100]
    print("List:",list1)
    list2 = ['hello'] * 5
    print("list2:",list2)
    # 计算列表的长度
    print(len(list1))
    # 下标索引计算
    print(list1[0])

    # print(list1[5])
    list1[2] = 400
    print("list1:",list1)
    # 添加元素
    list1.append(1234)
    list1.insert(1,333)
    list1 += [5000,6000]
    print("list1:",list1)
    print("len(list1):",len(list1))

    # 删除元素
    list1.remove(3)
    del list1[0]
    print("delete yuansu hou list1:",list1)

    # 清空元素列表,报错没有这样的方法。
    # list1.clear
    print(list1)

    print("-----列表切片-------")
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title())
    print()
    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruit3 = fruits  # 没有复制列表只创建了新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)

    print("修改复制切片，查看值的信息")
    fruits3[0] = "a"
    print(fruits3)
    print(fruits)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

    print("----------列表排序--------")
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


    print("------------列表生成式语法-----------------------")
    f =[x for x in range(1,10)]
    print("f:",f)
    f = [x + y for x in 'abcde' for y in '12345']
    print(f)

    # 用列表的生成表达式语法创建容器
    # 用这种语法创建列表之后元素已经准备就绪，所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1,10)]
    # 查看对象占用的内存字节数
    print(sys.getsizeof(f))
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1,10))
    print(sys.getsizeof(f))
    print(f)
    for val in f :
        print(val)
def fib(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a
def yuanzu():
    print("------------元组----------------")
    # 定义元祖
    t = ('hello',29,True,'shanghai')
    print(t)
    # 获取元组中的元素
    print(t[0])
    print(t[3])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'  # TypeError
    # 变量t重新引用了新的元组原来的元组将被垃圾回收
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    # 将元组转换成列表
    person = list(t)
    print(person)
    # 列表是可以修改它的元素的
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)

# 集合运算，集合与数学上的语义一致
def settest():
    print("jihe集合运算-----------------")
    set1 = {1,2,3,3,3,2}
    print(set1)
    print('len(set1)=',len(set1))
    set2 = set(range(1,10))
    print("set2:",set2)
    set1.add(4)
    set1.add(5)
    set2.update([11,12])
    print(set1)
    print(set2)
    set2.discard(15)
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print("after deleted num of set2 :",set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2)
    print("集合便利完毕")
    # 元组转换成集合
    set3 = set((1,2,3,4,4,3,2,1))
    print('set3:',set3)
    print(set3.pop())
    print('set3:', set3)
    print("集合的交集，并集，差集，对称差集运算")
    print(set1 & set2)
    print(set1 | set2)
    # print(set1.union(set2))
    print(set1 - set2)
    # print(set1.difference(set2))
    print(set1 ^ set2)
    # print(set1.symmetric_difference(set2))
    # 判断子集和超集
    print(set2 <= set1)
    # print(set2.issubset(set1))
    print(set3 <= set1)
    # print(set3.issubset(set1))
    print(set1 >= set2)
    # print(set1.issuperset(set2))
    print(set1 >= set3)
    # print(set1.issuperset(set3))
# 字典测试
def dictest():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    # invalid syntax
    # scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    # 清空字典
    scores.clear()
    print(scores)
# 在屏幕上显示跑马灯文字
def paoma():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        # os.system('cls')
        # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]
def generate_code(n = 4):
    """
    设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
    :param n: 验证码的长度
    :return: 验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(n):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def  get_suffix(filename, has_dot=False):
    """
    获取我呢见名的后缀
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


# 计算指定的年月日是这一年的第几天
def is_leap_year(y):
    """
    判断一年是不是闰年
    :param y: 年份
    :return: 是否是闰年
    """
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0
def which_day(y,m,d):
    """
    输入年月日，判断是这一年的那一天
    :param y: 年
    :param m: 月
    :param d: 日
    :return: 一年当中的第几天
    """
    if m < 2 :
        return d
    elif m < 3:
        return 31 + d
    else:
        days_of_month = [
            [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(y)]
        total = 0
        for i in range(m - 1):
            total += days_of_month[i]
        return total + d


if __name__ == '__main__':
    listtest()

    print("------自定义生成器---------")
    for v in fib(7):
        print(v)
    yuanzu()

    print("jieh集合运算-----------》")
    settest()

    print("字典操作----------------")
    dictest()

    print("跑马----------------")
    # paoma()

    print("验证码生成器------------------------")
    print(generate_code())

    print("获取我呢见名的后缀--------------------")
    print(get_suffix("xxx.ddd"))

    print("ji计算指定日期是这一年的第几天----------------------")
    print(which_day(1980, 11, 28))
    print(which_day(1981, 12, 31))
    print(which_day(2018, 1, 1))
    print(which_day(2016, 3, 1))
    print(which_day(2016, 2, 1))


