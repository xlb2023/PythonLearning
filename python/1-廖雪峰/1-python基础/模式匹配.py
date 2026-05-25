#!/usr/bin/env python3
# -*- conding: utf-8 -*-

score = 'B'
match score:
    case 'A':
        print("score is A")
    case 'B':
        print("score is B")
    case 'C':
        print("score is C")
    case 'D':
        print("score is D")
    case _:
        print("score is ???")

#match的复杂匹配，可以匹配单个值、范围、也可以把匹配后的值捆绑到变量

age = 15

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print("10 years old")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 |18:
        print("11~18 years old")
    case 19:
        print("19 years old")
    case _:
        print('not sure')

#match匹配列表,可以匹配单个列表的值、可以匹配多个值、也可以把匹配后的值捆绑到变量

# args = ['gcc', 'hello.c', 'worald.c']
#args = ['clean']
# args = ['gcc']
args = [ ]

match args:
     # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定一个文件：
    case ['gcc',file1,*files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    case ['clean']:
        print('clean')
    case _:
         print('invalid command.')


