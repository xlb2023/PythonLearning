#!/usr/bin/env python3
#-*- encoding : utf-8 -*-

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+x
print(sum)

# range(101)  0~100
sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

n = 0
while n<3:
   print(L[n])
   n = n + 1

#break:结束循环
# n= 1
# while n<=100:
#     if n>10:
#         break
#     print(n)
#     n = n+1
# print("END")
#contiune:跳过这次循环
n = 0
while n< 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
