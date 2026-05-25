# /usr/bin/env python3
# -*- encoding : utf-8 -*-

# __repr__ and __str__ are two special methods in Python that are used to define how an object is represented as a string.
class Student(object):
  def __init__(self,name):
    self.name = name
  def __str__(self):
    return 'Student object (name: %s)' % self.name
  __repr__ = __str__
print(Student('Michael'))

# __iter__ and __next__ are two special methods in Python that are used to define how an object can be iterated over.
class Fib(object):
  def __init__(self):
    self.a, self.b = 0, 1 # 初始化两个计数器a，b
  def __iter__(self):
    return self # 实例本身就是迭代对象，故返回自己
  def __next__(self):
    self.a, self.b = self.b, self.a + self.b # 计算下一个值
    if self.a > 100000: # 退出循环的条件
      raise StopIteration();
    return self.a # 返回下一个值
for n in Fib():
  print(n)
  #__getitem__  是一个特殊方法，用于定义当使用索引访问对象时的行为。
class Fib(object):
  def __getitem__(self, n):
    a, b = 1, 1
    for x in range(n):
      a, b = b, a + b
    return a
f = Fib()
print(f[0]) # 1
print(f[1]) # 1
print(f[2]) # 2
print(f[3]) # 3
 # 使用__getitem__ 可以实现切片（slice）操作
class Fib(object):
  def __getitem__(self, n):
    if isinstance(n, int): # n是索引
      a, b = 1, 1
      for x in range(n):
        a, b = b, a + b
      return a
    if isinstance(n, slice): # n是切片
        start = n.start
        stop = n.stop
        if start is None:
          start = 0
        a, b = 1, 1
        L = []
        for x in range(stop):
          if x >= start:
            L.append(a)
          a, b = b, a + b
        return L
f = Fib()
print(f[0:5]) # [1, 1, 2, 3, 5]


