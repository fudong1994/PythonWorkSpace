"""
-------------------------------------------------
   File Name:python_basic03
   Author:Lee
   date: 2021/5/24-15:55
-------------------------------------------------
"""

"""
本章讲解：注释、命名规则、保留字、行与缩进
"""

# 注释1：注释单行
# 注释2

'''
注释多行
第三个注释
第四个注释
'''

"""
注释多行
第五个注释
第六个注释
print('hello world')
"""

# 多行注释快捷键，选中需要注释的文本，然后 Ctrl+/

# 鹅鹅鹅，曲项向天歌。
# 白毛浮绿水，红掌拨清波。


# 命名规则
'''
666 = 'a'  # 不能以数字开头
and = 123  # and是保留字，不能当作变量名
money&ss = 123  # 除了下划线，不推荐你使用其它的符号作为变量名
'''


# 查看python的保留字
import keyword

print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
 '''

# 行与缩进
print(1)
# print(1) #该行报错

