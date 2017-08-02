# -*- coding: utf-8 -*-

# load packages =======================================
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

# load dataset =========================================
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
np.unique(y)

# data pre-processing ====================================
# split data into train and test datasets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# modeling ============================================
forest = RandomForestClassifier(criterion = 'entropy', n_estimators = 10, random_state = 1, n_jobs = 2)
forest.fit(X_train, y_train)





# plot ================================================
plot_decission_regions(X_combined, y_combined, classifier = forest, test_idx = range(105, 150))
plt.xlabel('Petal_length')
plt.ylabel('Petal_width')
plt.legend(loc = 'upper left')
plt.show()






