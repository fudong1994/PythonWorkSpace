"""
-------------------------------------------------
   File Name:python_basic12
   Author:Lee
   date: 2021/5/25-14:09
-------------------------------------------------
"""

"""
本章讲解：运算符
"""

# 知识1：算术运算符  + - * /   %(取余)  //(取整):向下取整  **(幂等)
print(10 + 20)
print(10 - 20)
print(10 * 20)
print(10 / 20)  # 0.5
print(20 / 10)  # 2.0  除法运算会返回一个浮点数

print(1 % 2)  # 1
print(2 % 3)  # 2
print(10 % 20)  # 10
print(6 % 3)  # 0
print(10 % 3)  # 1
print(20 % 6)  # 2
# 小数对大数取余，余小的
# 所有奇数对2取余都是1  所有的偶数对2取余都是0

print(2 ** 3)  # 8

print(10 // 20)  # 0
print(25 // 2)  # 12
print(-25 // 2)  # -13

# 知识点2： 赋值运算符  =  +=  -=  *=   /=  **=  %=  //=
a = 10
a += 1  # 相当于 a = a+1
print(a)  # 11

a -= 1  # 相当于 a = a-1
print(a)  # 10

a *= 2  # 相当于 a = a*2
print(a)  # 20

a /= 4  # 相当于 a = a /4
print(a)  # 5.0

a = 5
a //= 2  # 相当于 a = a // 2
print(a)  # 2

a %= 2  # 相当于 a = a%2
print(a)  # 0

# 知识点3： 比较运算符   >    <    >=   <=    !=(不等于)   ==(相等)  结果只能是 True或False
a = 20
b = 10
print(a == b)  # False
print(a < b)  # False
print(a > b)  # True

# 知识点4：逻辑运算符  and(全真为真)    or(全假为假)  not(取反)
# and(全真为真)  (条件A and 条件B) 当两个条件同时成立，结果为成立(True)
# or(全假为假)  (条件A or 条件B) 当两个条件都不成立时，结果为不成立(False)
print(a > 0 and b > 0)  # True
print(a < 0 and b > 0)  # False
print(a < 0 or b < 0)  # False
print(a < 0 or b > 0)  # True

a = 10
b = 20
print(a < 0 or (a < 0 or b < 0))  # False
print(a < 0 or (b > 0 or (a < 0 or b < 0)))  # True

print(not (a < 0 and (b < 0 or (a > 0 or b > 0))))  # True
print(not (1 > 0))  # False

# 知识点5：成员运算符   in(在指定序列寻找指定值，找到返回True、否则返回False)
# not in(在指定序列寻找指定值，找不到返回True、否则返回False)
str1 = 'xiaohua'
print('x' in str1)  # True
print('x' not in str1)  # False

"""
查看储存地址函数   id()
"""
int01 = 5
print(id(int01))
int02 = 123456789111
print(id(int02))

a = 5000000000000
b = 5000000000000
print('a的物理地址是：', id(a), 'b的物理地址是：', id(b))

name = 'xiaohua'
name1 = 'xiaohua'
print('name的物理地址是：', id(name), 'name1的物理地址是：', id(name1))

# 身份运算符   is(判断两个标识符是同一对象，直接比对物理地址)
# is not (判断两个标识符不是同一对象，直接比对物理地址)
a = 100
b = 100
print(id(a), '******', id(b))
print(a is b)  # True

b = 30
print(id(a), '******', id(b))
print(a is b)  # False
print(a is not b)  # True

# is 和  ==  的区别是什么？
# is 是判断变量的物理存储地址是否相等     == 用来判断变量的值是否相等
