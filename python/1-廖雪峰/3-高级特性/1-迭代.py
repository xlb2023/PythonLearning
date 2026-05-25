#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
from collections.abc import Iterable
#迭代（Iteration）
#在c语言中的迭代仅能有下标的对象，
#但在python中的for循环比c语言中的更抽象，不仅仅可以用在tuple和list上，还可以用在dict、set、string、以及其他一切可迭代对象
#举个例子：string
s = 'abcdefjhkgk'
for S in s:
    print(S)
print("---------------------")
#再举一个：dict
#dict默认迭代key值
d = {'a':1,'b':2,'c':3,'d':4}
for key in d:
    print(key)
#如果想迭代vaule值，可以通过dict的内置函数
#通过values函数迭代dict的values值
print("---------------------")
for vaule in d.values():
    print(vaule)
#通过items函数同时迭代key和values的值
print("---------------------")
for key,vaules in d.items():
    print(key,vaules)
#在python中使用for循环时，不关注对象的数据类型，只需要判断该对象是否为可迭代对象即可
#所以如何判断要迭代的对象是否为可迭代对象，在python中很重要
#在python中通过collections.abc模块的Iterable类型判断
#首先需要导入collections.abc模块
#from collections.abc import Iterable
print("---------------------")
print(isinstance("abc",Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance((1,2,3),Iterable))
print(isinstance(123,Iterable))
#下标循环：和java对标
#通过python中的内置函数--enumerate函数--实现
#举个例子：list通过--enumerate函数--实现索引-元素迭代
print("---------------------")
for i,vule in enumerate(['A','B','C']):
    print(i,vule)
#在python中for循环可以引用多个变量，如下
print("---------------------")
list1 = [(1,2),(1,2),(1,2)]
for x,y in list1:
    print(x,y)
#错误事例:ValueError: too many values to unpack (expected 2)
# print("---------------------")
# list1 = [(1,2,3),(1,2,4),(1,2,5)]
# for x,y in list1:
#     print(x,y)
#迭代查找一个list中最小和最大值,并返回tuple
print("---------------------")
def findMinAndMax(L):
    if L == None or L == []:
        return (None,None)
    MAX = L[0]
    MIN = L[0]
    for l in L:
        if l>MAX:
            MAX = l
        elif l< MIN:
            MIN = l
    return (MIN,MAX)
L1 = [6,4,32,842,23,75]
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')