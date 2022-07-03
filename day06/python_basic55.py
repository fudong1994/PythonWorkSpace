"""
-------------------------------------------------
   File Name:python_basic55
   Author:Lee
   date: 2021/6/1-14:11
-------------------------------------------------
"""
"""
函数传递值的方式：值传递、引用传递

值传递：传递的是变量的值而非变量本身，被传递的变量的值不会被改变
引用传递：传递的是变量本身，被传递的变量的值会被改变

注意：
1、可变类型(list/dict/set为可变类型)用的是 引用传递
2、不可变类型(number/str/tuple)用的是 值传递
"""


def fun1(a):
    a += 1
    print(a)  # 11


a = 10
fun1(a)  # 值传递 调用fun1方法 并且把a的值10  传送给fun1的a
print(a)  # 10


def fun2(lst):
    lst.append(5)
    print(lst)  # [1,2,3,4,5]


list1 = [1, 2, 3, 4]
fun2(list1)  # 引用传递  传递的是list1变量本身
print(list1)  # [1,2,3,4,5]

"""
使用lambda 能够实现简单的函数
语法： lambda[arg1,arg2....]:函数体
"""


def fun3(a, b):
    return a % b


print(fun3(1, 2))  # 1

# 使用lambda 定义上面的函数

fun4 = lambda a, b: a % b  # 入参是 a 、 b    函数体是a%b
print(fun4(2, 2))  # 0


# 写一个函数判断是否为偶数

def fun5(num):
    if num % 2 == 0:
        print('是偶数')


fun6 = lambda num: num % 2 == 0  # 入参是num 函数体为 num%2==0

print(fun6(1))  # False
