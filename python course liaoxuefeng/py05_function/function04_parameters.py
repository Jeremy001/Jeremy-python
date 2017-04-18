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

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
# 函数person除了必选参数name和age外，还包括关键字参数kw。
# 调用person函数时，可以只传入必选参数
person('Jeremy', 25)
# 也可以传入多个关键字参数
person('Jeremy', 25, city = 'hangzhou')
person('Jeremy', 25, gender = 'male', city = 'beijing')
# 关键字参数的使用场景可以是：传入的必选参数和非必选参数均有，同时非必选参数的个数不定
# 如果已经有一个dict，则也有笨/好两种办法用它作为参数：
extra = {'city':'beijing','job':'programmer'}
# 笨办法：
person('Jeremy', 25, city = extra['city'], job = extra['job'])
# 好办法：
person('Jeremy', 25, **extra)

# 命名关键字参数
# 检查关键字参数中是否有city/job参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# 以上定义的函数只是检查了一下是否包含city和job，实际调用的时候还是可以传入多个参数的：
person('Jeremy', 25, city = 'beijing', address = 'hangzhou', ziocode = 123456)
# 如果要限制输入的关键字参数，则可使用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
# 命名关键字参数和必选参数之间要用一个星号*隔开，*号后面的就是命名关键字参数
person('Jeremy', 25, city = 'beijing', job = 'programmer')
# 调用时，对于命名关键字参数，必须输入参数名，否则会报错
# 如果在命名关键字参数前还有可变参数，则不需要用星号*分隔开
def person(name, age, *arg, city, job):
    print(name, age, arg, city, job)
# 和其他参数一样，命名关键字参数也可以有默认值
def person(name, age, *, city = 'beijing', job)
    print(name, age, city, job)
person('Jeremy', 25, job = 'programmer')

# 参数组合
# python中定义函数时，可以将以上5中参数组合一起，顺序如下：
# 必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a = ', a, 'b =', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
# 在函数调用的时候，python解释器自动按照参数位置和参数名把对应的参数传进去
f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 'xx')
f2(1, 2, d = 99, ext = None)

# 可以通过list和tuple调用组合参数的函数
args = (1, 2, 3, 4)
kw = {'d':99, 'x':'#'}
f1(*args, **kw)
args = (1, 2, 3)
f2(*args, **kw)

