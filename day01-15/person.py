# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 16:52
desc: @property装饰器，提供getter和setter装饰器.
"""

import sys
from math import sqrt
from time import time, localtime, sleep

reload(sys)
sys.setdefaultencoding('utf8')


class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 限定自定义类型的对象只能绑定某些属性
    # __slots__的限定只对当前类的对象生效，对子类并不起任何作用。
    __slots__ = ('_name', '_age', '_gender')

    # 访问器，getter方法
    @property
    def name(self):
        return self._name

    # 访问器，getter方法
    @property
    def age(self):
        return self._age

    # 访问器，修改方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


# xuesh学生
class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        # p3.0以上的写法
        # super().__init__(name,age)

        # python2.7的写法
        super(Student, self).__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super(Teacher, self).__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._b + self._a + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))


def main():
    person = Person('小安', 7)
    person.play()
    person.age = 333
    # person.name='张'
    person.play()
    # person._gen = 123
    # print(person._gen)

    print("----------------")
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print('周长 %s' % (t.perimeter()))
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        print(t.area())
        print(Triangle.area(t))
    else:
        print('无法构成三角形.')

    print("-------------clock-------------")

    # 通过类方法创建并获取系统时间
    # clock = Clock.now()
    # while True:
    #     print(clock.show())
    #     sleep(1)
    #     clock.run()

    print('----------展示类之间的关系--------------')
    stu = Student('校长', 23, 'nv')

    stu.study("英语")

    t = Teacher('张三', 33, '数学')
    t.teach("JAVA 编程思想")


# 类相关的对象

class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    main()
