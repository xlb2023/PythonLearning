#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

#通过列表生成式，我们可以直接创建一个列表，受到内存限制，列表容量是有限的，生成器通过一边循环一边计算的机制的解决这个问题
#列表生成式[]
L = [x*x for x in range(10)]
for n in L:
    print(n)
#生成器()
L1 = (x*x for x in range(10))
print(L1)
#可以使用next函数迭代生成器
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
# next(L1)
#当超出生成器范围时，抛出StopIteration异常
#next(L1)
#未避免抛出StopIteration异常，可以使用for循环
# for g in L1:
#     print(g)
#当遇到推算算法比较复杂，无法用简单的for in表达式实现时，我们还可以通过函数来实现：
#例如：斐波那契数列
def fib(max): # type: ignore
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a , b = b , a + b
        n += 1
    return 'done'
fib(10)
#将上面的函数中print换成yield后，该函数就可以从普通函数转变为generator函数
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'
b = fib(6)
print(b)
#生成器是一个返回迭代器的函数，和普通函数的顺序执行不同，它包含了yield语句，每次调用next(g)就会执行到下一个yield语句，返回yield语句
#后面的值，并保持状态，直到遇到yield语句，再次调用next(g)时，从上次yield语句的位置开始执行，直到遇到下一个yield语句，
#返回yield语句后面的值，并保持状态，直到遇到StopIteration异常，最后抛出StopIteration异常，终止执行
#每次调用generator函数都会生成一个新的、独立的generator对象，具体如下：(输出结果均为1)
print(next(fib(6)))
print(next(fib(6)))
print(next(fib(6)))
#正确写法是调用agenertor函数生成一个generator对象，然后再使用next函数对generartor对象进行迭代，具体如下：
ex = fib(10)
print(next(ex))
print(next(ex))
print(next(ex))
#杨辉三角
