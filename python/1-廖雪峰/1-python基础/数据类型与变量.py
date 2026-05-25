# 字符串
print("I'm OK")
print('I\'m learning \npython.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(r'''line1
line2\n
line3''')
# 布尔值
age = int(input('请输入年龄：'))
if age > 18:
    print("adult")
else:
    print('teenager') 
#变量:python是动态语言，不需要在创建变量时定义变量类型

#变量在计算机内存中的表示：创建变量的过程是先在内存中创建字符串ABC，再在内存中创建一个名为a的变量，并把它指向‘ABC’

a = 'ABC'
b = a
a = 'XYZ'
print(b)

n = 123
f = 456.789
s1 = "'Hello, world'"
s2 = "\'Hello, \\\'Adam\\\'\'"
s3 = "\r\'Hello, \"Bart\"\'"
s4 = '''r\'\'\'Hello,
Lisa!\'\'\''''
print('n =',n,'\n','f =',f,'\n','s1 =',s1,'\n','s2 =',s2,'\n','s3 =',s3,'\n','s4 =',s4)

# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。

# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。

