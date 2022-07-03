"""
-------------------------------------------------
   File Name:python_basic56
   Author:Lee
   date: 2021/6/1-14:41
-------------------------------------------------
"""
"""
内置函数：python自带的函数
"""
# 常用的内置函数： range/len/input/print/id/type/sum/max/min/sort....
# 高级内置函数

# 1、eval()：能够识别字符串中的表达式，并且进行运算

print('1+1')  # 1+1
print(eval('1+1'))  # 2   eval()将字符串中的表达式识别为1+1，并且进行运算
eval('print("hello world")')  # hello world

num1 = input('请输入一个整数：')
num2 = input('请输入一个数字：')
print(eval(num1) + eval(num2))  # 识别字符串中的数字

# 输入一个列表,求出列表的和
list1 = input('请输入列表：')  # [1,2,3,34,5]
print(sum(eval(list1)))  # 45

# 2、exec() 可以识别相对复杂的表达式  eval()只能识别简单的表达式
# 有返回值时用eval() 没返回值时用exec()

str_fun = """
def fun1():
    print('hello')
"""

# eval(str_fun) # 该行代码报错，eval()只能识别相对简单的表达式
exec(str_fun)  # exec()函数识别字符串的时候 识别到fun1()函数
fun1()  # hello

# 3、filter()  自定义过滤，filter用来过滤序列，过滤掉不合符条件的元素，返回符合条件的元素
list2 = [10, 20, 30, 50, 70, 100, 80]


# 使用filter 过滤出list2中大于30的数据
# 第一步：写一个过滤条件
def fun2(x):
    return x > 30


# filter() 需要传2个参数，第一个参数是函数名，第二个参数是序列对象
# 把后面可迭代的序列中每一个元素传给前面的函数，返回True或False，并且把返回为True的元素放到一个迭代器里(最好转成列表使用)

# 第二步：使用filter过滤
res = filter(fun2, list2)
print(list(res))

# filter同如下逻辑：
list2 = [10, 20, 30, 50, 70, 100, 80]
list3 = list()
for i in list2:
    if i > 30:
        list3.append(i)
print(list3)

# 使用filter() 过滤出元组中的偶数
tup1 = (1, 2, 3, 4, 5, 6, 76, 78, 2, 3, 32, 22, 88)


def fun3(x):
    return x % 2 == 0


print(tuple(filter(fun3, tup1)))  # 使用fun3()的规则过滤tup1，把过滤后的结果转换为元组

# map(): 把后面可迭代的序列中每一个元素传给前面的函数，将结果放到一个迭代器中，放的是结果
res = map(fun3, tup1)  # map() 会把tup1的每一个元素放入fun3函数中运行，把运行结果放到迭代器中(最好转成列表使用)
print(tuple(res))  # (False, True, False, True, False, True, True, True, True, False, True, True, True)

# 5、zip():聚合打包  当需要打包的对象长度不统一时，按最短的来
list1 = ['name', 'age', 'sex', 'class']
list2 = ['xiaohua', 18, '女', 19, 50]

res = dict(zip(list1, list2))  # 把list1和list2组装然后转换为字典
print(res)  # {'name': 'xiaohua', 'age': 18, 'sex': '女', 'class': 19}


# 底层逻辑
dt = {}
for i in range(len(list1)):
    dt[list1[i]] = list2[i]
print(dt)

# 6、 isinstance()  判断数据类型
num = 1000
print(isinstance(num, int))  # True  判断num是否属于int类型

str1 = 'abc'
print(isinstance(str1, int))  # False
print(isinstance(str1, str))  # True

# 判断一个字符串中是否为纯数字
str2 = '123456789aaa'

is_true = '是纯数字'

for i in str2:
    if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        is_true = '不是纯数字'
        break

print(is_true)