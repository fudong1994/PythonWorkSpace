"""
-------------------------------------------------
   File Name:python_basic31
   Author:Lee
   date: 2021/5/27-14:03
-------------------------------------------------
"""
"""
本章讲解：条件判断
"""

"""
条件判断分为单分支语句、双分支和多分支语句

单分支语句语法：
if 条件：
    语句块

如果条件成立则执行语句块、反之则不执行语句块
"""

# case1:如果今天天气好，我就晒被子
tianqi = input('请输入天气：')

if tianqi == '好':
    print('可以晒被子了')
    print('好开心')

# case2:如果今天是周五，明天就不用上课了
date = input('请输入今天是星期几：')

if date == '星期五' or date == '五' or date == '5' or date == '周五':
    print('明天就不用上课了！')
    print('和对象约会去')

# case2优化：
date = input('请输入今天是星期几：')

if date in ['星期五', '五', '5', '周五', 'friday', 'Friday']:
    print('明天就不用上课了！')
    print('和对象约会去')

# 模拟Oracle登录
name = input('请输入用户名：')
password = input('请输入密码：')

if name == 'scott' and password == '123456':
    print('恭喜您登录成功~')
else:
    print('用户名或密码错误，请检查您的输入是否正确')

"""
双分支语句语法：
if 条件：
    语句块1
else:
    语句块2

如果条件成立执行语句块1，其他情况执行语句块2
"""
# case1：如果天气好，晒被子。天气不好 睡觉
tianqi = input('请输入天气：')

if tianqi == '好':
    print('晒被子')
else:
    print('睡觉')

# case2:如果今天是周五或周六，明天不用上课，其他时间正常上课
date = input('请输入星期几：')

if date in ('周五', '周六'): # True False
    print('明天不用上课')
else:
    print('正常上课')

# 练习： 用户从控制台输入一个整数，判断他是奇数还是偶数？
num = int(input('请输入一个整数：'))

if num % 2:  # 只要是整数取余2 只有2个结果，要么是1 要么是0   非0即真，所以余1时为True，执行if的语句块，反之为False执行else语句块
    print('%d是奇数' % num)
else:
    print('{}是偶数'.format(num))

