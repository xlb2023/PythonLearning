#!/usr/bin/env python3
# # -*- encoding : utf-8 -*-
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#用递归函数编写n！
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
#函数运行模式
#===> fact(5)
#===> 5 * fact(4)
#===> 5 * (4 * fact(3))
#===> 5 * (4 * (3 * fact(2)))
#===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
print(fact(100))
#在调用递归函数是，要注意防止栈溢出；由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
#print(fact(1000))
#解决递归函数的栈溢出问题，要通过**尾递归**或者是**循环**解决栈溢出问题
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
#尾递归
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1,num * product)
# print(fact(1001))
#循环
def fact(n):
    sum = 1
    while n > 0:

        sum = sum * n

        n = n - 1
    return sum 
print(fact(1000))
#汉诺塔
def move(n,a,b,c):
    if n ==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
move(4,'A','B','C')
