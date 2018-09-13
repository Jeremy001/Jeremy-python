# encoding = utf-8

# load packages ====================================
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

# load dataset ======================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
# split data into train and test datasets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# modeling ========================================
from sklearn.tree import DecisionTreeClassifier
# 使用熵作为度量，训练一颗最大深度为3的决策树
tree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 3, random_state = 0)
tree.fit(X_train, y_train)


# define plot_decision_region function ====================
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

# plot ============================================
plot_decision_region(X_train, y_train, classifier = tree)
plt.legend()
plt.show()

# 把模型输出保存为.dot文件 ==========================
from sklearn.tree import export_graphviz
export_graphviz(tree, out_file = 'tree.dot', feature_names = ['petal Length', 'petal Width'])





