# -*- coding: utf-8 -*-

# 对于大部分机器学习算法和优化算法来说，如果特征都在同一范围内，会获得更好的结果
# 有两种方法能使不同的特征有相同的取值范围：归一化(normalization)和标准化(standardization)
# 归一化指的是将特征范围缩放到[0,1]，是最小-最大缩放(min-max scaling)的特例
# 标准化，将特征值缩放到以0为中心，标准差为1的正态分布

# load packages =====================================
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# datasets =========================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
# split data into train and test dataset
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# normalization ======================================
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.fit_transform(X_test)

print(X_train[1:6,])
print(X_train_norm[1:6,])

 # standardization ====================================
from sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.fit_transform(X_test)

print('-------------------------')
print(X_train_std[1:6,])



















