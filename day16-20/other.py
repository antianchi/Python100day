#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-31 13:26:57
LastEditors: antch
LastEditTime: 2019-05-31 13:26:57
Description: 其他语法.

'''

def main():
    """使用生成式（推导式）语法"""
    prices = {
          'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
    }
    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key:value for key ,value in prices.items() if value > 100}
    print(prices)
    print(prices2)
    print('生成式（推导式）可以用来生成列表、集合和字典。')

    print('嵌套的列表-------------')
    names = ['关羽','张飞','赵云','马超','黄忠']
    courses = ['语文','数学','英语']
    # 录入五个学生三门课程的成绩
    # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # scores = [[None] * len(courses)] * len(names)
    scores = [[None]*len(courses) for _ in range(len(names))]
    for row ,name in enumerate(names):
        for col ,course in enumerate(courses):
            scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
            print(scores)


if __name__=='__main__':
    main()




