# -*- coding: utf-8 -*-

# numpy 数组
import numpy as np
a = np.array([1, 2, 3, 4, 0, -1, 5])
print(a)
print(a[:3])    # 切片，得到a的前三个元素
print(a.min())
a.sort()    # 对a排序（升序），相当于改变了a
print(a)
b = np.array([[1, 2, 3], [3, 4, 5]])    # 二维数组
print(b*b)

# scipy 矩阵
# 1.求解线性方程组
# 2x1 - x2^2 = 1
# x1^2 - x2 = 2
from scipy.optimize import fsolve
def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2**2 - 1, x1**2 - x2 - 2]
result = fsolve(f, [1, 1])  # 输入初始值[1,1]并求解
print(result)
# 2.数值积分
from scipy import integrate     # 导入积分函数
def g(x):
    return (1 - x**2) ** 0.5
pi_2, err = integrate.quad(g, -1, 1)    # 积分结果和误差
print(pi_2*2)


# matplotlib
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.sin(x) + 1
z = np.cos(x**2) + 1
plt.plot(x, y, label = '$\sin x + 1$', color = 'red', linewidth = 2)
plt.plot(x, z, 'b--', label = '$cos x^2 + 1$')
plt.xlabel("Time(s)")
plt.ylabel('Volt')
plt.title("A simple demo")
plt.ylim(0, 2.2)
plt.legend()
plt.show()




















