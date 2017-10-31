#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python中的字符串类型是str
# 编码问题：
# ASCII编码 -- GB2312 -- Unicode -- UTF-8
# 内存中，使用unicode编码，硬盘和传输的时候，使用UTF-8编码
# python3使用unicode编码，可以直接输出中文
print('包含中文的string')

# 单个字符，ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord("A")
ord("中")
chr(66)
chr(25991)

# 用十六进制写字符串：
'\u4e2d\u6587'
'中文'

# bytes类型：
x = b'ABC'
y = 'ABC'
print(x,y)

# 以unicode表示的str通过encode()方法可以编码为指定的bytes:
'ABC'.encode('ascii')
'中文'.encode('utf-8')
'中文'.encode('ascii')  # 报错，因为中文字符无法转换为ascii编码

# 如果我们从硬盘或网络上读取了字节流，那么读到的数据是bytes,通过decode()就可以把bytes转变成str
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 计算字符数：len(str)
len('ABC')  # 3个字符
len('中文')  # 2个字符

# 计算字节数：len(bytes)
len(b'ABC')  # 3个字节，可以看出1个英文字符占据1个字节
len(b'\xe4\xb8\xad\xe6\x96\x87')  # 6个字节，可以看出1个中文字符占据3个字节
len('中文'.encode('utf-8'))

# 在操作字符串时，经常互相转化bytes和str，在包含中文字符的时候，务必使用utf-8进行编码
# 因此，通常会在python文件的顶部增加下面两行注释：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行注释是告诉linux和OS X系统：这是一个Python可执行程序，windows系统会自动忽略这个注释
# 第二行注释是告诉Python解释器按照utf-8编码读取源代码，否则代码中的中文字符输出可能有乱码
# 同时，在写代码时，务必确保编辑器在使用utf-8 without BOM进行编码

# 格式化 %
# 输出类'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx是根据变量变化的
x = 'Hello, %s' % 'world'
print(x)
y = 'Hi, %s, your score is %d' % ('Micheal', 59.5)
print(y)
# %s:字符串;
# %d:整数;
# %f:浮点数;
# %x:十六进制整数;
# 对整数和浮点数，还可以设置整数前是否补零以及整数和小数的位数
x = '%2d-%02d' % (3, 1)
print(x)
pi = '%.2f' % 3.1415926
print(pi)
# 如果不太确定%后面应该跟什么，那么可以统一用%s， 它会把任何数据类型转换为字符串
x = 'Age:%s, Gender: %s' % (25, 'female')
print(x)
# 如果%本身就要保持为字符，那就需要转义：%%表示1个%：
x = 'percentage:%.2f%%' % 7.2364
print(x)
