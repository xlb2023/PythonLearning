#!/usr/bin/env python3
#-*- conding: utf-8 -*-

#占位符  %d 整数   %s 字符串   %f  浮点数   %x 十六进制数

a = int(input('2+3 ='))

b = input('Hello ')

c = float(input('请输入浮点数：'))

print('2+3=%d'%a)
print('Hello %s'%b)
print('我是浮点数 %.4f'%c)

# format()函数
print('Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125))

# f-string
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')

