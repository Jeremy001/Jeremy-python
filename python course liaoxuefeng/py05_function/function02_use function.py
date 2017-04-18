#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python built-in functions:
# https://docs.python.org/3/library/functions.html#abs

# 调用函数 function(parameter1, parameter2, ...)
abs(1)
abs(-1)

# 调用函数时，如果：
# 1.传入的参数数量不对；
# 2.传入的参数的类型不对；
# 都会报TypeError的错误
abs(1, 2)
abs('12')

# 数据类型转换
int(123)
int(12.34)
float(12)   # 12.0
str(12.34)    # '12.34'
bool(12)    # True
bool('')    # False

# 把函数赋给一个变量，就是给函数命名一个别名
a = abs
a(-1)   # 1

# practice，把整数转换成十六进制
n1 = 255
n2 = 1000
print(hex(255), hex(1000))





























