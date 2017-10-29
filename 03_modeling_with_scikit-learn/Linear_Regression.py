# -*- coding: utf-8 -*-

# load packages ===============================================
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# load dataset ================================================
diabetes = datasets.load_diabetes()

# use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# split data into training and test data
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# split target into training and test
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# create linear regression objects
regr = linear_model.LinearRegression()

# train model using train data
regr.fit(diabetes_X_train, diabetes_y_train)

# make prediction using test data
diabetes_y_pred = regr.predict(diabetes_X_test)

# the coefficients
print("Coefficients:", regr.coef_)
# the mean squared error
print("Mean Squared Error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Variance score
print('Variance score:%.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# plot
plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.plot(diabetes_X_test, diabetes_y_pred, color = 'blue', linewidth = 3)
plt.show()


