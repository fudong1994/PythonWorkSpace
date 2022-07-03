"""
-------------------------------------------------
   File Name:python_basic41
   Author:Lee
   date: 2021/5/28-14:02
-------------------------------------------------
"""

"""
for循环
for 变量 in 可迭代数据(str/list/tuple/range()):
    循环体
"""
# 知识点1： range函数
for i in range(0, 5):  # 每循环一次，把0-4数字赋值给i
    print(i)  # 打印出 [0-5)

for i in range(2, 9):  # 2,3,4,5,6,7,8
    print(i)

for i in range(1, 10, 2):  # 产生1-10的奇数，2表示步长
    print(i)

# 打印1-2021年有多个闰年
count = 0
for i in range(1, 2022):
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
        count += 1
print('1-2021年间一共有{}个闰年'.format(count))

# range()：通常是配合for循环使用，生成一个指定范围内的整数队列，每次给for循环的变量重新赋值(自增或自减)

# 打印1-100的奇数和
sm = 0
for i in range(1, 101):
    if i % 2 == 1:
        sm += i
print('1-100的奇数和为:%d' % sm)

sm1 = 0
for i in range(1, 101, 2):
    sm1 += i
print('1-100的奇数和为:%d' % sm1)
