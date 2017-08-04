# encoding = utf-8

# load packages ====================================
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets


# logistic function ===================================
def sigmod(z):
    return 1.0 / (1.0 + np.exp(-z))
z = np.arange(-7, 7, 0.1)
phi_z = sigmod(z)
plt.plot(phi_z)
plt.show()

# load dataset ======================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
np.unique(y)

# data pre-processing =================================
# 1.split data into train and test datasets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# 2.standardization
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# modeling ========================================
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C = 1000.0, random_state = 0)
lr.fit(X_train_std, y_train)




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

plot_decision_region(X_train_std, y_train, classifier = lr)
plt.show()



# regularization ===========================================
# 过拟合(overfitting)是机器学习中很常见的问题，指的是一个模型在训练集上表现很好但是泛化能力巨差(在测试集上的表现糟糕)。如果一个模型饱受过拟合困扰，我们也说此模型方差过高，造成这个结果的原因可能是模型含有太多参数导致模型过于复杂。
# 同样，模型也可能遇到欠拟合(underfitting)问题，我们也说此模型偏差过高，原因是模型过于简单不能学习到训练集中数据存在的模式，同样对于测试集表现很差
# 正则化是解决特征共线性、过滤数据中噪音和防止过拟合的有用方法

weights, params = [], []
for c in np.arange(-5, 5):
    lr = LogisticRegression(C = 10**c, random_state = 0)
    lr.fit(X_train_std, y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)

weights = np.array(weights)

plt.plot(params, weights[:, 0], label = 'petal length')
plt.plot(params, weights[:, 1], linestyle = '--', label = 'petal width')
plt.ylabel('weight coefficient')
plt.xlabel('C')
plt.legend(loc = 'upper left')
plt.xscale('log')
plt.show()













