# -*- coding: utf-8 -*-

# load packages ==========================================

import pandas as pd

df = pd.read_csv('../scipy-2017-tutorial-pandas/data/gapminder.tsv',
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
df = pd.read_csv('../scipy-2017-tutorial-pandas/data/gapminder.tsv',
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
plt.show()

df2 = gyle.reset_index()
print(df2.head())
df2.to_csv('./lifeExp_by_year.csv', index = False)
