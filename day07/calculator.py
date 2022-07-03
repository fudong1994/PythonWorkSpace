"""
-------------------------------------------------
   File Name:calculator
   Author:Lee
   date: 2021/6/1-16:33
-------------------------------------------------
"""
# 定义一个全局变量
name = 'xiaohua'


# 加法
def add(x, y):
    return x + y


# 减法
def minus(x, y):
    return x - y


# 乘法
def mul(x, y):
    return x * y


# 除法
def division(x, y):
    return x / y


# print(__name__)

if __name__ == "__main__":  # 判断是否在当前模块下运行(__name__在当前模块下的值为:__main__，在其他模块下值为：day07.calculator)
    print(__name__)
    print(__file__)
    print(__doc__)

