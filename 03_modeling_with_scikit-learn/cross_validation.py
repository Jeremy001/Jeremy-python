# -*- coding: utf-8 -*-

# load packages ==============================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

# load data ==================================================
iris = datasets.load_iris()
print(iris.data.shape)
print(iris.target.shape)
# split data into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(iris.data,
                                                    iris.target,
                                                    test_size = .4,
                                                    random_state = 0)
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)

# modeling ==================================================
clf = svm.SVC(kernel = 'linear', C = 1).fit(X_train, y_train)
print(clf.score(X_test, y_test))

















