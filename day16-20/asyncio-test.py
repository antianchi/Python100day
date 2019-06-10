#!/usr/bin/env python
# coding=UTF-8
#! python3
'''

Author: antch
Email: atc00@foxmail.com
Date: 2019-06-10 20:57:47
LastEditors: antch
LastEditTime: 2019-06-10 20:57:47
Description: 异步处理.
异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的
形式执行这些任务，我们并不能保证任务将以某种顺序去执行，
因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给
另一项任务。异步任务通常通过多任务协作处理的方式来实现，
由于执行时间和顺序的不确定，因此需要通过回调式编程或者future
对象来获取任务执行的结果。Python 3通过asyncio模块和await和
async关键字（在Python 3.7中正式被列为关键字）来支持异步处理。
'''

import asyncio

def num_generate(m,n):
    """指定范围的数字生成器"""
    yield from range(m,n+1)

async def prime_filter(m,n):
    """素数过滤器"""
    primes = []
    for i in num_generate(m,n):
        flag = True
        for j in range(2,int(i**0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        if flag:
            print("Prime => " , i)
            primes.append(i)
        
        await asyncio.sleep(0.001)
    return tuple(primes)

async def square_mapper(m,n):
    """平方映射器"""
    squares = []
    for i in num_generate(m,n):
        print("Square => " ,i*i)
        squares.append(i*i)
        await asyncio.sleep(0.001)
    return squares

def main():

    loop = asyncio.get_event_loop()
    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
    future.add_done_callback(lambda x: print(x.result()))
    loop.run_until_complete(future)
    loop.close()

if __name__ == '__main__':
    main()