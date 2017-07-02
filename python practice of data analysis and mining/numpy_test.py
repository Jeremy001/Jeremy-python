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
