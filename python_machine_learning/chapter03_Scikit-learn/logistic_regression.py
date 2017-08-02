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
iris = 
# data pre-processing =================================


















