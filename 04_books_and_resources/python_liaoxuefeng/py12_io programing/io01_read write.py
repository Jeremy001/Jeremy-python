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

# read()：调用文件中的所有内容；
# read(size):调用设定大小的文本内容：size个字节
# readlines():每次读取一行；
# 如果文件很小，用read()一次性读取所有内容
# 如果文件大写未知，用read(size)，设置size，保险一些
# 如果希望按行读取，用readlines()
with open('text.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

# 读取二进制文件，如图片或视频，'r'改成'rb'

# 字符编码
# 读取非utf-8编码的文件，需要给open()加上encoding参数
f = open('text.txt', 'r', encoding = 'gbk')
f.read()
# 忽略错误
f = open('text.txt', 'r', encoding = 'gbk', errors = 'ignore')
f.read()

# 写文件，格式一样， 区别是'r'改成'w'(一般文件)/'wb'(二进制文件)
f = open('text.txt', 'w')
f.write('oh my god!')
f.close()
# 写文件时，操作系统往往不会直接写入磁盘，而是先写入内存中缓存起来，然后有空的时候慢慢写入磁盘；
# 只有调用了close()方法时，操作系统才能保证把数据全部写入了磁盘
with open('text.txt', 'w') as f:
    f.write('haha, I\'m coming!')
