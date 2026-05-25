#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

#dict:字典
# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


#创
d = {"Michael": 95,"Bob": 75,'Tracy': 85}
print(d['Michael'])
print(d['Bob'])
#改
d['Bob'] = 67
print(d["Bob"])
#增
d['jack']=90
print(d["jack"])
print(d)
#判断是否存在
# for 'Thomas' in d:
    # print(" ")
print(d.get('Thomas'))
print(d.get('Thomas',-1))
print(d)
#删
d.pop("Bob")
print(d)
#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
t = (1,2,3)
d[t] = "tuple"
print(d)
#set：set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 创
# set的特性：过滤重复元素
s = set([1,2,3,3])
print(s)
s = set([1,1,2,2,3,3])
print(s)
#增
s.add(4)
print(s)
#删
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

s1 = set([1,2,3,4])
s2 = set([2,3,4,5])
#交集
print(s1 & s2)
#并集
print(s1 | s2)

#不可变对象
#首先要明确对象和变量的区别：
    #对象是什么：是数据、是变量赋值后所指向的数据。
    #变量是什么：
#而所谓的不可变对象指的是变量指向的对象中的内容不可变。
#所有就有了以下的例子：
#不可变对象：字符串、元组
a = 'abc'
print(a.replace('a','A'))
print(a)
b = a.replace('a','A')
print(b)

#通过以上例子再次证明字符串未不可变对象，其中b变量所指向的对象的值之所以是Abc是因为a变量所指向的对象的值在执行replace这个函数后复制abc，然后将a修改为A，存储在新的位置。

#不可变对象分为：1:内容不可变、2:指向不可变、3：1 and 2 dict对key的要求属于第3种，所以只有当数据类型必须满足内容和指向都不可变的时候才能做key
d = {(1,2,3)}
# d = {(1,2,[1,2]):1}

s = set((1,2,[1,2]))
print(s)
# print(d)
