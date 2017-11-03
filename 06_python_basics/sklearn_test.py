# encoding = utf-8

import numpy as np
import pandas as pd

# Pre-processing数据预处理
from sklearn.datasets import load_iris
iris = load_iris()
print(iris)
print(type(iris))
from sklearn.cross_validation import train_test_split
train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size = 0.2, random_state = 1)
print(train_data)

# Modeling 建模
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion = "entropy")
# 建立模型
clf.fit(train_data, train_target)
# 预测
y_pred = clf.predict(test_data)


# Verify 模型验证
from sklearn import metrics
# 验证方法1：准确率得分
print(metrics.accuracy_score(y_true = test_target, y_pred = y_pred))
# 验证方法2：混淆矩阵
print(metrics.confusion_matrix(y_true = test_target, y_pred = y_pred))
# 横轴表示实际值，纵轴表示预测值
# 如本例中，有一条记录预测错误，实际为第二类，预测成第三类



# 决策树结果输出
with open("./data/tree.dot", "w") as fw:
    tree.export_graphviz(clf, out_file=fw)

