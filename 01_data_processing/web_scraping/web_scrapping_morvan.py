# -*- coding: utf-8 -*-

# 加载包
from urllib.request import urlopen

# 

html = urlopen('https://www.google.com').read()

print(html)








