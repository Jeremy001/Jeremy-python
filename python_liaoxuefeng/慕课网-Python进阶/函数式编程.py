# encoding = utf-8

# python中变量可以指向函数
ab = abs
ab(-10)

# 高阶函数：可以以函数作为参数的函数
def add(x, y, f):
    return f(x) + f(y)

add(-5, 9, abs)



