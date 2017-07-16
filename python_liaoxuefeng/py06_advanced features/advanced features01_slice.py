#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 取一个list或tuple中的部分元素
# 笨办法：
L1 = ('Jeremy', 'Sarah', 'Micheal', 'Steve', 'Adam')
L2 = ['Jeremy', 'Sarah', 'Micheal', 'Steve', 'Adam']
print(L1[0], L1[2], L1[4])
# 好办法：切片
print(L2[0:3])
# 从0开始，0可以省略
print(L2[:3])
# 可以从任意位置开始，只要不超过范围
print(L2[1:3])
# 也可以倒着来：
print(L2[-3:])    # 最后3个
print(L2[-3:-1])
print(L2[-1])   # 最后一个

# 切片操作很爽
L = list(range(100))
print(L)
# 前10个
print(L[0:10])
# 后10个
print(L[-10:])
# 前11-20个：
print(L[10:20])
# 前10个数，隔一个取一个数：0，2，4，6，。。。
print(L[:10:2])
# 所有数，每5个取一个数：
print(L[::5])
# 复制一个list
print(L[:])

# tuple的操作跟list完全一样

# 字符串也可以看作一个list
cha = 'ABCDEFG'
print(cha[0:3])
print(cha[-3:])
print(cha[::2])
