#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

# 格式化
# 1.% %

#a = int(input("3+2="))
#print("3+2=%d"%a)

# 2.format函数
#a = int(input("3+2="))
#print("3+2={0}".format(a))

# 3.f-string
#a = int(input("3+2="))
#print(f"3+2={a}")

#list
#创
a = [1,2,3,4]
print(a)
#增
a.insert(1,1)
print(a)
#删
a.pop(-1)
#改
a.append(2)
print(a)
a[0] = 3
print(a)
#嵌套
a = [1,2,3,[2,3,4,'jun'],4]
print(a[3])
print(a[3][0])
print(a,len(a))
#tuple
a = (1,2,3,4)
print(a)
# "不可修改"
#a[0] = 1
print(a[0])
# "不可修改性指的是元组中的元素是不可修改时，该元组不可修改"
a = (1,2,3,[1,2,4,3],4)
print(a)
a[3].append(3)
a[3][0] = 'list'
print(a)
# 当元组中只存在一个元素时，必须带逗号
a = (1)
print(a)
a = (1,)
print(a)

a=input()
a=float(a)
if a >32:
    print("过于肥胖")
elif a>=25 and a<=32:
    print("比较肥胖")
elif a>18.5 and a<25:
    print("正常")
else:
    print("过轻")