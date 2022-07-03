"""
-------------------------------------------------
   File Name:python_basic66
   Author:Lee
   date: 2021/6/2-14:17
-------------------------------------------------
"""
"""
异常的处理

try:
    语句块1
except 异常类型1:
    语句块2
except 异常类型2:
    语句块3
....
[else]：else为可选内容，如果没有异常，则执行else中的内容
[finally]：finally为可选内容，不管有没有异常，都必须执行、

执行try中的语句块1，如果语句块1出现了异常类型1则执行语句块2
"""

num = input('请输入整数类型的数字：')
try:
    if int(num) % 2 == 0:
        print('是偶数')
    else:
        print('是奇数')
except ValueError:  # 如果try中的代码出现了 ValueError，则执行except下的代码
    print('请输入正确的整数！')
else:
    print('没有出现异常')  # 如果try中的代码没有出现异常，则执行else中的内容
finally:
    print('执行完成！')

"""分别处理多种异常"""

try:
    num = input('请输入一个数字：')
    print(10 / int(num))
except ZeroDivisionError: # 处理 除数为0的异常
    print('除数不能为0！')
except ValueError:  # 处理 非整数情况
    print('请输入正确的数据！')

"""同时处理多种异常"""

try:
    num = input('请输入一个数字：')
    print(10 / int(num))
except (ZeroDivisionError, ValueError):  # 处理非整数、除数为0 的情况
    print('请输入正确的数据！')

""" 万能处理异常方式 """

try:
    num = input('请输入一个数字：')
    print(10 / int(num))
except Exception as e:  # 如果出现异常，就执行except下的代码
    print('请输入正确的数据！', e)  # e代表报错信息
