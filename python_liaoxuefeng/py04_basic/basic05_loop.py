#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 为了进行重复的操作，一般用循环语句来实现

# 05.1 for ... in ...循环
names = ['Jeremy', 'Micheal', 'Sarah']
for name in names:
    print(name)

# 计算0-10的和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 整数序列range()
range(5)    # range(0, 5)
print(range(5))    # range(0, 5)
print(list(range(5)))    # [0, 1, 2, 3, 4]

# 计算0-100，不可能逐个写出0-100，可使用range()函数生成一个整数序列，然后通过list()函数转换成一个list
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


# 05.2  while循环
# 只要条件满足，就不断循环，直到条件不满足时跳出循环
# 计算100以内的所有奇数之和：
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)
# 另一种写法：
sum = 0
n = 1
while n < 100:
    sum = sum + n
    n = n + 2
print(sum)

# practice
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello, ', name)

# break语句，提前结束循环
# 无break，打印1-100
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
# 有break，打印1-10
n = 1
while n <= 100:
    print(n)
    n = n + 1
    if n > 10:
        break
print('END')

# continue语句，跳过当前这次循环，直接执行下一次循环
# 无continue语句，打印1-10：
n = 0
while n < 10:
    n = n + 1
    print(n)
print('END1')
# 加上continue语句，只打印1-10中的奇数：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:   # 取模==0，表示n为偶数
        continue
    print(n)
print('END2')
# 以上代码仔细思考一下，为什么：
# (1)n从0开始；
# 答：为了保证数字从1开始
# (2)n = n + 1要写在if n % 2 == 0 之前？
# 答：如果写在其之后，判断的就不是当前的数字，而是其变化之前的;
#         而且，如果写在其之后，n无法继续增加；程序应该只能跳过打印这个步骤，而不能跳过增加这个步骤

n = 11
while n > 0:
    n = n -1
    if n % 2 == 0:
        continue
    print(n)
print('End3')

# 特别注意：除非万不得已的情况，否则不要写break和continue，因为这两个语句写得不恰当的话，可能使程序进入死循环
# 退出死循环的方法：CTRL + C或强制结束python程序
