# -*- coding: utf-8 -*-

# load packages ==============================================
import numpy as np
import pandas as pd

# Series ===================================================
# s = pd.Series(data, index = index)
# 1.data can be many different things
# 2.index argument can be missing

# 1.1 data is ndarray
s = pd.Series(np.random.randn(5), 
                        index = ['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)
s2 = pd.Series(np.random.randn(5))
print(s2)
print(s2.index)

# 1.2 data is dict
d = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(d)
print(s)
print(s.index)
s = pd.Series(d, index = ['b', 'd', 'c', 'a'])
print(s)
print(s.index)

# 1.3 scalar value
s = pd.Series(5., index = ['a', 'b', 'c', 'd', 'e'])
print(s)

# slicing
# 1. ndarray
s = pd.Series(np.random.randn(5), 
                        index = ['a', 'b', 'c', 'd', 'e'])
print(s)
print(s[0])
print(s[:3])
print(s[s > s.median()])
print(s[[4, 3, 2]])
print(np.exp(s))

# 2.dict
print(s['a'])
print(s['a'] > 1)
print('e' in s)
print('f' in s)
# print(s['f'])     # get an error
print(s.get('f'))
print(s.get('e'))
print(s.get('f', np.nan))




# dict ====================================================





























