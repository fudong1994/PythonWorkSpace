"""
-------------------------------------------------
   File Name:python_basic61
   Author:Lee
   date: 2021/6/1-16:42
-------------------------------------------------
"""

import day07.calculator as cal

"""
模块导入：当前模块导入其他模块的内容，我们就可以使用该模块的变量或函数

模块导入方式1： 
导入整个模块格式: import 包名.模块名 as 别名 (推荐使用) 
"""

print(cal.name)  # xiaohua  访问calculator模块下的name变量
print(cal.add(2, 3))  # 5  访问calculator模块下的add函数
print(cal.division(10, 4))  # 2.5

print(cal.__name__)  # day07.calculator
print(__name__)  # __main__
