#!/usr/bin/env python3
#-*- conding: utf-8 -*-

# list是列表，是python中的一种数据类型，是一种有序的集合，可以随时添加和删除其中的元素。
# 创
classmates = ['Michael','Bob','Tracy']
# 查
print(classmates,len(classmates))
print(classmates[0],classmates[1],classmates[2],len(classmates[0]))
print(classmates[-1],classmates[-2],classmates[-3])
classmates.append('Aadm')
print(classmates[3],classmates[-1])
#增
    #插入
classmates.insert(1,'Jack')
print(classmates,len(classmates))
#改
classmates[1] = 'Search'
print(classmates,len(classmates))
#删
classmates.pop(1)
print(classmates,len(classmates))

#一个列表可以存放不同类型的元素
A = ['Admin',123,True]
print(A,len(A))

#嵌套另一个列表
B = ['Admin',123,['Michael',13.14],True]
print(B,len(B))

#或者
C = ['Michael',13.14]

B = ['Admin',123,C,True]

print(B,len(B))
