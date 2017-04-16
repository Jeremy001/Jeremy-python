#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# if:如果条件为true，则%#￥@，否则啥也不干
age = 20
if age >= 18:   # 注意这里有个冒号！！！
    print('Your age is:', age)
    print('Adult')

# if else:如果条件为true，则干abcd，否则干1234
age = 3
if age >= 18:
    print('Your age is:', age)
    print('Adult')
else:
    print('Your age is:', age)
    print('Teenager')

# if elif else:如果条件1满足，则执行if后面的动作；否则看是否满足条件2，满足的话执行elif后面的动作，否则执行else后面的动作
age = 12
if age >= 18:
    print('Your age is:', age)
    print('Adult')
elif age >= 6:
    print('Your age is:', age)
    print('Teenager')
else:
    print('Your age is:', age)
    print('kid')

# if条件可以简写：
x = 1
if x:
    print('True')
# 只要x是非零数值，非空字符串，非空list，就判断为true，否则为false

# if and input()
age = input('你的出生年份:')
if age >= 2000:
    print('欢迎你，00后！')
else:
     print('你走吧，00前！')
# 上一段代码会报错，TypeError:unorderable types: str() >= int()
# 原因是输入的年份是字符串类型，需要转换成数值类型：
age = input('你的出生年份：')
age = int(age)
if age >= 2000:
    print('欢迎你，00后')
else:
    print('你走吧，00前，这里不欢迎你！')

# practice
height = 1.75
weight = 80.5
bmi = weight / (height ** 2)  # **表示阶乘
if bmi < 18.5:
    print('小明，你体重过轻！多吃点！')
elif bmi < 25:
    print('小明，你体重正常！继续保持！')
elif bmi < 28:
     print('小明，你体重过重！注意啦！')
elif bmi < 32:
     print('小明，你体重肥胖！还吃！！！')
else:
     print('小明，你体重严重肥胖！没救了！')
