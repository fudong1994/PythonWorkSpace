"""
-------------------------------------------------
   File Name:python_basic62
   Author:Lee
   date: 2021/6/1-17:02
-------------------------------------------------
"""
from day07.calculator import name, add, division
"""
模块导入方式2： 导入某个模块下的部分内容 (不推荐该方法，如果倒入多个文件可能存在相同的方法名的情况，造成意想不到的bug)
格式： from 包名.模块名 import 函数名1，函数名2，变量......
"""

print(name)  # xiaohua
print(add(20, 30))  # 50
print(division(99, 30))  # 3.3
