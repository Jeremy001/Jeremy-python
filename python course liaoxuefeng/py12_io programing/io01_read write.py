#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 读文件的基本步骤：
# open
# read
# close

f = open('text.txt', 'r')   # 路径 + 文件名 + 文件后缀，读的方式，'r'表示读
text = f.read()    # read()方法：一次性读取文件的所有内容，适合小文件，不适合大文件
print(text)
f.close()   # 读文件结束后要关闭，因为文件对象占用操作系统的资源

# 如果文件不存在，报IOError的错误
# 由于文件读写过程中都可能产生IOError的错误，一旦出错，后面的f.close()就不会调用，
# 为了保证无论是否调用都正确地关闭文件，可以用try ... finally来实现
try:
    f = open('text.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 但每次都这么写太繁琐了，python引入with语句自动调用close()方法：
with open('text.txt', 'r') as f:
    print(f.read())




































