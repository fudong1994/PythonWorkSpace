"""
-------------------------------------------------
   File Name:python_basic23
   Author:Lee
   date: 2021/5/26-14:40
-------------------------------------------------
"""

"""
本章讲解：集合 set
集合的定义：{value1,value2,value3.....}
集合的特征：无序、没有索引、不能重复
注意：集合只能存放不可变类型的元素
"""

# 1.集合的定义
set1 = {11, 22, 33, 44}
print(set1)  # {33, 11, 44, 22}  打印出来是无序的

# set2 = {11, 22, 33, [1, 2, 3], 'a'}  # 不能存放可变类型的数据

# 2.集合添加单个元素  add()
set1 = {11, 22, 33, 44, 'xiaohua', (1, 2, 3)}
set1.add(55)
print(set1)  # {33, 'xiaohua', 11, 44, (1, 2, 3), 22, 55}

# 3.集合添加多个元素  update()
set1 = {11, 22, 33, 44, 'xiaohua', (1, 2, 3)}
set1.update({0, 1, 2})
print(set1)  # {0, 33, 1, 2, 'xiaohua', 11, 44, (1, 2, 3), 22}

# 移除元素1  remove()  元素不存在时会报错
set1 = {11, 22, 33, 44, 'xiaohua', (1, 2, 3)}
set1.remove(11)
print(set1)  # {33, 44, 'xiaohua', (1, 2, 3), 22}
# set1.remove('a')  不存在时 会报错

# 5.移除元素2  discard()  元素不存在时不会报错
set1 = {11, 22, 33, 44, 'xiaohua', (1, 2, 3)}
set1.discard(11)
print(set1)  # {33, 'xiaohua', 44, (1, 2, 3), 22}
set1.discard(11)  # 不会报错

# 6.集合中的内容不能重复
set1 = {11, 22, 33, 44, 55, 11, 22}
print(set1)  # {33, 11, 44, 22, 55}
# 我们可以利用该特性对列表、元组数据进行去重
list1 = [11, 11, 11, 22, 3, 4, 5, 6]
print(list(set(list1)))  # [3, 4, 5, 6, 11, 22]

# 7.清空集合  clear()
set1 = {11, 22, 33, 44, 55, 11, 22}
set1.clear()
print(set1)  # set()

# 新建空集合
set2 = set()
print(type(set2))  # <class 'set'>

# 8.删除集合  del
del set1
# print(set1)  # NameError: name 'set1' is not defined

# 9.交集(intersection)    和 并集(union)
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1.intersection(set2))  # 交集  {3, 4, 5}

print(set1.union(set2))  # 并集 {1, 2, 3, 4, 5, 6, 7}

# 10.函数  len()/in/not in/max()/min()/sum()........
set1 = {1, 2, 3, 4, 5}
print(len(set1))  # 5

set2 = {3, 4, 5, 6, 7}
print(max(set2))  # 7
