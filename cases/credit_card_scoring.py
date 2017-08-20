# -*- coding: utf-8 -*-

# load packages =============================================
import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score   # 模型评估库
from sklearn.ensemble import RandomForestClassifier   # 导入随机森林算法库
from sklearn.model_selection import train_test_split    # 导入分割数据集的库
from sklearn.model_selection import StratifiedShuffleSplit, GridSearchCV

# read dataset ==============================================
train_df = pd.read_csv('./data/cs_train.csv', header = 0)
print(train_df.head())
print(train_df.columns)
print(train_df.info())
# 发现MonthlyIncome\NumberOfDependents两个变量有缺失值




# missing value and outliers ====================================
print(train_df.isnull().sum())


# 缺失值处理方法：

# 1.删除法

# dataframe.dropna(axis = 0, how = 'any', thresh = None)
#     axis = 0, 删除样本；axis = 1, 删除特征列
#     how = 'any', 只要含有缺失值就删除；how = 'all', 全部为缺失值才删除
#     thresh = None, 不设阈值；thresh = 5
#     subset = ['column name'], 还可以通过设置subset参数来指定根据某列是否含有缺失值来删除样本

# 由于缺失值样本量较大，我们不采用删除法


# 2.替代法

# 比如用中位数/均值等替换掉nan值
# pandas.fillna()
train_df['MonthlyIncome'].fillna(train_df['MonthlyIncome'].median(), inplace = True)
train_df['NumberOfDependents'].fillna(train_df['NumberOfDependents'].median(), inplace = True)
print(train_df.isnull().sum())
# scikit-learn.Imputer()
from sklearn.preprocessing import Imputer
imr = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)
imr = imr.fit(train_df)
train_imputed = imr.transform(train_df.values)
print(train_df.isnull().sum())

# 3.预测法
# 用其他变量来预测带缺失值的变量
# （1）很可能预测不准确，因为不相关
# （2）如果预测准确，那么该变量与其他变量是多重共线性，可删除该变量


# 4.映射法
# 使用one-hot编码
# 优点：保留了样本的信息
# 缺点：增加了计算的复杂度

# 异常值


# split dataset ==============================================

# 随机划分
from sklearn.cross_validation import ShuffleSplit
rs = ShuffleSplit(6, n_iter = 1, test_size = 2, random_state = None)
for train_index, test_index in rs:
    print('Train:', train_index, 'Test:', test_index)

# 分层划分
# 比如性别特征变量的分布是男60%女40%，那么我们希望训练集和测试集中该变量的分布跟总体一致
from sklearn.cross_validation import StratifiedShuffleSplit
y = np.array([0, 0, 0, 1, 1, 1])
sss = StratifiedShuffleSplit(y, n_iter = 3, test_size = 2, random_state = 0)
for train_index, test_index in sss:
    print("Train:", train_index, "Test:", test_index)

# K折交叉验证
from sklearn.cross_validation import KFold
kf = KFold(6, n_folds = 3, shuffle = True, random_state = 0)
for train_index, test_index in kf:
    print("Train:", train_index, "Test:", test_index)

# 留一法
from sklearn.cross_validation import LeaveOneOut
loo = LeaveOneOut(6)
for train_index, test_index in loo:
    print("Train:", train_index, 'Test:', test_index)

# 把划分数据集与模型评估组合一起
from sklearn.cross_validation import StratifiedKFold
# scores = cross_val_score(estimator, X, y, cv = 10, scoring = 'accuracy')
# print(scores)
























