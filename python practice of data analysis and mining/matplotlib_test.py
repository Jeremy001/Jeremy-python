# encoding = utf-8
import numpy as np
from matplotlib import pyplot as plt

# 定义x轴
# 从-π到π，256个点，包含端点值
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
c,s = np.cos(x),np.sin(x)
plt.figure(1)
plt.plot(x, c, color = "blue", linewidth = 1.0, linestyle = "-", label = "COS", alpha = 0.5)
plt.plot(x, s, "r*", label = "SIN")
plt.title("COS & SIN")
ax = plt.gca()
ax.splines["right"].set_color("none")
ax.splines["top"].set_color("none")
ax.splines["left"].set_position(("data".0))
ax.splines["bottom"].set_position(("data".0))

plt.show()
















