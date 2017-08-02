# encoding = utf-8

# load packages ========================================
import numpy as np
from sklearn import datasets

# load datasets =========================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
np.unique(y)

# data pre-processing ====================================
# 1.split data into train and test datasets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# 2.standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# modeling ============================================
from sklearn.linear_model import Perceptron
ppn = Perceptron(n_iter = 40, eta0 = 0.01, random_state = 0)
'''
# n_iter: 对训练集的迭代次数
# eta0: 学习率
# 设置random_state参数使得shuffle结果可再现
'''
ppn.fit(X_train_std, y_train)

# prediction ============================================
y_pred = ppn.predict(X_test_std)
print('Misclassified sample:%d' % (y_test != y_pred).sum())

# model performance ======================================
from sklearn.metrics import accuracy_score
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))











