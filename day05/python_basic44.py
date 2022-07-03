"""
-------------------------------------------------
   File Name:python_basic44
   Author:Lee
   date: 2021/5/31-11:08
-------------------------------------------------
"""
"""
冒泡排序
"""

# 数据交换，将a和b的值进行交换
a = 10
b = 20
print('a的值是：', a)
print('b的值是：', b)

# t = a
# a = b
# b = t

a, b = b, a

print('a的值是：', a)
print('b的值是：', b)

# 有一个元素为int类型的列表，[20,16,88,60,14],互换下标0和1位置的元素
list1 = [20, 16, 88, 60, 14]

# temp = list1[0]  # temp = 20
# list1[0] = list1[1]
# list1[1] = temp

list1[0], list1[1] = list1[1], list1[0]

print(list1)

# 使用冒泡排序对列表进行 从小到大的排序 (核心：每循环一次，确定一个位置)
list1 = [20, 16, 88, 60, 14]
# [20, 16, 88, 60, 14]
# 第一次循环  相邻两个值进行比较，一共比较4次，如果前边的值比后边的值大，交换位置
# [16, 20, 88, 60, 14]   [16, 20, 88, 60, 14]   [16, 20, 60, 88, 14]   [16, 20, 60, 14, 88]
# 第二次循环  相邻两个值进行比较，一共比较4次，如果前边的值比后边的值大，交换位置
# [16, 20, 60, 14, 88]   [16, 20, 60, 14, 88]   [16, 20, 14, 60, 88]  [16, 20, 14, 60, 88]
# 第三次循环  相邻两个值进行比较，一共比较4次，如果前边的值比后边的值大，交换位置
# [16, 20, 14, 60, 88]   [16, 14, 20, 60, 88]   [16, 14, 20, 60, 88]  [16, 14, 20, 60, 88]
# 第四次循环  相邻两个值进行比较，一共比较4次，如果前边的值比后边的值大，交换位置
# [14, 16, 20, 60, 88]   [14, 16, 20, 60, 88]   [14, 16, 20, 60, 88]  [14, 16, 20, 60, 88]

for i in range(len(list1) - 1):  # 外循环控制循环的次数
    for j in range(len(list1) - 1 - i):  # 内循环控制元素比较交换的次数
        if list1[j] > list1[j + 1]:  # 判断前边的值比后边的值大
            list1[j], list1[j + 1] = list1[j + 1], list1[j]  # 数据交换
print(list1)