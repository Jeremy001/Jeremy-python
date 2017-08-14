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
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import learning_curve

pipe_lr = Pipeline([('scl', StandardScaler()),
                              ('clf', LogisticRegression(penalty = '12', random_state = 0))])

train_sizes, train_scores, test_scores = learning_curve(estimator = pipe_lr,
                                                                                        X = X_train,
                                                                                        y = y_train,
                                                                                        train_sizes = np.linspace(0.1, 1.0, 10),
                                                                                        cv = 10)
train_mean = np.mean(train_scores, axis = 1)
train_std = np.std(train_scores, axis = 1)
test_mean = np.mean(test_scores, axis = 1)
test_std = np.std(test_scores,axis = 1)

# plot learning curve ============================================
plt.plot(train_sizes, train_mean, color = 'blue',
            marker = 'o', marker_size = 5, label = 'training accuracy')
plt.fill_between(train_sizes,
                         train_mean + train_std,
                         train_mean - train_std,
                         alpha = 0.15, color = 'blue')
plt.plot(train_sizes, test_mean, color = 'green', linestyle = '--',
            marker = 's', marker_size = 5, label = 'test accuracy')
plt.fill_between(train_sizes,
                         test_mean + test_std,
                         test_mean - test_std,
                         alpha = 0.15, color = 'green')
plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc = 'lower right')
plt.ylim([0.8, 1.0])
plt.show()


