# -*- coding: utf-8 -*-


# 如果一个模型在训练集的表现比测试集好很多，那我们就要小心了，模型很可能过拟合了。过拟合意味着模型捕捉了训练集中的特例模式，但对未知数据的泛化能力比较差，我们也说模型此时具有高方差。
# 模型过拟合的一个原因是对于给定的训练集数据，模型过于复杂，常用的减小泛化误差的做法包括：
# 收集更多的训练集数据
# 正则化，即引入模型复杂度的惩罚项
# 选择一个简单点的模型，参数少一点的
# 降低数据的维度


# load packages ======================================
import pandas as pd
import numpy as np



# read dataset =======================================
df_wine = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
df_wine.columns = ['Class Label','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','intensity','Hue','OD280/OD315 of diluted wines','Proline']

# 数据集分为3个类别，1/2/3，分别代表3个葡萄品种

# 把数据集随机分割成训练集和测试集
from sklearn.cross_validation import train_test_split
# 把wine数据的特征矩阵赋值给X，把类别变量赋值给y
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# 设置test_size=0.3,使得训练集占Wine样本数的70%，测试集占30%


# data preprocessing ==================================
# standardization
from sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.fit_transform(X_test)


# regularization =======================================
# 正则项是对现在损失函数的惩罚项，它鼓励权重参数取小一点的值，换句话说，正则项惩罚的是大权重参数。

# modeling
from sklearn.linear_model import LogisticRegression
# 设置惩罚方式为l1，即L1正则化
lr = LogisticRegression(penalty = 'l1', C = 0.1)
lr.fit(X_train_std, y_train)

# model performance
print("Training accuracy:", lr.score(X_train_std, y_train))
print("------------------------------")
print("Test accuracy:", lr.score(X_test_std, y_test))
# 发现模型在训练集和测试集上的精度没有显著差异，我们认为模型没有过拟合

# 由于Wine数据集是多类别数据，所以lr使用了One-vs-Rest(OvR)方法
print(lr.intercept_)
# 下面打印输出的结果是3个模型中每个变量的权重，发现不少变量的参数是0，意味着模型基本剔除了这些变量
# 因此L1正则可以用来做特征选择
print(lr.coef_)


# 画出正则路径，即不同正则威力下的不同特征的权重参数：
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.subplot(111)
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'pink', 'lightgreen', 'lightblue', 'gray', 'indigo', 'orange']
weights, params = [], []
for c in np.arange(-4, 6):
    lr = LogisticRegression(penalty = 'l1', C = 10 ** c, random_state = 0)
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10 ** c)

weights = np.array(weights)
for column, color in zip(range(weights.shape[1]), colors):
    plt.plot(params, weights[:, column], label = df_wine.columns[column + 1], color = color)

plt.axhline(0, color = 'black', linestyle = '--', linewidth = 3)
plt.show()







