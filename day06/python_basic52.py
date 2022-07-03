"""
-------------------------------------------------
   File Name:python_basic52
   Author:Lee
   date: 2021/5/31-14:25
-------------------------------------------------
"""
"""
函数：函数是可以重复使用的一段代码  比如：print()、id()、type()、input()....
函数的定义规则：
def 函数名([参数1,参数2,参数3....]):
    函数体(用来写具体的功能)
    [return] 代表结束该函数并且返回数据
"""
# 设计sort()  函数
list1 = [20, 16, 88, 60, 14]


def sort1(reverse=False):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1 - i):
            if reverse:
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
            else:
                if list1[j] < list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)


def add1():  # 声明一个函数 名称为 add1,没有入参,没有返回
    print('该函数被调用')


add1()  # 根据函数名调用add1函数


def add2(a, b):  # 声明一个函数 名称为 add2,需要2个入参,没有返回，调用该函数时必须要传入2个参数
    print(a + b)


add2(10, 20)  # 30  调用add2函数并且传入2个参数
add2(5554444, 9999888)  # 15554332  函数可以多次调用


def add3(a, b, c):  # 声明一个函数 名称为 add3,需要3个入参,调用该函数时必须要传入3个参数
    return a + b + c  # return 代表结束该函数，并且返回a+b+c的值


print(add3(1, 2, 3))  # 6
res = add3(10, 30, 50)
print(res)  # 90


# 设计一个函数，有两个入参，该函数可以返回矩形的面积，并且调用该函数三次
def area(length, width):
    return length * width


res = area(5, 3)
print(res)

res1 = area(10, 8)
print(res1)

res2 = area(3, 2)
print(res2)


# 声明一个函数,判断是奇数还是偶数，并返回判断结果
def judge(num):
    if num % 2:
        return '%d是奇数' % num
    else:
        return '%d是偶数' % num


res = judge(3)
print(res)  # 3是奇数


# 声明一个函数 需要传入一个保存多个人的成绩的元组，该函数返回元组中所有成绩的和
def sum_score(tup1):
    return sum(tup1)


tup1 = (80, 90, 60, 55, 70)
res = sum_score(tup1)
print(res)  # 355


# 求立方体体积 / 判断是否为闰年

# 函数返回多个值
def math(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c, d, e, f  # 如果返回多个之，会自动把多个返回值打包成一个元组返回


res = math(10, 20)
print(res)  # (30, -10, 200, 0.5)

add1, sub1, mul1, division = math(1, 2)  # 自动拆包
print(add1, sub1, mul1, division)  # 3 -1 2 0.5


# 设计一个函数，返回班级的总成绩、平均成绩、最大成绩、最小成绩
def class_score(lst):
    return sum(lst), sum(lst) / len(lst), max(lst), min(lst)


zgcj, pjcj, zdcj, zxcj = class_score([50, 60, 70, 80, 90])
print(zgcj, pjcj, zdcj, zxcj)  # 350 70.0 90 50


# 设计一个函数，返回班级的总成绩、平均成绩、最大成绩、最小成绩,以字典形式返回
def class_score_dict(lst):
    return {'总成绩': sum(lst), '平均成绩': sum(lst) / len(lst), '最高成绩': max(lst), '最小成绩': min(lst)}


res = class_score_dict([100, 80, 90, 30, 50])
print(res)
