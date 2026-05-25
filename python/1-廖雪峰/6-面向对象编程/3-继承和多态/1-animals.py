# /usr/bin/env python
# -*- coding: utf-8 -*-
class Animal(object):
  def run(self):
    print('Animal is running...')
class Dog(Animal):
    def run(self):
       print('Dog is running...')
class Cat(Animal):
   def run(self):
      print('Cat is running...')
Dog().run()
Cat().run()

def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())

print(type(Dog()))

a = Animal()
d = Dog()
c = Cat()
print(isinstance(a,Animal))
print(isinstance(d,Animal))
print(isinstance(c,Animal))
print(isinstance(d,Dog))
print(isinstance(c,Dog))
print(isinstance(d,Cat))
print(isinstance(c,Cat))
print(isinstance([1, 2, 3], (list, tuple)))
print(dir('1213'))
class MyObject(object):
   def __init__(self):
        self.x = 9
        def power(self):
           return self.x *self.x
obj = MyObject()
setattr(Cat,'gender','man')
print(getattr(Cat,'gender'))
print(hasattr(Cat,'gender'))


def count():
    f = lambda : i * i
    fs = []
    for i in range(1, 4):
        fs.append(f()) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()

print(f1, f2, f3)