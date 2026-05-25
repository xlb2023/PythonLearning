# /usr/bin/env python3
# -*- encoding : utf-8 -*-

class Animal(object()):
    pass
# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass

#MixIn
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')
class CarnivorousMixIn(object):
    def eat(self):
        print('Eating meat...')
class Dog(Mammal,RunnableMixIn,CarnivorousMixIn):
    pass
import socket, threading
from socketserver import TCPServer, ForkingMixIn
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
from socketserver import UDPServer, ThreadingMixIn
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass