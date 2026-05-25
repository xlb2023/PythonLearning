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
  


