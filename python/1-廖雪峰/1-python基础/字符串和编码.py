#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

print('包含中文的str')
A = ord('A')
W = ord('中')
B = chr(66)
C = chr(25991)
print(A,'\n',W,'\n',B,'\n',C)
'ABC'.encode('ASCII')