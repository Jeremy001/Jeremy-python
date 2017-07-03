# encoding = utf-8

# import
import numpy as np

lst = [[1, 3, 5], [2, 4, 6]]
print(type(lst))

# numpy array
np_lst = np.array(lst)
print(type(np_lst))

# 定义numpy array元素的数据类型
ny_lst = np.array(lst, dtype = np.float)

# numpy array的属性
print(np_lst.shape)
print(np_lst.ndim)
print(np_lst.dtype)
print(np_lst.itemsize)
print(np_lst.size)

# numpy array自带的数组
print(np.zeros([2,3]))
print(np.ones([2,3]))
# 一个随机数（0-1之间）
print(np.random.rand())
# 随机数矩阵（均匀分布）
print(np.random.rand(2, 3))
# 一个随机整数（设置整数范围）
print(np.random.randint(1, 10))  # 1-10之间
# 多个随机整数
print(np.random.randint(1, 10, 3))
# 一个标准正态分布随机数
print(np.random.randn())  # 标准正态分布
# 一个标准正态分布随机数组
print(np.random.randn(2, 4))
# 问题：如何生成既定均值和标准差的正态分布随机数？
# 从给定数据范围中随机抽取
print(np.random.choice([10, 20, 30, 40, 50]))
# 根据分布名称来生成随机数
print('distribute:')
print(np.random.beta(1, 10, 20))  # beta分布
# 以上是用beta分布举例，可以设置很多其他的分布


# 数组的常用操作

# 等差数列，从1开始，到11结束（不包括11）
print(np.arange(1, 11))
print(np.arange(1, 11).reshape([2, 5]))
print(np.arange(1, 11).reshape([2, -1]))

# 函数
lst = np.arange(1, 11).reshape([2, 5])
print(np.exp(lst))  # 指数
print(np.exp2(lst))  # 平方
print(np.sqrt(lst))  #开二次方
print(np.sin(lst))  # 三角函数
print(np.log(lst))  # 对数

# 聚合函数
lst = np.array([[[1, 2, 3, 4],
               [4, 5, 6, 7]],
               [[7, 8, 9, 10],
               [10, 11, 12, 13]],
               [[14, 15, 16, 17],
               [18, 19, 20, 21]]
               ])
# sum
print(lst.sum())
print(lst.sum(axis = 0))
print(lst.sum(axis = 1))
print(lst.sum(axis = 2))
# max
print(lst.max())
print(lst.max(axis = 0))
print(lst.max(axis = 1))
print(lst.max(axis = 2))
# min
print(lst.min())
print(lst.min(axis = 0))
print(lst.min(axis = 1))
print(lst.min(axis = 2))

# 对两个数组的操作
lst1 = np.array([1, 2, 3, 4])
lst2 = np.array([7, 3, 4, 1])
print(lst1 + lst2)
print(lst1 - lst2)
print(lst1 * lst2)
print(lst1 / lst2)
print(lst1 == lst2)  # 判断两个数组的对应元素是否相等
print(lst1**2)  # 平方
print(lst1.reshape([2, 2]))
print(np.dot(lst1.reshape([2, 2]), lst2.reshape([2, 2])))  # 点乘，即矩阵乘法

# 数组合并
print(np.concatenate((lst1, lst2), axis = 0))
print(np.vstack((lst1, lst2)))
print(np.hstack((lst1, lst2)))

# 数组拆分
print(np.split(lst1, 2))
print(np.split(lst1, 4))
print(np.split(np.hstack((lst1, lst2)), 2))
# 问题：如何根据行、列（维度）拆分数组？

# 数组复制
print(np.copy(lst1))
