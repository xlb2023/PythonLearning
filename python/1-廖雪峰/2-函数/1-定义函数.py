#!/usr/bin/env python3
# -*- encoding : utf-8 -*-


#定义函数使用def语句，并依次写出函数名、括号、括号中的参数和冒号，然后在缩进块中编写函数体，函数的返回值用return语句返回。
def my_abs(x):
#对输入的参数进行检查：
    if not isinstance(x,(int,float)):
        raise TypeError('bad openrand type')
    if x >= 0:
        return x
    else:
        return -x

# 调用函数
# from (文件名) import (函数名)

#空函数
#pass 语句是占位符，什么都不做。

def nop():
    pass
#返回多个值
import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx,ny
#可以同时获取返回值
x,y = move(200,100,70,math.pi/6)
print(x,y)
#其实函数中有多个返回值时，是通过一个元组（tuple）返回return结果。
r = move(200,100,70,math.pi/6)
print(r)
# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。

#练习
def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad openrand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad openrand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad openrand type')
    if b**2-4*a*c >0:
        x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
        x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
        return x1,x2
    elif b**2-4*a*c == 0:
        x1 = -(b/2*a)
        return x1
    else :
        return "无解"
print(quadratic(1,2,3))
print(quadratic(4,4,1))
