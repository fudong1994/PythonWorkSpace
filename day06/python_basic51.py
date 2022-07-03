"""
-------------------------------------------------
   File Name:python_basic51
   Author:Lee
   date: 2021/5/31-14:04
-------------------------------------------------
"""

"""
组包/装包：通俗的讲，组包就是把多个数据装在一个元组中
拆包/解包：把一组数据进行拆分，比如 列表/字典/元组等拆分成单个数据
"""

# 自动组包
num = 1, 2, 3
print(num)  # (1, 2, 3) 将多个元素组装成一个元组

group = 10, 'Tom', {'name': 'xiaohua', 'age': 18}
print(group)  # (10, 'Tom', {'name': 'xiaohua', 'age': 18})

# 自动拆包
my_list = ['xiaohua', 20, '1001']
name, age, num = my_list
print(name, age, num)  # xiaohua 20 1001

my_tuple = ('xiaohua', 20, '1001')
name, age, num = my_tuple
print(name, age, num)  # xiaohua 20 1001

my_dict = {'name': 'xiaohua', 'age': 18, 'num': '1002'}
n, a, nu = my_dict
print(n, a, nu)  # 字典在拆包的时候是把所有的key值进行拆分  name age num

# 在函数调用过程中，如果变量前边加 *号，代表拆包
print(*my_list)  # xiaohua 20 1001
print(*my_tuple)  # xiaohua 20 1001
print(*my_dict)  # name age num

# 注意：在拆包的过程中，我们可以利用*将多个变量的值存在一个列表中，用*表示组包
print('===' * 50)
names = ('小花', '小王', '小刘', '小林', '小龙')
name1, *name = names
print(name1)  # 小花
print(type(name1))  # <class 'str'>
print(name)  # ['小王', '小刘', '小林', '小龙']
print(type(name))  # <class 'list'>

print('===' * 50)

*name, name1 = names
print(name1)  # 小龙
print(name)  # ['小花', '小王', '小刘', '小林']

name1, *name, name2 = names
print(name1)  # 小花
print(name)  # ['小王', '小刘', '小林']
print(name2)  # 小龙
