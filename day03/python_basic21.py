"""
-------------------------------------------------
   File Name:python_basic21
   Author:Lee
   date: 2021/5/25-16:27
-------------------------------------------------
"""

"""
本章讲解：列表

列表的定义：[]
列表的作用：可以存储任意类型一组数据
列表也是属于序列之一、列表是可变类型
"""

list1 = ['xiaohua', '小兰', '小风', [2, 3, 6, 8], 1, 5, True]
print(list1)  # ['xiaohua', '小兰', '小风', [2, 3, 6, 8], 1, 5, True]
print(list1[0])  # xiaohua
print(list1[-1])  # True
print(list1[3])  # [2,3,6,8]   list1列表的3号位置的元素
print(list1[3][2])  # 6  list1列表的3号位置的序列的2号位置的元素值
print(list1[0][0])  # x
# print(list1[4][0])  #  4号位置是一个int类型，是非序列，所以无法用下标去获取
print(id(list1))  # 1463350747784

# 通过下标修改值
list1[0] = '小张'
print(list1)  # ['小张', '小兰', '小风', [2, 3, 6, 8], 1, 5, True]
print(id(list1))  # 1463350747784   列表里元素值修改后，物理地址不变，因为列表是可变类型

# 字符串、数字都是不可变类型，所以重新赋值 物理地址变更
a = '666'
print(id(a))  # 1463351251832
a = '777'
print(id(a))  # 1463351251888

b = 1
print(id(b))  # 140735955915808
b = 10
print(id(b))  # 140735955916096

# 重新赋值
list1 = [1, 2, 3]  # 重新赋值会重新指向一个新的物理地址
print(id(list1))  # 1456003009288
list1 = [1, 2, 3]
print(id(list1))  # 2178657903240 即使完全相同的数据，物理地址也不一样

# 切片 和字符串类型相同
list1 = ['xiaohua', '小兰', '小风', [2, 3, 6, 8], 1, 5, True]
print(list1[2:5])  # ['小风', [2, 3, 6, 8], 1]

print(list1[:4])  # ['xiaohua', '小兰', '小风', [2, 3, 6, 8]]
print(list1[1:-5])  # ['小兰']
print(list1[:4:2])  # ['xiaohua', '小风']

# 在列表尾部增加单个元素： append()
list3 = [1, 2, 3, 4]
print(id(list3))  # 2821237793416
list3.append(5)
print(id(list3))  # 物理地址和修改前一致，因为列表是可变类型
print(list3)  # [1, 2, 3, 4, 5]

# 在指定位置添加单个元素： insert(index,value)  通过下标指定插入数据
list4 = [1, 4, 8, 9, 11]
list4.insert(3, 'a')
print(list4)  # [1, 4, 8, 'a', 9, 11]

# 在列表尾部添加多个元素 extend()   合并列表，无法指定位置，直接在尾部添加
list5 = [1, 4, 8, 9, 11]
list5.extend([1, 2, 3])
print(list5)  # [1, 4, 8, 9, 11, 1, 2, 3]

list6 = ['xiaohua', 'xiaohong']
list5.extend(list6)
print(list5)  # [1, 4, 8, 9, 11, 1, 2, 3, 'xiaohua', 'xiaohong']

# 删除元素方式1： remove()   根据元素值进行删除
list7 = ['a', 'b', 'c', 1, 2, 3]
list7.remove('b')
print(list7)  # ['a', 'c', 1, 2, 3]

list7 = ['a', 'b', 'c', 1, 2, 3, 'b']
list7.remove('b')
print(list7)  # ['a', 'c', 1, 2, 3, 'b']   删除第一次出现的元素

# 删除元素方式2: pop(index)  通过下标进行删除
list7 = ['a', 'b', 'c', 1, 2, 3, 'b']
list7.pop(3)
print(list7)  # ['a', 'b', 'c', 2, 3, 'b']

# 清空元素  clear()
list7 = ['a', 'b', 'c', 1, 2, 3, 'b']
list7.clear()  # 清空列表中所有数据，但是框架保留，且位置不变
print(list7)  # []

# 删除对象：使用 del      用法：del 对象   直接解除对物理内存的占用
del list7
# print(list7)  # 会报错，因为list7已经被从内存中释放了，所以程序不知道什么是list7

# 查找值对应的下标位置   .index()
list8 = ['a', 'b', 'c', 1, 2, 3, 'b']
res = list8.index('a')
print(res)  # 0

res1 = list8.index('b')
print(res1)  # 1  查找元素在序列里第一次出现的位置
# res2 = list8.index('z')
# print(res2)  # 会报错  ValueError: 'z' is not in list

# 查找元素出现的次数  .count()
list9 = ['a', 'b', 'c', 1, 2, 3, 'b']
res3 = list9.count('b')
print(res3)  # 2  b出现了2次

# 复制列表  .copy()
list10 = [1, 2, 3]
list11 = list10.copy()
print(list11)  # [1, 2, 3]
print(id(list10), id(list11))  # 2500949712968  2500949713032  地址不一样

list12 = list11
print(id(list11), id(list12))  # 2299242684616 2299242684616  地址相同

"""
注意：
.copy()复制和赋值的区别：copy会复制一个新的对象出来，赋值会使用同一个对象
"""

a = ['a', 'b', 'c']
b = a
c = a.copy()
# 如果这时我修改了a的列表数据，请问b和c 谁会跟着变化？
a.append('d')
print(a)  # ['a', 'b', 'c', 'd']
print(b)  # ['a', 'b', 'c', 'd']
print(c)  # ['a', 'b', 'c']
"""
注意： a和b 使用的同一对象，如果a和b任意一个产生变化，那么另外一个会跟着变化
    c和a使用的并非同一对象，不管是a是否变化，都不会影响c
"""

# sort() 升序，必须是纯数字或纯字符
# list14 = [1,6,3,7,5,'a']  会报错，必须是纯数字或纯字符
# list14 = ['a', '小虎', 'c', 'z', 'A', 'B']  # 纯字符可以排序
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
list14.sort()
print(list14)

# reverse() 颠倒
list15 = [6, 3, 2, 5, 1]
list15.reverse()
print(list15)  # [1, 5, 2, 3, 6]

# 降序方式1：先进行升序，再颠倒
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
list14.sort()
list14.reverse()
print(list14)  # [87, 33, 9, 7, 6, 5, 4, 3, 3, 3, 1]

# 降序方式2： sort() 默认是升序，如果将参数reverse的值设定为True则为降序
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
list14.sort(reverse=True)  # reverse控制是否需要进行颠倒， True:是  False:否
print(list14)  # [87, 33, 9, 7, 6, 5, 4, 3, 3, 3, 1]

# len()  求列表长度
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
print(len(list14))  # 11

# in  /  not   in
# in(在指定序列寻找指定值，找到返回True、否则返回False)
# not in(在指定序列寻找指定值，找不到返回True、否则返回False)
list15 = ['a', 'b', 'c']
bo1 = 'a' in list15
print(bo1)  # True
bo2 = 'a' not in list15
print(bo2)  # False

# max()   返回列表中最大值
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
print(max(list14))  # 87
list15 = ['a', 'b', 'c', 'z']
print(max(list15))  # z

# sum() 求和
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
print(sum(list14))  # 161

# 列表的 + 和 * 的操作 和字符串相同
list14 = [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3]
list15 = ['a', 'b', 'c', 'z']
print(list14 + list15)  # [9, 7, 3, 4, 5, 1, 3, 6, 87, 33, 3, 'a', 'b', 'c', 'z']
print(list15 * 3)  # ['a', 'b', 'c', 'z', 'a', 'b', 'c', 'z', 'a', 'b', 'c', 'z']


