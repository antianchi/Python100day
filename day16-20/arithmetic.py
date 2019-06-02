#!/usr/bin/env python
# coding=UTF-8
#! python3
''''

Author: atch
Email: atc00@foxmail.com
Date: 2019-05-28 11:00:59
LastEditors: antch
LastEditTime: 2019-05-28 11:00:59
Description: python进阶，算法.

'''

def select_sort(origin_items,comp=lambda x,y: x<y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) -1):
        min_index = i
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
            items[i],items[min_index] = items[min_index],items[i]
    return items

def bubble_sort(origin_items,comp=lambda x,y: x>y):
    """高质量冒泡排序（搅拌排序）"""
    items = origin_items[:]
    for i in range(len(items) -1):
        swapped = False
        for j in range(i,len(items) - 1 - i):
            if comp(items[j],items[j+1]):
                items[j],items[j+1] = items[j+1],items[j]
                swapped = True
        if swapped :
            swapped = False
            for j in range(len(items) - 2 -i,i,-1):
                if comp(items[j-1],items[j]):
                    items[j],items[j-1] = items[j-1],items[j]
                    swapped = True
        if not swapped:
            break
    return items

def merge_sort(items,comp=lambda x,y: x<=y):
    """归并排序（分治法）"""
    if len(items) < 2:
        return items[:]
    # //取整除 - 返回商的整数部分（向下取整）
    mid = len(items)//2
    left = merge_sort(items[:mid],comp)
    right = merge_sort(items[mid:],comp)
    return merge(left,right,comp)

def merge(items1,iterms2,comp):
    """合并（将两个有序的列表合并成一个有序的列表）"""
    items = []
    index1,index2 = 0,0
    while index1 < len(items1) and index2 < len(iterms2):
        if comp(items1[index1],iterms2[index2]):
            items.append(items1[index1])
            index1+=1
        else:
            items.append(iterms2[index2])
            index2+=1
    items += items1[index1:]
    items += iterms2[index2:]
    return items 

def seq_search(items,key):
    """顺序查找"""
    for index,item in enumerate(items):
        if item == key :
            return index
    return -1

def bin_search(items,key):
    """折半查找"""
    start,end = 0,len(items) -1
    while start < end :
        mid = (start + end)//2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid -1
        else:
            return mid
    return -1

def quick_sort(origin_items,comp=lambda x,y: x<=y):
    """
    快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
    """
    items = origin_items[:]
    _quick_sort(items,0,len(items)-1,comp)
    return items 

def _quick_sort(items,start,end,comp):
    if start<end:
        pos = _partition(items,start,end,comp)
        _quick_sort(items,start,pos-1,comp)
        _quick_sort(items,pos+1,end,comp)

def _partition(items,start,end,comp):
    pivot = items[end]
    i = start - 1
    for j in range(start,end):
        if comp(items[j],pivot):
            i+=1
            items[i],items[j] = items[j],items[i]
    items[i+1],items[end] = items[end],items[i+1]
    return i+1





def main():
    a = [1,3,2,6,4]
    sa = select_sort(a)
    print('原始数组：',a)
    print("-------选择排序-------")
    print(sa)
    print("-------冒泡排序-------")
    sa1 = bubble_sort(a)
    print(sa1)
    print("-------归并排序算法-------")
    sa2 = merge_sort(a)
    print(sa2)
    print("-------快速排序算法-------")
    sa3 = quick_sort(a)
    print(sa3)


    

if __name__=='__main__':
    main()

