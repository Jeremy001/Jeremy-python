# encoding = utf-8

# load packages ========================================
import numpy as np
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt


# load datasets =========================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target


# data pre-processing ====================================
# split data into train and test datasets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
# standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)


# create datasets ========================================
np.random.seed(0)
X_xor = np.random.randn(200, 2)
y_xor = np.logical_xor(X_xor[:, 0] > 0, X_xor[:, 1] > 0)
y_xor = np.where(y_xor, 1, -1)
plt.scatter(X_xor[y_xor == 1, 0], X_xor[y_xor == 1, 1], 
                    c = 'b', marker = 'x', label = '1')
plt.scatter(X_xor[y_xor == -1, 0], X_xor[y_xor == -1, 1], 
                    c = 'r', marker = 's', label = '-1')
plt.legend()
plt.show()
# 如果要用线性超平面将正负类分开是不可能的，所以前面介绍的线性逻辑斯蒂回归和线性SVM都鞭长莫及。

# 可以用核函数来训练一个核SVM，从而对非线性可分的数据集映射到高维空间，从而实现线性可分
from sklearn.svm import SVC
svm = SVC(kernel = 'rbf', random_state = 0, gamma = 1.0, C = 10.0)
svm.fit(X_xor, y_xor)

# define plot_decision_region function ========================
from matplotlib.colors import ListedColormap
def plot_decision_region(X, y, classifier, resolution = 0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                                                np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)

    plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[y == cl, 0], y = X[y == cl, 1],
                            alpha = 0.8, c = cmap(idx),
                            marker = markers[idx], label = cl)


plot_decision_region(X_xor, y_xor, classifier = svm)
plt.show()

# 通过图形发现，分类效果还是很不错的

# 其中参数gamma可以被理解为高斯球面的阶段参数，如果我们增大gamma值，会产生更加柔软的决策界
# 以下案例用来理解gamma参数

svm1 = SVC(kernel = 'rbf', random_state = 0, gamma = 0.2, C = 1.0)
svm1.fit(X_train_std, y_train)
plot_decision_region(X_train_std, y_train, classifier = svm1)
plt.show()

svm2 = SVC(kernel = 'rbf', random_state = 0, gamma = 100, C = 1.0)
svm2.fit(X_train_std, y_train)
plot_decision_region(X_train_std, y_train, classifier = svm2)
plt.show()

# 虽然gamma值较大的模型对训练集分类效果很大，但其泛化能力一般很差，所以选择适当的gamma值有助于避免过拟合。



