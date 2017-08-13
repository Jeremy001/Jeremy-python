# -*- coding: utf-8 -*-


# 重复利用某些参数
# 利用管道pipeline

# load packages =============================================
import pandas as pd
import numpy as np
import matplotlib as plt

# read dataset ===============================================
# Breast Cancer Wisconsin数据集
# 569个样本。每一条数据前两列是唯一的ID和相应的类别值(M=恶性肿瘤，B=良性肿瘤)，第3-32列是实数值的特征

df_bcw = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data', header = None)

# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()


# data preprocessing ==========================================
# 1.标签转换
from sklearn.preprocessing import LabelEncoder
X = df_bcw.iloc[:, 2:].values
y = df_bcw.iloc[:, 1].values
print(np.unique(y))

le = LabelEncoder()
y = le.fit_transform(y)
print(np.unique(y))

# 疑问:标签转换时，可否指定正例？

# 2.把数据集拆分成训练集和测试集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# modeling ==================================================
# 将transformer和Estimator放入同一个管道
# 我们需要进行的处理有：
# 1.将特征变量标准化
# 2.PCA主成分分析降维
# 3.建模
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),
                              ('pca', PCA(n_components = 2)),
                              ('clf', LogisticRegression(random_state = 1))])
pipe_lr.fit(X_train, y_train)
print('Test Accuracy: %.3f' % pipe_lr.score(X_test, y_test))


