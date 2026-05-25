#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

#取L列表的前n个元素

L=['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#方法一：

print(L[0],L[1],L[2])

#方法二：
#range(n)函数：其中的n指的是到索引n结束，但不包括索引n，索引默认从0开始。
r= []
for i in range(1,3):
    r.append(L[i])
print(r)
#方法三：*切片（Slice）*
#切片：L[x:y]指的是从索引x开始（包括），到y结束（排除），默认从0开始
#列表list切片
#前5个元素
print(L[:5])
#第2个和第3个元素
print(L[1:4])
#后2个元素
print(L[-2:])
#倒数第2个元素
print(L[-2:-1])
#取出双数索引的元素
print(L[::2])
#元组tuple切片
T=(0,1,2,3,4,5,6,7,8)
#前5个元素
print(T[:5])
#第2个和第3个元素
print(T[1:4])
#后2个元素
print(T[-2:])
#倒数第2个元素
print(T[-2:-1])
#取出双数索引的元素
print(T[::2])
#字符串String切片
S='abcdefghijklmn'
#前5个元素
print(S[:5])
#第2个和第3个元素
print(S[1:4])
#后2个元素
print(S[-2:])
#倒数第2个元素
print(S[-2:-1])
#取出双数索引的元素
print(S[::2])
#删除字符串首尾空格
# i = 0
# for x in 'abcdefjhigk'[i:i+1]:
#     print(x)
def trims(s):
    if s is None:
        print("s is NULL")
        return
    i = 0
    j = 0
    for ch in s:
        if ch == ' ':
            i = i+1
        else:
            break
    # while i<len(s) and s[i] == ' ':
    #     i = i + 1
    for ch in reversed(s):
        if ch == ' ':
            j = j+1
        else:
            break
    # while j+len(s)>0 and s[j] == ' ':
    #     j = j - 1
    # s=s[i:len(s)+j+1]
    s = s[i:len(s)-j]
    return s
if trims('hello  ') != 'hello':
    print('测试失败1!')
elif trims('  hello') != 'hello':
    print('测试失败2!')
elif trims('  hello  ') != 'hello':
    print('测试失败3!')
elif trims('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trims('') != '':
    print('测试失败5!')
elif trims('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')