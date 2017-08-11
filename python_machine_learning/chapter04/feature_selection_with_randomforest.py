# -*- coding: utf-8 -*-

# 随机森林能够度量每个特征的重要性，我们可以依据这个重要性指标进而选择最重要的特征
# 在训练好随机森林模型后，直接调用feature_importances属性就能得到每个特征的重要性
# 对于基于树的模型，不必对特征进行标准化或归一化


# load packages ======================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read dataset =======================================
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
df_wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','intensity','Hue','OD280/OD315 of diluted wines','Proline']

# 把数据集随机分割成训练集和测试集
from sklearn.cross_validation import train_test_split
# 把wine数据的特征矩阵赋值给X，把类别变量赋值给y
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# 设置test_size=0.3,使得训练集占Wine样本数的70%，测试集占30%

# modeling =========================================
from sklearn.ensemble import RandomForestClassifier
feat_labels = df_wine.columns[1:]
forest = RandomForestClassifier(n_estimators = 10000, random_state = 0, n_jobs = -1)
forest.fit(X_train, y_train)
importances = forest.feature_importances_
indices = np.argsort(importances)[::-1]
for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30, feat_labels[f], importances[indices[f]]))

# 画出各特征的重要性排序
plt.title("Feature Importances")
plt.bar(range(X_train.shape[1]), 
            importances[indices], 
            color = 'lightblue',
            align ='center')
plt.xticks(range(X_train.shape[1]), 
                feat_labels, 
                rotation = 90)
plt.xlim([-1, X_train.shape[1]])
plt.tight_layout()
plt.show()



# sklearn的随机森林实现，包括一个transform方法能够基于用户给定的阈值进行特征选择
# 所以如果你要用RandomFroestClassifier作为特征选择器，这就很easy了
# 举个例子：设置阈值为0.15，会选择出三个维度特征，Alcohol、Malic acid和Ash。 

X_selected = forest.transform(X_train, threshold = 0.15)
print(X_selected.shape)
























