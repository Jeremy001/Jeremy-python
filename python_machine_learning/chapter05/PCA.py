# -*- coding: utf-8 -*-

# PCA(principal component analysis, 主成分分析)是一种被广泛使用的无监督的线性转换技术，主要用于降维
# 其他领域的应用还包括探索数据分析和股票交易的信号去噪，基因数据分析和基因表达。
# PCA根据特征之间的相关性帮助我们确定数据中存在的模式
# PCA方向极其容易受到数据中特征范围影响，所以在运用PCA前一定要做特征标准化，这样才能保证每维度特征的重要性等同。
# PCA的步骤：
# 1 将d维度原始数据标准化。
# 2 构建协方差矩阵。
# 3 求解协方差矩阵的特征向量和特征值。
# 4 选择值最大的k个特征值对应的特征向量，k就是新特征空间的维度，k<<d。
# 5 利用k特征向量构建映射矩阵。
# 6 将原始d维度的数据集X，通过映射矩阵W转换到k维度的特征子空间。

# load packages =============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1 将d维度原始数据标准化. =======================================

# read dataset 
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
# df_wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','intensity','Hue','OD280/OD315 of diluted wines','Proline']

# data preprocessing 
# split data into train and test dataset
from sklearn.cross_validation import train_test_split
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# Standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

# 2 构建协方差矩阵.============================================
import numpy as np
cov_mat = np.cov(X_train_std.T)
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)
print("\nEigenvalues \n%s" %eigen_vals)



# 3 求解协方差矩阵的特征向量和特征值。===============================



# 4 选择值最大的k个特征值对应的特征向量，k就是新特征空间的维度，k<<d。========




# 5 利用k特征向量构建映射矩阵.=====================================







# 6 将原始d维度的数据集X，通过映射矩阵W转换到k维度的特征子空间.=============
















