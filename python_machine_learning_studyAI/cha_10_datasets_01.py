# -*- coding: utf-8 -*-

# sklearn中的数据集有以下这些 ===================================
# 1.自带的小型数据集（较小）
#     sklearn.datasets.load_<name>
# 2.可在线下载的数据集（较大）
#     sklearn.datasets.fetch_<name>
# 3.计算机生成的数据集
#     sklearn.datasets.make_<name>
# 4.svmlight / libsvm格式的数据集
#     sklearn.datasets.load_svmlight_file(...)
# 5.从mldata在线下载获取数据集
#     sklearn.datasets.fetch_mldata(...)


# 1.自带的小型数据集（较小）====================================
#     sklearn.datasets.load_<name>

from sklearn.datasets import load_iris
iris = load_iris()
# 自带的数据集是Bunch类型，类似字典
# 打印iris键值对的键
print(iris.keys())
# 打印iris的目标变量的值
print(iris.target)
# 打印iris的样本值
print(iris.data)
# 打印目标变量值对应的具体含义
print(iris.target_names)
# 打印该数据集的说明文档
print(iris.DESCR)
# 打印改数据集的特征变量名称
print(iris.feature_names)
# 打印样本数和特征数
print(iris.data.shape)
# 打印第一个样本
print(iris.data[0])
# 打印前10个样本
print(iris.data[0:10])

# 统计三个分类出现的次数，bincount
import numpy as np
print(np.bincount(iris.target))

# 每个特征上绘制三个分类的直方图
import matplotlib.pyplot as plt
# 先绘制第一个特征
x_index = 3
colors = ['blue', 'red', 'green']

for label, color in zip(range(len(iris.target_names)), colors):
    plt.hist(iris.data[iris.target == label, x_index],
             label = iris.target_names[label],
             color = color)
plt.xlabel(iris.feature_names[x_index])
plt.legend(loc = 'upper right')
plt.show()
# 根据直方图，我们发现petal length是比较好的分类特征，petal width也不错
# 但是setosa比较好分类出来，但是另外两种可能不太好区分，分布重合度较高


# 两两特征绘制散点图
x_index = 0
y_index = 1
colors = ['red', 'blue', 'green']

for label, color in zip(range(len(iris.target_names)), colors):
    plt.scatter(iris.data[iris.target == label, x_index],
                iris.data[iris.target == label, y_index],
                label = iris.target_names[label],
                color = color)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
plt.legend(loc = 'upper right')
plt.show()









