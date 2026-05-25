#!/usr/bin/env python3
# # -*- encoding : utf-8 -*-
# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解。

# Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
#函数参数包括：位置参数、默认参数、可变参数、关键字参数、命名关键字参数
#1、位置参数
#举例说明：
    #计算x平方的函数
def power(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad openrand type')
    return x * x
print(power(500))
#其中的x就是power(x)函数的位置参数
    #计算x的n次方的函数：
def power(x,n):
    sum = 1
    if not isinstance(x,(int,float)):
        raise TypeError('bad openrand type')
    while n>0:
        if n>=1:
            n = n-1
            sum = sum * x
        else:
            sum = sum * (x**n)
            n = 0
    return sum
print(power(6,1.5))
#2、默认参数
# 默认参数可以大大降低函数的用的复杂度
# 规则：1、必选参数必须在前，默认参数在后；2、默认参数必须是不可变对象
def power(x,n=2):
    sum = 1
    if not isinstance(x,(int,float)):
         raise TypeError('bad openrand type')
    while n > 0:
        if n >= 1:
            n = n-1
            sum = sum * x
        else :
            sum = sum * (x**n)
            n = 0
    return sum
print(power(55))
# python的参数在函数运行结束后不会收回空间？？？
# 默认参数必须是不可变对象
#若默认参数不是不可变对象
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
#会出现[1, 'END']、[1, 'END', 'END']、[1, 'END', 'END', 'END']
#正确方法
def add_end(L=None):
    if L == None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
#可变参数：允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个**tuple**
#所谓可变参数指的是可传入参数的数量可以变化，即可以是0个、1个、2个、任意个
#例如:给定一组数字a,b,c,d.....计算a**2+b**2+c**2+d**2....
#利用数列和元组简化函数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n**2
    return sum
print(calc([1,2,3]))
print(calc((1,3,5,7)))
#利用可变参数简化函数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n ** 2
    return sum 
#可以传list或者tuple作为可变参数
print(calc(1,2))
#传入可变参数
nums = [1,2,3]
print(calc(*nums))
nums = [1,2,3]
#给change函数传入nums可变参数，到函数后会变成tuple。
#def change(*numbers):
#    numbers[0] = 3
#change(*nums)
#print(nums)
#关键字参数：允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个**dict**
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',job='Engineer')
extra = {'city':'Beijing','job':'Engineer'}
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
person('Jack',24,city=extra['city'],job=extra['job'])
#也使用可以简化的写法
person('Jack',24,**extra)
#命名关键字参数：
#通过if in 检查是否存在city和job参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name=',name,'age=',age,'other=',kw)
#但依然无法限制调用者传入关键字参数
person('hacker',22,city='neimenggu',addr='huhehot',zipcode=123456)
#可以通过以下方式限制关键字的名字-->**命名关键字参数**
#命名关键字参数，调用者在调用函数时必须给命名关键字参数进行赋值
def person(name,age,*,city,job):
    print(name,age,city,job)
person("jack",24,city="beijing",job='')
#下面这种情况也是一样
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#如果加city和job的参数名，则会被认为是位置参数，然后赋值给*args这个可变参数
#person('hacker',22,'NMG','IT')
#以下是正确的赋值方式
person('Jack',24,city='Beijing',job='Engineer')
#为避免以上情况，做进一步优化处理，给命名关键字参数添加缺省值，具体如下：
def person(name,age,*args,city='nmg',job='IT'):
    print('name=',name,'age=',age,args,'city=',city,'job=',job)
person('Hacker',22)
#参数组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
f1(1,2)
f1(1,2,3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',kw='d')
f2(1,2,d=99,kw=100)
#利用tuple或list和dist即可调用函数
args = (1,2,3,4)
kw={'d':99,'x':'#'}
f1(*args,**kw)
args = (1,2,3)
f2(*args,**kw)
def mul(x, *y):
    sum = x
    for n in y:
        sum = sum * n
    return sum
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

