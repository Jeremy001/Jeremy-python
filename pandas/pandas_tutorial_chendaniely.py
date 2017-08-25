# -*- coding: utf-8 -*-

# load packages ==========================================

import pandas as pd

df = pd.read_csv('../../scipy-2017-tutorial-pandas/data/gapminder.tsv',
                 delimiter = '\t')
print(df.head())
print(type(df))
print(df.shape)
print(df.info())
print(df.columns)

country_df = df['country']
print('--------------------------')
print(type(country_df))
print(country_df.shape)
print(country_df.head())

print(df[['country', 'continent', 'year']].head())

# 删除变量01
del df['country']
print(df.head())
# 删除变量02
df = df.drop('continent', axis = 1)
print('---------------------------------')
print(df.head())


# select columns and samples 01 ==============================
df = pd.read_csv('../../scipy-2017-tutorial-pandas/data/gapminder.tsv',
                 delimiter = '\t')
print(df.loc[0])
print(df.head())
print(df.loc[99])
print(df.tail())
print(df.iloc[-1])
print(df.ix[0])
print(df.ix[99])
print(df.ix[[0, 99, 999]])
print(df.ix[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])
print(df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']])
print(df.iloc[[0, 99, 999], [0, 3, 5]])

# select columns and samples 02 ==============================

le_mean = df['lifeExp'].mean()
print(le_mean)
print(df.loc[df['lifeExp'] >= le_mean, :].shape)


# group by ===============================================

# mean
# group by one column and summarise one column
df.groupby('year')
print(df.groupby('year')['lifeExp'].mean())
# group by one column and summarise multiple columns
print(df.groupby('year')['lifeExp', 'gdpPercap'].mean())
# group by mutiple columns and summarise multiple columns
print(df.groupby(['year', 'continent'])['lifeExp', 'gdpPercap'].mean())
# multiple and multiple and table
print((df.groupby(['year', 'continent'])['lifeExp', 'gdpPercap'].mean()).reset_index())

# nunique
print(df.groupby('continent')['country'].nunique())

# plot
gyle = df.groupby('year')['lifeExp'].mean()
import matplotlib.pyplot as plt
gyle.plot()
# plt.show()

df2 = gyle.reset_index()
print(df2.head())
df2.to_csv('./lifeExp_by_year.csv', index = False)


# merge union join ===============================================
df1 = pd.read_csv('../../scipy-2017-tutorial-pandas/data/concat_1.csv')
df2 = pd.read_csv('../../scipy-2017-tutorial-pandas/data/concat_2.csv')
df3 = pd.read_csv('../../scipy-2017-tutorial-pandas/data/concat_3.csv')
print('df1 ------------------------------------------')
print(df1)
print('df2 ------------------------------------------')
print(df2)
print('df3 ------------------------------------------')
print(df3)

row_concat = pd.concat([df1, df2, df3])
print('row_concat ------------------------------')
print(row_concat)
print(row_concat.loc[0])
print(row_concat.iloc[0])

new_row1 = pd.Series(['n1', 'n2', 'n3', 'n4'])
new_row2 = pd.Series(['n5', 'n6', 'n7', 'n8'])
print(new_row1)
print(new_row2)
print(pd.concat([df1, new_row1]))






















