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
    
    