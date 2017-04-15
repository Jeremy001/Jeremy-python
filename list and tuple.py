# python内置的一种数据类型是列表：list；list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Tom', 'Jeremy', 'Micheal', 'Bob']
print(classmates)

# len()获取列表的元素个数
len(classmates)

# 索引获取列表中的元素
classmates[0]  # 第一个元素
classmates[1]  # 第二个元素
classmates[4]  # 报错IndexError，超出了列表的范围
# 最后一个元素的索引是len(classmates) - 1

# 索引获取排在后面的元素
classmates(-1)  # 最后一个元素
classmates(-2)  # 倒数第二个元素
classmates(-4)  # 倒数第四个(即第一个)元素
classmates(-5)  # 报错IndexError，超出了列表的范围

# list是一个可变的有序表，通过append()往list中追加元素到末尾
classmates.append('Sarah')
# 也可以把元素追加到指定位置
classmates.insert(1, 'Steve')

# 删除末尾的1个元素pop()
classmates.pop()
## 删除指定位置的元素pop(i)
classmates.pop(1)

# 修改某个元素的方法：直接赋值给相应的位置
classmates[2] = 'Mike'

# list中各个元素的类型可以不同
L = ['Jeremy', 25, 'male', False]
# list中的元素可以是list
L = ['Jeremy', 25, ['English', 'Mathmatics', 'Statistics', 'Chinese'], False]
# 或写作：
m = ['English', 'Mathmatics', 'Statistics', 'Chinese']
L = ['Jeremy', 25, m, False]
len(L)
# 注意L只有四个元素，其中第三个元素是一个list，这个list中也有四个元素
# 因此，L可以看作是一个二维数组，相应的有三维数组，四维数组。。。
# 要取到"Statistics",有两个方法：
m[2]
L[2][2]

# 如果list中一个元素都没有，那就是一个空list
L = []
len(L)


# 另一种有序列表叫元组tuple,tuple和list很相似，不过tuple创建之后就不能修改
classmates = ('Tom', 'Jeremy', 'Micheal', 'Bob')
# 现在classmates不能变了，它没有append(),insert(),pop()这些方法
# tuple中元素的引用方法与list相同，但是不能赋值为其他元素
# 为什么用tuple？就是因为tuple不可变，所以代码更安全，所以能用tuple的情况下，就尽量不要用list
# 当定义一个tuple的时候，它的元素就要确定下来：
t = (1, 2)
t
# 定义一个空的tuple
t = ()
t
# 但是，如果定义只有一个元素的tuple，则不能这么定义：t = (1); 而要这么定义：t = (1,)，即加一个的逗号

# tuple的不可变指的是元素指向性不可变：
m = ['Math', 'Chinese', 'English']
t = ('Jeremy', 25, m)
t
m[1] = 'Statistics'
t

# practice
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
