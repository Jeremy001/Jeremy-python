# -*- coding: utf-8 -*-

# 2.2.3 数据结构

# list and tuple
a = [1, 2, 3]
b = a
print(a)
print(b)
b[1] = 100
print(a)
print(b)

b2 = a[:]
print(b2)
b2[1] = 2
print(a)
print(b2)

l1 = list("abcd")
print(l1)
t1 = tuple([1, 2, 3, 'a'])
print(t1)

# list and tuple funciton

print(len(a))
print(max(a))
print(max(l1))
print(min(a))
print(min(l1))
print(sum(a))
# ?????????????
# print(sum(l1))
print(sorted(a))
# cmp?ô????أ?
# print(cmp(a, b))
# cmp(a[1], b2[3])

# function in list
a.append(1)
print(a.count(1))
print(a.extend([1, 2, 3]))
a.index(1)
a.insert(2, 1)
a.pop(1)

# 列表解析
a = [1, 2, 3]
b = []
for i in a:
    b.append(i + 2)
print(a)
print(b)
b = [i + 2 for i in a]
print(b)


# 字典dict
d = {'key1':1, 'key2':2}
print(d)
d = dict([['key1', 1], ['key2', 2]])
print(d)

# 集合set
s = {1, 2, 3, 2}
print(s)
s = set([1, 2, 3, 2])
print(s)
# 集合的运算
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)      # 交集（在s1和s2）
print(s1 | s2)      # 并集（在s1或s2）
print(s1 - s2)      # 差集（在s1，不在s2）
print(s1 ^ s2)      # 对称差集（在s1或s2，但不在两者的交集中）



# 函数式编程
# 函数式程序设计，泛函编程
# lambda(), map(), reduce(), filter()

# map()
# 用于逐一遍历
a = [1, 2, 3]
b = [i + 2 for i in a ]
print(b)
b = map(lambda x: x+2, a)
b = list(b)
print(b)
# map的速度比列表解析更快，因为列表解析实际上还是做for循环，但是map的效率原则上可以跟C语言媲美

# reduce
# 用于递归计算
from functools import reduce
# reduce(lambda x,y: x*y, range(1, n+1))
c = reduce(lambda x,y: x*y, range(1, 11))       # 10的阶乘
print(c)
c = 1
for i in range(1, 11):
    c = c * i
print(c)

# filter
# 用于过滤
f = filter(lambda x: x >5 and x < 8, range(10))
f = list(f)
print(f)
f = [i for i in range(10) if i > 5 and i < 8]
print(f)

# 用map(), reduce(), filter()是兼顾简洁和效率的，它们的运行速度比for循环快得多！



