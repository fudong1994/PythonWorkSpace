"""
-------------------------------------------------
   File Name:python_basic34
   Author:Lee
   date: 2021/5/27-17:43
-------------------------------------------------
"""

# 练习1：用户输入一个年份，判断是否为闰年？    (能被4整除但不能被100整除，或者能被400整除)
year = int(input('请输入一个年份：'))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('{}是闰年'.format(year))
else:
    print('{}不是闰年'.format(year))

# 练习2：用户输入三个边，判断是否构成三角形  (三条边必须满足： 三角形任意两边之和大于第三边，任意两边之差小于第三边)
a = int(input('请输入第一条边：'))
b = int(input('请输入第二条边：'))
c = int(input('请输入第三条边：'))

if a <= 0 or b <= 0 or c <= 0:
    print('请输入正确的边长')
else:
    if a + b > c and a + c > b and b + c > a:
        print('构成三角形')
    else:
        print('不构成三角形')
