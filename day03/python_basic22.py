"""
-------------------------------------------------
   File Name:python_basic22
   Author:Lee
   date: 2021/5/26-13:57
-------------------------------------------------
"""
"""
本章讲解：元组
元组的定义：用()存储一组数据，为不可变类型，创建后不能修改数据
            任意无符号的对象，以逗号隔开，默认为元组
            创建元组的主要符号是  逗号,
            元组也是序列之一
            (三大序列：str字符串/list列表/tuple元组)
"""

# 1.元组的创建
tup1 = ('xiaohua', 'xiaobai', 1, 2)
print(tup1)  # ('xiaohua', 'xiaobai', 1, 2)
print(type(tup1))  # <class 'tuple'>

tup2 = 1, 2, 3, 4
print(tup2)  # (1, 2, 3, 4)
print(type(tup2))  # <class 'tuple'>

tup3 = 1, 2, 3, 4, [1, 2, 34, 4]
print(tup3)  # (1, 2, 3, 4, [1, 2, 34, 4])
print(type(tup3))  # <class 'tuple'>

tup4 = 1,  # 元组如果只有一个成员，需要在成员后加逗号
print(tup4)  # (1,)
print(type(tup4))  # <class 'tuple'>

tup5 = (1)  # 这里虽然有() 但是这里其实声明的一个int类型
print(tup5)
print(type(tup5))  # <class 'int'>

tup6 = (1,)
print(type(tup6))  # <class 'tuple'>

# 2.查看元组中的数据：通过下标访问
tup7 = (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'], 'xiaohua', 'xiaobai', True)
print(tup7[2])  # 3
print(tup7[-1])  # True
print(tup7[-2][-3])  # b
print(tup7[6][3][0])  # c

# 3.元组切片
tup7 = (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'], 'xiaohua', 'xiaobai', True)
print(tup7[:3])  # (1, 2, 3)
print(tup7[2:6])  # (3,4,5,6)
print(tup7[2:6:2])  # (3,5)

# 4.元组中 count(),统计元素出现的次数
tup8 = ('a', 'b', 'c', 'd', 'e', 'f', 'f', 'a', 'c', 'd')
print(tup8.count('a'))  # 2
print(tup8.count('c'))  # 2

# 5.元组中的index(),查找元素的下标
tup7 = (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'], 'xiaohua', 'xiaobai', True)
print(tup7.index('xiaohua'))  # 7
print(tup7[6].index(3))  # 2   tup7[6]代表是元组里的那个列表
# print(tup7.index('c'))  # 'c'在元组中的列表里，不能直接查

# 6. 元组不能修改，但是可以拼接
# tup7[1] = 5  # 无法直接修改里面的元素

tup7 = (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'])
print(id(tup7))  # 2742556453904
tup8 = tup7 + ('A', 'B', 'C')
print(id(tup8))  # 2742556693064
print(tup8)  # (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'], 'A', 'B', 'C')

# 7.元组中的可变类型是可以修改的,且地址不变
tup7 = (1, 2, 3, 4, 5, 6, [1, 2, 3, 'c', 'd'])
print(id(tup7))  # 2356393693568
tup7[-1][2] = 'xiaohua'
print(id(tup7))  # 2356393693568
print(tup7)

"""
元组是不可变类型
列表是可变类型
"""

# 8.元组和其他序列一样都可以使用： +/*/len()/in/not in/max()/min()/sum()........

# 9.序列之间的互相转换

# 字符串转列表
str1 = 'abc'
list1 = list(str1)
print(list1)  # ['a', 'b', 'c']

# 字符串转元组
str1 = 'abc'
tup1 = tuple(str1)
print(tup1)  # ('a', 'b', 'c')

# 列表转元组
list1 = ['a', 'b', 'c']
tup1 = tuple(list1)
print(tup1)  # ('a', 'b', 'c')

# 列表转字符串
list1 = ['a', 'b', 'c']
str1 = str(list1)
print(str1, '他的类型是：', type(str1))  # "['a', 'b', 'c']" 他的类型是： <class 'str'>

# 如何把列表和元组的元素链接为字符串     join()
list1 = ['a', 'b', 'c']
str1 = ''.join(list1)
print(str1)  # abc

tup1 = ('1', '2', '3')
str2 = ''.join(tup1)
print(str2)  # 123

# 将字符串按照某些需求分割为列表
str1 = 'bcxkzbnclsagddgbwdbnxbchgldbchasbdjksablcxxzbclsb'
# 以's'字符进行分割
list1 = str1.split('s')
print(list1)  # ['bcxkzbncl', 'agddgbwdbnxbchgldbcha', 'bdjk', 'ablcxxzbcl', 'b']

# 去除下面字符串中的空格
str2 = 'daghd jakl hasdu hadh audh ualdh klahd lhagduwhdkahbdskj asd kas hdka sk lda dw dlw'

# 第一种
print(''.join(str2.split(' ')))

# 第二种
print(str2.replace(' ', ''))
