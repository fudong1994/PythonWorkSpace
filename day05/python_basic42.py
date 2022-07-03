"""
-------------------------------------------------
   File Name:python_basic42
   Author:Lee
   date: 2021/5/28-14:22
-------------------------------------------------
"""
"""
for循环
for 变量 in 据可迭代数(str/list/tuple/set/dict):
    循环体
"""

# 值遍历    遍历：可以就是对象中的每一个元素都过一遍
set1 = {'11', '22', '33', '44'}
for i in set1:
    print(i)

list1 = [1, 2, 3, 34, 5, 5, 6, 7]
for i in list1:
    print(i, end=' ')

print()
print('111')

for i in range(5):  # range 如果只给一个参数，起始位置默认从0开始
    print(i)

# 通过下标遍历

list2 = ['xiaohua', 'xiaowang', 'xiaoliu']
#        list2[0]    list2[1]    list2[2]

for i in range(len(list2)):  # i = 0,1,2
    print(list2[i])

tup1 = (1, 2, 3, 4, 5, 6, 67, 7, 78, 1, 2, 3, 4, 5, 5, 5, 5)

for i in range(len(tup1)):
    print(tup1[i], end=' ')

# 练习 统计上面这个元组的5出现的次数
count = 0
for i in tup1:
    if i == 5:
        count += 1
print('5出现了{}次'.format(count))

# 练习 统计出'python is easy!' 中是否存在k
str1 = 'python is easy！'

is_ex = '不存在'  # 开关、标识符

for i in str1:
    if i == 'k':
        is_ex = '存在'
        break
print(is_ex)

dt = {'name': 'xiaohua', 'age': 19, 'sex': '女', 'nickname': 'xiaohua'}
keys_list = list(dt.keys())  # 获取所有的键 并且转换为list ['name', 'age', 'sex', 'nickname']
value_list = list(dt.values())  # 获取所有的值 并且转换为list ['xiaohua', 19, '女', 'xiaohua']
items_list = list(dt.items())
# 获取所有的键值对 并且转换为list [('name', 'xiaohua'), ('age', 19), ('sex', '女'), ('nickname', 'xiaohua')]
print(keys_list, value_list, items_list)

# 找出字典dt中 value值xiaohua 出现的次数
count = 0
for i in dt.values():
    if i == 'xiaohua':
        count += 1
print('xiaohua出现的次数：', count)

# 用两种方式遍历下面的字符串？
str1 = '生命诚可贵，爱情价更高，若为python顾，二者皆可抛'

# 值遍历
for i in str1:
    print(i, end='')

print()

# 下标遍历
for i in range(len(str1)):
    print(str1[i], end='')
