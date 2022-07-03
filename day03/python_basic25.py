"""
-------------------------------------------------
   File Name:python_basic25
   Author:Lee
   date: 2021/5/26-16:44
-------------------------------------------------
"""
"""

python的数据类型：
数字、字符串、列表、元组、集合、字典

可变类型：列表、集合、字典
不可变类型：数字、字符串、元组

有序的：字符串、列表、元组
无序的：数字、集合、字典

"""

"""
可变类型和不可变类型的区别
"""

# 1.区分重新赋值和更改内容
a = 100
a = 200  # 此处是重新赋值

# 2.可变类型可以修改内容，比如列表类型
list1 = ['xiaohua', 'xiaoliu', 'xiaowang']
print(id(list1))  # 1516515779144
list1[0] = 'xiaoxu'  # 列表可以修改内容，物理地址不变
print(id(list1))  # 1516515779144

# 3.不可变类型不能修改内容
phone_num = '18866665555'
phone_num[1] = '6'
print(phone_num)  # TypeError: 'str' object does not support item assignment  str类型不支持该操作
