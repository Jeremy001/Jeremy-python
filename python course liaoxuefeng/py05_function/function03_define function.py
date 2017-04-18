#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在python中定义函数的方法：
# def 函数名(参数1, 参数2):
#       函数体
#       return
# 函数的返回值用return
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
my_abs(9)
my_abs(-6)

# 导入函数的方法
# 把my_abs()函数定义保存你为abstest.py文件，则可以通过from abstest imort my_abs来导入my_abs()函数
from abstest import my_abs
my_abs(9)
my_abs(-6)

# 空函数
# 什么事情也不做，用pass
def nop():
    pass
# pass语句可以作为占位符，比如函数中返回什么值还没考虑好，可以先用pass代替，运行时就不会报错；
def adult(age):
    if age >= 18:
        pass

# 参数检查
# 调用函数时，如果参数个数不对，会报错提示：
# my_abs(1, 2, 3)
# 但参数数据类型不符合要求，我们定义的my_abs就有问题:
# my_abs('9')
# abs('9')
# 内置函数abs报错提示错误原因，而我们定义的函数my_abs()不会提示错误原因
# 我们修改一下函数的定义，先判断一下参数的数据类型，用isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# my_abs('9')


# 返回多个值
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 以上返回的多个值其实是假象，实际返回的是一个值
r = move(x = 100, y = 100, step = 60, angle = math.pi / 6)
print(r)
# 返回的r实际上是一个tuple，多个变量可以同时接收一个tuple，然后按照位置赋值

# practice
import math
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        return TypeError('bad operand type(a)')
    if not isinstance(b, (int, float)):
        return TypeError('bad operand type(b)')
    if not isinstance(c, (int, float)):
        return TypeError('bad operand type(c)')
    if a == 0:
        if b == 0:
            if c == 0:
                print('x为任意值')
            else:
                x = '此方程无解'
                return x
        else:
            x = -c/b
            return x
    else:
        deta = b * b - 4 * a * c
        if deta < 0:
            x = '无实数解'
            return x
        else:
            x1 = (math.sqrt(deta) - b) / (2 * a)
            x2 = -(math.sqrt(deta) + b) / (2 * a)
            return x1, x2
r = quadratic(1, 1, 1)
print(r)

