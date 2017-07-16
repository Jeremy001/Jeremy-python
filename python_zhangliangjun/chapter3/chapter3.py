# -*- coding: utf-8 -*-

import pandas as pd
# 读取excel文件
catering_sale = './demo/data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col = u'日期')
print(data[1:5])
print(data.describe())
print(len(data))

# 绘制箱线图
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
p = data.boxplot()
# plt.show()

# 统计量
stats = data.describe()
stats.loc['range'] = stats.loc['max'] - stats.loc['min']
stats.loc['var'] = stats.loc['std'] / stats.loc['mean']
stats.loc['dis'] = stats.loc['75%'] - stats.loc['25%']
print(stats)


# 累计百分比，帕累托图
import pandas as pd
dish_profit = './demo/data/catering_dish_profit.xls'
data2 = pd.read_excel(dish_profit, index_col = u'菜品名')
print(data2.head())
print(len(data2))
data2.sort_values(by = u'盈利', ascending = False)
print(data2)

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure()
data2[u'盈利'].plot(kind = bar)







