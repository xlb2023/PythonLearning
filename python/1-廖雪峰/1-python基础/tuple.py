#!/usr/bin/env python3
#-*- conding: utf-8 -*-

# tuple也是一种python的数据类型，中文名字叫元组，和list类似，区别在于list可以进行增删改查，而元组只能进行查，具有指向不可变的特征。

#创
T = (1,)
print(T,len(T))

# 元组的“可变性”
T1 = (1,2,3,4,5,[1,2])
print(T1,len(T1))
T1[5][0]='X'
print(T1,len(T1))