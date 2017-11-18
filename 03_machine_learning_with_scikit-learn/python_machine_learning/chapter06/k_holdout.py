# -*- coding: utf-8 -*-

# load packages =============================================
import pandas as pd
import numpy as np
import matplotlib as plt

# read dataset ===============================================
df_bcw = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data', header = None)


# data preprocessing ==========================================
# 1.标签转换
from sklearn.preprocessing import LabelEncoder
X = df_bcw.iloc[:, 2:].values
y = df_bcw.iloc[:, 1].values
print(np.unique(y))

le = LabelEncoder()
y = le.fit_transform(y)
print(np.unique(y))

# 2.把数据集拆分成训练集和测试集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# modeling ==================================================
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),
                              ('pca', PCA(n_components = 2)),
                              ('clf', LogisticRegression(random_state = 1))])

# k foldout交叉验证
from sklearn.cross_validation import StratifiedKFold
kfold = StratifiedKFold(y = y_train, n_folds = 10, random_state = 1)
scores = []

for k, (train, test) in enumerate(kfold):
    pipe_lr.fit(X_train[train], y_train[train])
    score = pipe_lr.score(X_train[test], y_train[test])
    scores.append(score)
    print("Fold:%s, Class dist.:%s, Acc:%.3f" % (k + 1, np.bincount(y_train[train]), score))

print('CV accuracy:%.3f +/- %.3f' % (np.mean(scores), np.std(scores)))


# sklearn还实现了一个直接得到交叉验证评估结果的方法cross_val_score(内部同样是分层k折交叉验证)
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(estimator = pipe_lr,
                                          X = X_train,
                                          y = y_train,
                                          cv = 10,
                                          n_jobs = 1)
print("CV accuracy: %s" %scores)
print('CV accuracy:%.3f +/- %.3f' % (np.mean(scores), np.std(scores)))






