"""
-------------------------------------------------
   File Name:constants
   Author:Lee
   date: 2021/6/17-16:20
-------------------------------------------------
"""
import os
"""
使用常量对路径进行管理
好处：代码使用非绝对路径，可移植性更高
"""

path = os.path.dirname(__file__)  # 获取当前文件的目录
print(path)

path = os.path.dirname(os.path.dirname(__file__))  # 获取当前文件目录的 父级目录
print(path)
