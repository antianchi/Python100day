# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/25 22:59
desc: 工资结算.

某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

import sys
from abc import ABCMeta,abstractmethod

reload(sys)
sys.setdefaultencoding('utf8')

class Employee(object):
    """员工"""
    def __init__(self,name):
        self._name = name
    

    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        """
        获得月薪
        """
        pass

class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """程序员"""

    def __init__(self,name,working_hour = 0):
        super(Programmer,self).__init__(name)
        self._working_hour = working_hour
    
    @property
    def working_hour(self):
        return self._working_hour
    
    @working_hour.setter
    def working_hour(self,working_hour):
        self._working_hour = working_hour
    
    def get_salary(self):
        return 150.0 * self._working_hour

class SaleMan(Employee):
    """销售员"""

    def __init__(self, name,sales = 0):
        super(SaleMan,self).__init__(name)
        self._sales = sales
    
    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self,sales):
        self._sales = sales if sales > 0 else 0
    
    def get_salary(self):
        return 1200 + self.sales * 0.05
    

def main():

    ems = [
        Manager(' 刘备'),
        Programmer(' 张飞'),
        Manager(' 曹操'),
        SaleMan(' 荀彧'),
        SaleMan(' 吕布'),
         Programmer(' 张辽'),
        Programmer(' 赵云')
    ]

    for e in ems:
        if isinstance(e,Programmer):
            e.working_hour = int(input('请输入%s本月工作时间: ' % e.name))
        elif isinstance(e,SaleMan):
            e.sales = int(input('请输入%s本月的销售额：' % e.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (e.name, e.get_salary()))


if __name__ == '__main__':
    main()
    


    
    