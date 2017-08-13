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
plt.xlim([10 ** (-5), 10 ** 5])
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc = 'upper left')
ax.legend(loc = 'upper center', bbox_to_anchor = (1.38, 1.03), ncol = 1, fancybox = True)
plt.show()
# 发现当C很小时，正则项的威力很大


# dimensionality reduction ============================
# 通过特征选择进行维度降低(dimensionality reduction)，维度降低有两种做法：特征选择(feature selection)和特征抽取(feature extraction)
# 特征选择会从原始特征集中选择一个子集合。特征抽取是从原始特征空间抽取信息，从而构建一个新的特征子空间

# SBS算法
# 一个经典的序列特征选择算法是序列后向选择(sequential backward selection, SBS),它能够降低原始特征维度提高计算效率，在某些情况下，如果模型过拟合，使用SBS后甚至能提高模型的预测能力
# python定义SBS算法
from sklearn.base import clone
from itertools import combinations
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

class SBS():
    def _init__(self, estimator, k_features, scoring = accuracy_score, test_size = 0.25, random_state = 1):
        self.scoring = scoring
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.test_size = test_size
        self.random_state = random_state

    def fit(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = self.test_size,
            random_state = self.random_state)
        dim = X_train.shape[1]
        self.indices = tuple(range(dim))
        self.subsets = [self.indices_]
        score = self._calc_score(X_train, y_train, X_test, y_test, self.indices_)
        self.scores_ = [score]

        while dim > self.k_features:
            scores = []
            subsets = []

            for p in combinations(self.indices_, r = dim - 1):
                score = self._calc_score(X_train, y_train, X_test, y_test, p)
                scores.append(score)
                subsets.append(p)

            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)
            dim -= 1
            self.scores_.append(scores[best])
        self.k_score_ = self.scores_[-1]

        return self
    def transform(self, X):
        return X[:, self.indices_]
    def _calc_score(self, X_train, y_train, X_test, y_test, indices):
        self.estimator.fit(X_train[:, indices], y_train)
        y_pred = self.estimator.predict(X_test[:, indices])
        score = self.scoring(y_test, y_pred)
        return score

# k_features参数:设定想要得到的特征子集数
# accuracy_score:评估模型在特征子集的表现


# 用KNN作为Estimator来运行SBS算法
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 2)
sbs = SBS(knn, k_features = 1)
sbs.fit(X_train_std, y_train)

# SBS算法记录了每一步最优特征子集的成绩，我们画出每个最优特征子集在验证集上的分类准确率：
k_feat = [len(k) for k in sbs.subsets_]
plt.plot(k_feat, sbs_scores_, marker = 'o')
plt.ylim([0.7, 1.1])
plt.ylabel('Accracy')
plt.xlabel("Number of features")
plt.grid()
plt.show()


