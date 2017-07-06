# encoding = utf-8
import numpy as np
from matplotlib import pyplot as plt

# 定义x轴
# 从-π到π，256个点，包含端点值
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
# cos(x), sin(x)
c,s = np.cos(x),np.sin(x)
plt.figure(1)
# 画图，设置线条颜色，线宽，线型，标签，透明度等
plt.plot(x, c, color = "blue", linewidth = 1.0, linestyle = "-", label = "COS", alpha = 0.5)
plt.plot(x, s, "r*", label = "SIN")
# 添加标题
plt.title("COS & SIN")
ax = plt.gca()  # 轴编辑器
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_position(("data",0))
ax.spines["bottom"].set_position(("data",0))
ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks(np.linspace(-1, 1, 5, endpoint = True))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor = "white", edgecolor = "none", alpha = 0.2))
# 设置图例
plt.legend(loc = "upper left")
# 设置网格线
plt.grid()
# 设置图形显示范围：前两个设置x轴的最小最大值， 后两个设置y轴的最小最大值
# plt.axis([-1, 1, -0.5, 1])
# 设置填充范围
plt.fill_between(x, np.abs(x)<0.5, c, c>0.5, color = "green", alpha = 0.25)
# 添加辅助线
t = 1
plt.plot([t, t], [0, np.cos(t)], "y", linewidth = 3, linestyle = "--")
# 添加注释文字
plt.annotate("cos(1)", xy=(t, np.cos(1)), xycoords = "data", xytext = (+10, +30), 
    textcoords = "offset points", arrowprops = dict(arrowstyle = "->", connectionstyle = "arc3, rad = .2"))
plt.show()



















