# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import module1 as m1
import module2 as m2
import module3

from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()

m1.foo()
m2.foo()

print("判断一个数是不是回文数")
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0 :
        total = total * 10 + temp % 10
        print("total:",total)
        temp //= 10
        print("temp:",temp)
    return total == num


print(is_palindrome(123321))


# 变量作用域
def foo():
    """
    global关键字来指示foo函数中的变量a来自于全局作用域，
    如果全局作用域中没有a，
    那么下面一行的代码就会定义变量a并将其置于全局作用域
    """
    global a
    a = 200
    print(a)
if __name__ == '__main__':
    a = 100
    foo()
    print(a)