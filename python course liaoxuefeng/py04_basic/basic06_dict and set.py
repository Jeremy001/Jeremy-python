#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict
# python内置了字典；dict的支持，全称dictionary，以键值对存储，具有极快的查询速度
# 如果用list实现，则需要两个list：
names = ['Micheal', 'Jeremy', 'Sarah']
scores = [90, 84, 65]
# 如果给定一个名字，要查找对应的成绩，则需要先从names中找到对应的位置，然后到scores中查找对应的成绩
# 如果list很长，那么这样的查询消耗的时间就比较长
# 而用dict则可实现name-score的对照，查询的效率会大大提高，dict的查找就像查字典一样
d = {'Micheal' : 95, 'Jeremy' : 100, 'Sarah' : 88}
print(d)
print(d['Micheal'])    # 95

# 往dict中添加数据
d['Adam'] = 67
print(d)
print(d['Adam'])

# 如果往同一个key中多次放入数据，那么保留的是最后一次放入的数据
d['Jack'] = 99
print(d)
d['Jack']   # 99
d['Jack'] = 69
print(d)
d['Jack']   # 69

# key不存在的问题
# 查询的时候，key如果不存在，会报错
# d['Thomas']    # 报错 KeyError:"Thomas"

# 要避免Key不存在的错误，有下面有个方法：
# 1.先用in判断key是否存在，然后分别处理
'Thomas' in d   # false
# 2.通过dict的get方法，如果key不存在，可以返回none，或者自己指定的value
d.get('Thomas')    # 返回none，只是python并没有显示
d.get('Thomas', -1)    # 返回-1
print(d.get('Jack', '-1'))  # 如果存在，返回对应的值，不存在则返回指定的值

# 删除key和对应的值
d.pop('Adam')   # 显示对应删除的值67
print(d)    # 删除了Adam

# dict的特点是：
# 1. 插入和查询的速度极快，不会随着key的增加而变慢
# 2. 消耗内存多
# 而list的特点是：
# 1. 插入和查询的速度较慢，随着key的增加而变慢
# 2. 消耗内存少
# 所以dict是用空间来换时间

# dict可以用在很多需要高速查询的地方，key必须时候不可变对象
# 字符串、整数等都是不可变的，可以作为key，而list是可变的，不能作为key
# 但是对value没有要求：
d2 = {'key1':[1, 0, 0], 'key2':[0, 1, 0], 'key3':[0, 0, 1]}
print('d2:', d2)
print(d2['key1'])


# set

# set是一组key的集合，但不存储value，set中没有重复的key
s = set([1, 2, 3])
s    # 1, 2, 3
# 重复元素在set中会自动过滤
s = set([1, 2, 2, 3, 3, 1])
s   # 1, 2, 3

# 添加key，可以重复添加，但是结果不变
s.add(4)
s   # 1, 2, 3, 4
s.add(4)
s   # 1, 2, 3, 4

# 删除key，remove()
s.remove(4)
s   # 1, 2, 3

# set可以看作是数据意义上的无序和无重复元素的集合，set之间可以作交集/并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2    # 2, 3 交集
s1 | s2    # 1, 2, 3, 4 并集

# set和dict的唯一差别就是没存储value，所以性质相同，不能存储可变对象
# s = set(['Jeremy', [100, 45, 90, 78]])    # 报错：TypeErro:Unhashable type:'list'

# 不可变对象
# 对可变对象进行操作，对象会随之改变
a = ['c', 'a', 'b']
a.sort()
a   # a, b, c
# 对不可变对象进行操作，对象不会随之改变
a = 'abc'
a.replace('a', 'A')    # Abc
a   # abc
# 对不可变对象进行操作时，实际上是新键了一个变量指向变化后的值，而原对象指向的值不变

