#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在一个函数内部调用自身，这个函数就是递归函数，比如阶乘fact(n)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
# 递归函数优点是逻辑清晰，定义简单

# 栈溢出
# 函数调用是通过栈这一数据结构来实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，就会减一层栈帧
# 如果递归调用的次数太多，就会导致栈溢出
# print(fact(1000))    # 报错

# 尾递归，解决栈溢出的问题
# 尾递归的含义：函数返回的时候，调用函数本身，return语句不返回表达式
def fact(n):
    return fact_iter(n ,1)

def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n - 1, n * product)

# 但是python标准的解释器没有针对递归做优化，所以python中任何递归函数还是存在栈溢出的问题

# practice

def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    move(n -1, a, c, b)
    print('move', a, '--->', c)
    move(n -1, b, a, c)































