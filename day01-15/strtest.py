# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 字符串常用函数

def main():
    str1 = 'hello,world!';
    print("#len计算字符串长度")
    print(len(str1))
    print("#获取字符串首字母大写的拷贝")
    print(str1.capitalize())
    print("oo------>",str1)
    print("# 获得字符串大写后的拷贝")
    print(str1.upper())
    print("oo------>",str1)
    print("# 从字符串中查找子串的位置")
    print(str1.find("or"))
    print(str1.find("or111"))
    print("oo------>",str1)
    print("# 与find相似，但是找不到会发生异常")
    # print(str1.index("or"))
    print("oo------>",str1)

    print("# 检查字符串是否以指定的字符串开头")
    print(str1.startswith("h"))
    print(str1.startswith("H"))
    print("oo------>",str1)
    print("# 检查字符串是否以指定的字符结尾")
    print(str1.endswith("!"))
    print("# 将字符串以指定的宽度居中并在两侧填充指定的字符")
    print(str1.center(50, '*'))
    print("# 将字符串以指定的宽度靠右放置左侧填充指定的字符")
    print(str1.rjust(30,"-"))

    str2 = "abc123456"
    print("字符串下标运算")
    print(str2[2])
    print("# 字符串切片（从制定的开始索引到指定的结束索引）")
    for val in str1[:]:
        print("字符打印：")
        print(val)
    print(str2[2:5])
    print(str2[2:])
    # 设置了步长为2
    print(str2[2::2])
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45
    print("# 检查字符串是否由数字构成")
    print(str2.isdigit())
    print("# 检查字符串是否以字母构成")
    print(str2.isalpha())
    print("# 检查字符串是否以字母数字构成")
    print(str2.isalnum())

    str3 = '  jackfrued@126.com '
    print(str3)
    print("# 获得字符串修剪左右两侧空格的拷贝")
    print(str3.strip())









