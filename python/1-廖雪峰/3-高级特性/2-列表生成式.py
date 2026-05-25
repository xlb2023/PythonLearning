#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import os
#列表生成式：List Comprehensions,是Python内置的非常简单却强大的可以用来创建list的生成式.
#举个例子：生成list[1,2,3,4,5,6,7,8,9,10]可以用list(range(1,11))
L1 = list(range(1,11))
print(L1)
#使用for循环生成[1x1, 2x2, 3x3, ..., 10x10]列表
L  =[]
for x in range(1,11):
    L.append(x*x)
print(L)
#使用列表生成式
L = [x*x for x in range(1,11)]
#使用判断语句进行筛选
print(L)
L = [x*x for x in range(1,11) if x*x % 2 ==0]
print(L)
#使用双循环进行全排列
L = [m+n for m in 'ABC' for n in 'XYZ']
print(L)
#os.listdir可以列出当前位置的文件和目录
L = [d for d in os.listdir('.')]
print(L)
#列表生成式也可以使用两个变量来生成list：
d = {'a':'1','b':'2','c':'3'}
L = [k+"="+v for k,v in d.items()]
print(L)
#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
L = [s.lower() for s in L]
print(L)
#if else
#当if放在for后面时，作为条件筛选，不可加else
#错误举例：SyntaxError: invalid syntax
#[x for x in range(1,11) if x % 2 == 0 else 0]
#正确
L  = [x for x in range(1,11) if x % 2 == 0]
print(L)
#当if放在for前面时，作为表达式，必须加else
#错误举例：expected 'else' after 'if' expression
# L = [x if x % 2 == 0 for x in range(1,11)]
#正确
L = [x if x % 2 == 0 else -x for x in range(1,11)]
print(L)
#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x,str)]
L2 = [x.lower() for x in L2]
#或者
L2 = [x.lower() for x in L1 if isinstance(x,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

