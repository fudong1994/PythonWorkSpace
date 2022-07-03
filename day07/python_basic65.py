"""
-------------------------------------------------
   File Name:python_basic65
   Author:Lee
   date: 2021/6/2-14:08
-------------------------------------------------
"""
"""
错误和异常的区别：
错误:不能通过解释器的编译，这种叫错误
异常:编译通过，运行时出现问题叫异常
"""

# 常见的错误
#  print()  # 缩进错误 IndentationError: unexpected indent
# print(  # 语法错误  SyntaxError

# 常见异常
# print(10/0)  # 除0异常 ZeroDivisionError: division by zero
# print('1' + 1)  # 类型错误 TypeError
list1 = [1, 2, 3, 4]
# print(list1[5])  # 下标越界异常 IndexError: list index out of range

# with open(r'./test1.txt', 'r') as fr:
#     print(fr.read())  # 找不到文件异常   FileNotFoundError

num = input('请输入一个数字：')
print(10 / int(num))
