#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#test01
100 + 200
print(100 + 200 + 300)
print('hello, world!')
print('hello','my name is','Jeremy')
print('100 + 200 =', 100 + 200)
# name = input('Please Enter Your Name:')
# print('hello,',name)
print('1024 * 768 =', 1024 * 768)
# print absolute value of an integer
a = -10
if a >= 0:
    print(a)
else:
    print(-a)
print(0x0001)
print("I'm ok!")
# 转义字符/
print('I\'m ok!')
# 转义字符可以转义很多字符，如\n:换行；\t:制表符；\\:\字符
print("I\'m learning \n python!")
print("\\\n\\")
# 用r' '来表示' ' 中的内容不转义
print(r'\\\t\\', "\\\t\\")
# 用'''...'''表示多行文本
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')
age = 19
if age >= 18:
    print('adult')
else:
    print('teenager')
# =:赋值符号，同一个变量可以多次赋值，而且每次赋值的数据类型可以不同
# 因此：python是动态语言；而java则不可以，所以java是静态语言
