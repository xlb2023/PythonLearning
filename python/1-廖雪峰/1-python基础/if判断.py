#/usr/bin/env python3
# -*- encoding: utf-8 -*-

a=input()
a=float(a)
if a >32:
    print("过于肥胖")
elif a>=25 and a<=32:
    print("比较肥胖")
elif a>18.5 and a<25:
    print("正常")
else:
    print("过轻")

