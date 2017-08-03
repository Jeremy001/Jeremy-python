# encoding = utf-8

# load packages ====================================
import matplotlib.pyplot as plt
import numpy as np


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
from sklearn.preprocessing import StardardScaler
sc = StardardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# modeling ========================================
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C = 1000.0, random_state = 0)
lr.fit(X_train_std, y_train)

plot_decission_regions(X_combined_std, y_combined, classifier = lr, test_idx = range(105, 150))
plt.show()



















