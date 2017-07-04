# encoding = utf-8
import numpy as np
from matplotlib import pyplot as plt

# 定义x轴
# 从-π到π，256个点，包含端点值
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
c,s = np.cos(x),np.sin(x)
plt.figure(1)
plt.plot(x, c)
plt.plot(x, s)
plt.show()
















