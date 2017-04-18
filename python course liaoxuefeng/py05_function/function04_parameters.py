#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 位置参数
# 计算平方
def power(x):
    return x * x
power(5)

# 如果我们还想计算3次方、4次方、5次方。。。，最佳的方法肯定是定义一个函数，而不是定义多个函数
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 默认参数，如果多数情况下，我们只计算平方，那么可以设置n参数的默认值为2
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
power(5)
# 这样，当我们调用power(5)时相当于调用power(5, 2)
# 默认参数的注意事项：
# 1.默认参数排在必选参数后面，而不能放在前面
# 2.调用函数时，如果设置默认参数时不写参数名称，则要按照参数的顺序
# 3.调用函数时，如果不设置默认参数，则默认采用默认值

# 定义默认参数的值时，不能用可变对象，而要用不可变对象

# 可变参数
# a^2 + b^2 + c^2 + ...
# 定义一个参数，然后把list或者tuple传给这个参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc([1, 2, 3])
calc([1, 4, 6, 7])
# 以上代码有个缺点，就是调用的时候要组装一个list后者tuple，可对自定义的函数做个修改：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2, 3)
calc(1, 4, 6, 7)
# 在参数前面加上星号*，则number就是可变参数，可以传入任意多个值(0个也可以)
calc()
# 如果已经有一个list或tuple，想传入作为参数，怎么做呢？
nums = [1, 3, 5]
# 笨办法：
calc(nums[0], nums[1], nums[2])
# 好办法：
calc(*nums)




























