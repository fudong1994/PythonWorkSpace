"""
-------------------------------------------------
   File Name:python_basic35
   Author:Lee
   date: 2021/5/28-9:42
-------------------------------------------------
"""
"""
while循环：

语法：
while 条件：
    语句块

当条件成立时执行语句块
"""

# 循环案例1：打印1-100
i = 1
while i <= 100:
    print(i)  # 打印i  (动作1)第一循环判断1<=100  打印了1  第二次循环判断2<=100  打印了2
    i += 1  # i = i+1  (动作2) 把i加1 那么i = 1+1   把i+1 那么i= 2+1

# 循环案例2：打印0-100的偶数
i = 0
while i <= 100:
    print(i)  # 0,2,4,6,8,10....100
    i += 2

print('===' * 50)

i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# 打印1-2021年所有的闰年
year = 1

while year <= 2021:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print('{}是闰年'.format(year))
    year += 1

# 求出1-100的偶数的数量
i = 1
count = 0  # 用来累计数量
while i <= 100:
    if i % 2 == 0:
        count += 1
    i += 1
print('1-100的偶数的数量为%d个' % count)

# 求出1-2021年闰年的数量
year = 1
count = 0
while year <= 2021:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        count += 1
    year += 1
print('1-2021年一共有%d个闰年' % count)

# 求出1-10的和
i = 1
sm = 0
while i <= 10:
    sm += i  # 1,3,6,10.....
    i += 1
print('1-10的和是%d' % sm)  # 1-10的和是55

# 求出1-100的偶数的和
i = 1  # 开关
sm = 0
while i <= 100:
    if i % 2 == 0:
        sm += i
    i += 1
print('1-100的偶数和为：%d' % sm)

# 求出1-10的阶乘
i = 1
sm = 1
while i <= 10:
    sm = sm * i
    i = i + 1
print('1-10的阶乘结果为：%d' % sm)
