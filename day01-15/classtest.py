# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 15:07
desc: 类的概念，类中定义函数，将对象的动态特征描述出来.
"""

import sys
from time import sleep

reload(sys)
sys.setdefaultencoding('utf8')


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def study(self,course_name):
        print("%s正在学习%s" %(self.name,course_name))


    def watch_av(self):
        """
        看AV
        :return:
        """
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情动作片.' % self.name)

# chuang创建对象
def main():
    st1 = Student('笑纳',23)
    # 给对象发消息
    st1.study("JAVAbiancheng 变成")
    st1.watch_av()


# 定义一个类描述数字时钟
class Clock(object):
    """数字时钟"""

    def __init__(self,hour=0,minute=0,second=0):
        """
        初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour+=1
                if self._hour == 24:
                    self._hour = 0
    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour,self._minute,self._second)

def my_clock():
    clock = Clock(23,59,58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()





if __name__=="__main__":
    main()
    my_clock()