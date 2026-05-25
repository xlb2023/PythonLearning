#!/usr/bin/env python3
# -*- encoding : utf-8 -*-
import math
def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad openrand type')
    if not isinstance(b,(int,float)):
        raise TypeError('bad openrand type')
    if not isinstance(c,(int,float)):
        raise TypeError('bad openrand type')
    if b**2-4*a*c >0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
    elif b**2-4*a*c == 0:
        x1 = -(b/2*a)
        return x1
    else:
        return '无解'
print(quadratic(2,3,1))


def test(*args):
    print(args)
L = [1,2,3,4]
test(*L)


def mul(x, *y):
    for z in y:
        x = x * z
    return x

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc())

def tail_f3(n, acc):
    if n <= 1:
        return acc
    return tail_f3(n-1, n * acc)   # 注意：整个条件表达式就是递归调用或 acc


print(tail_f3(5, 1))


def move(n, a, b, c):
# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        print(a, '-->', c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
def trim(s):
    #使用切片去除字符串里不必要的空格
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('str测试成功!')


def findMinAndMax(L):
    if L == []:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)
# 测试
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
d = {'key1':1,'key2':2,'key3':3}
print(d.items())

print([x * x for x in range(1, 11)])

import os
print([d for d in os.listdir('.')])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str) == True]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(0,len(L)-1)] + [1]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    if n == 10:
        break
    results.append(t)
    n = n + 1

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))
r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(reduce(fn, map(char2num, '13579')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('23123134124124'))

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int('23123134124124'))

def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, '   t ese   ')))
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):
    #请利用filter()筛选出回数：
    return str(n) == str(n)[::-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    s = s.split('.')
    return reduce(fn, map(char2num, s[0])) + reduce(fn, map(char2num, s[1])) / (10 ** len(s[1]))
print(str2float('123.456'))

def str2float(s):
    def fn(x,y):
         return x * 10 + y
    def str2int(s):
         return DIGITS[s]
    s = s.split('.')
    return reduce(fn,map(str2int,s[0]))+reduce(fn,map(str2int,s[1]))/10**len(s[1])
 
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
     print('测试成功!')
else:
     print('测试失败!')


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
     print('测试成功!')
else:
     print('测试失败!')
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name,reverse=True)
print(L2)

# 函数作为返回值
def make_adder(n):
    return lambda x: x + n

add_5 = make_adder(5)
print(add_5(10))


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*arg,**kw):
        start = time.time()
        r = fn(*arg,**kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return r
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


import time, functools

def metric(arg = None):
    if callable(arg):
        @functools.wraps(arg)
        def wrapper(*arg1,**kw):
            print('%s execute %s' % (arg.__name__, 'begin call'))
            r = arg(*arg1,**kw)
            print('%s execute %s' % (arg.__name__, 'end call'))
            return r
        return wrapper
    else:
        def decorator(fn):
            text = arg if arg is not None else 'execute'
            @functools.wraps(fn)
            def wrapper(*arg1,**kw):
                print('%s %s %s' % (fn.__name__, text, 'begin call'))
                r = fn(*arg1,**kw)
                print('%s %s %s' % (fn.__name__, text, 'end call'))
                return r
            return wrapper
        return decorator

@metric
def f(x,y):
    return x + y
f1 = f(1,2)
print(f1)
@metric('execute')
def f(x,y):
    return x * y
import functools

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def check_divisible(x, n):   # 注意参数顺序：先 n（要绑定的），后 x（filter 传入的）
    return x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        # 使用 partial 固定 check_divisible 的第一个参数 n
        it = filter(functools.partial(check_divisible, n = n), it)

# 打印 1000 以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
