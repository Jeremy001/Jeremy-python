# -*- coding: utf-8 -*-

# load packages ======================================
import pandas as pd
import numpy as np


# read dataset =======================================
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
df_wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','intensity','Hue','OD280/OD315 of diluted wines','Proline']
print('class labels:', np.unique(df_wine['Class Label']))
print(df_wine.head())

# 数据集分为3个类别，1/2/3，分别代表3个葡萄品种

# 把数据集随机分割成训练集和测试集
from sklearn.cross_validation import train_test_split
# 把wine数据的特征矩阵赋值给X，把类别变量赋值给y
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# 设置test_size=0.3,使得训练集占Wine样本数的70%，测试集占30%





















