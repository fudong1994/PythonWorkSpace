"""
-------------------------------------------------
   File Name:python_basic24
   Author:Lee
   date: 2021/5/26-15:44
-------------------------------------------------
"""

"""
字典：以key(键)-value(值)形式来保存数据 {key1:value1,key2:value2,key3:value3.....}
"""

"""
part01:字典的常见操作
"""

# 1. 字典的定义
dict1 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}

# 2.通过key获取value 方式1：
print(type(dict1))  # <class 'dict'>
print('name键对应的值为:', dict1['name'])  # name键对应的值为: xiaohua

# 3.通过key获取value 方式2：
print('name键对应的值为:', dict1.get('name'))  # name键对应的值为: xiaohua

# 4.增加单个键值对
dict1['class'] = '19班'
print(dict1)  # {'name': 'xiaohua', 'age': 18, 'sex': '女', 'class': '19班'}

# 5.增加多个键值对
dict1.update({'id': '1001', 'phone_num': 18656031111})
print(dict1)  # {'name': 'xiaohua', 'age': 18, 'sex': '女', 'class': '19班', 'id': '1001', 'phone_num': 18656031111}

# 6.修改value值
dict1['age'] = 19
print(dict1)  # {'name': 'xiaohua', 'age': 19, 'sex': '女', 'class': '19班', 'id': '1001', 'phone_num': 18656031111}

# 7.根据key删除value
dict1.pop('id')
print(dict1)  # {'name': 'xiaohua', 'age': 19, 'sex': '女', 'class': '19班', 'phone_num': 18656031111}

# 8.清空
dict1.clear()
print(dict1)  # {}

"""
part02：字典其他知识
"""
# 定义字典的几种方式
dict2 = dict(name='xiaoliu', age=35, sex='男')  # 定义字典方式2
print(dict2)  # {'name': 'xiaoliu', 'age': 35, 'sex': '男'}

dict3 = {}  # 定义字典方式3： 定义一个空字典
dict4 = dict()
print(dict3, dict4)

# 字典在存储过程中，如果已经有存在的key，新的值会覆盖已经存在的值
dict2 = dict(name='xiaoliu', age=35, sex='男')  # {'name': 'xiaoliu', 'age': 35, 'sex': '男'}
dict2.update({'age': 36, 'phone_num': 18618835799})
print(dict2)  # {'name': 'xiaoliu', 'age': 36, 'sex': '男', 'phone_num': 18618835799}

# 注意：字典的key值必须是不可变类型(数字、字符串、元组)，value可以是任意类型
dict1 = {1: [1, 2, 3, 4], 2: 18, 3: (2, 222)}
dict2 = {'第一组': ['xiaohua', 'xiaohua1', 'xiaohua2'],
         '第二组': ['xiaohua', 'xiaohua1', 'xiaohua2'],
         '第三组': ['xiaohua', 'xiaohua1', 'xiaohua2'], }
print(dict2['第二组'])  # ['xiaohua', 'xiaohua1', 'xiaohua2']

# 获取所有的key，获取所有的value，获取所有的键值对
dict3 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
ks = list(dict3.keys())  # 获取所有的key，并且转换为列表类型
print(ks)  # ['name', 'age', 'sex']

vs = list(dict3.values())  # 获取所有的value，并且转换为列表类型
print(vs)  # ['xiaohua', 18, '女']

kvs = list(dict3.items())
print(kvs)  # [('name', 'xiaohua'), ('age', 18), ('sex', '女')]

# 求出所有的value，过滤重复，且转换为列表
dict4 = {'name': 'xiaohua', 'age': 19, 'sex': '女', 'class': 19}
print(list(set(dict4.values())))  # [19, '女', 'xiaohua']
