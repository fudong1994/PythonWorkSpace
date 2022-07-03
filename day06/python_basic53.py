"""
-------------------------------------------------
   File Name:python_basic53
   Author:Lee
   date: 2021/5/31-15:44
-------------------------------------------------
"""
"""
函数的参数定义：
1、必须参数(位置参数)  2、默认参数  3、不定长参数(可变参数) 4、关键字参数
"""


# 1、必须参数(位置参数)：入参按照位置传递，在调用时入参的元素个数必须相同
def fun1(a, b, c):
    return a + b + c


res = fun1(1, 2, 3)
res2 = fun1(b=2, c=5, a=3)  # 把2赋值给fun1函数中的b，把5赋值给fun1函数中的c，把3赋值给fun1函数中的a
print(res2)


# 2、默认参数：我们可以在声明方法的时候给入参设置默认值

def fun2(a, b=10):  # 这里a是必须参数，b是默认参数，默认值为10 # 如果传入1个参数，那么b使用默认值，如果传入2个参数，b会使用参数值
    return a + b


res3 = fun2(1)  # 把1赋值给a  b使用默认值
print(res3)  # 11

res4 = fun2(20, 50)  # 代表把20给a 把50给b  b不使用默认值
print(res4)  # 70


# 3、不定长参数(可变参数):可以保存0-N个入参，一般使用*args，调用该方法时如果传入多个入参，会自动组包成一个元组

def fun3(*args):
    print('入参为:', args)


fun3(1, 2)  # 入参为: (1, 2)
fun3(5)  # 入参为: (5,)
fun3()  # 入参为: ()
fun3(1, 2, 3, 4, 5, 6, 7, 8, 8)  # 入参为: (1, 2, 3, 4, 5, 6, 7, 8, 8)


# 使用不定长参数声明一个函数，并且调用该函数：传入多个值，能够求出这些值的和

def fun4(*args):  # 接收多个参数并且打包成元组
    return sum(args)  # 求元组的和


print(fun4(1))  # 1
print(fun4(1, 2))  # 3
print(fun4(10, 230, 500))  # 740
print(fun4())  # 0


def fun5(a, *args):
    return sum(args) + a


print(fun5(10, 30))  # 40
print(fun4(10, 230, 500, 700))  # 1440


# 4、关键字参数:用来接收 key-value格式的入参，保存为一个字典

def fun6(**kwargs):  # 两颗星代表把传入的多个键值对打包成一个字典
    print(kwargs)


fun6(a=1, b=2, c=3)  # 调用该方法后 打印出一个字典 {'a': 1, 'b': 2, 'c': 3}
fun6(name='xiaohua', age=18, sex='女')  # {'name': 'xiaohua', 'age': 18, 'sex': '女'}


# 例：使用关键字参数声明一个函数，并且调用该函数：传入多个值，能够求出这些值的和
def fun7(**kwargs):  # 将key-value格式的入参打包成一个字典
    return sum(list(kwargs.values()))  # 获取字典所有的value值，并且转换为列表，再通过sum()求出列表的和


res5 = fun7(a=10, b=20, c=30)
print(res5)  # 60


# 多种参数类型混合使用1
def test(x, y=5, *args, **kwargs):
    print('x的值为{},y的值为{},args的值{},kwargs的值为{}'.format(x, y, args, kwargs))


test(1)  # x的值为1,y的值为5,args的值(),kwargs的值为{}
test(1, 2)  # x的值为1,y的值为2,args的值(),kwargs的值为{}
test(1, 2, 3)  # x的值为1,y的值为2,args的值(3,),kwargs的值为{}
test(1, 2, 3, 4)  # x的值为1,y的值为2,args的值(3, 4),kwargs的值为{}
test(1, 2, 3, 4, a=5, b=6)  # x的值为1,y的值为2,args的值(3, 4),kwargs的值为{'a': 5, 'b': 6}


# 多种参数类型混合使用2
def test2(*args, **kwargs):
    print('args的值是{},kwargs的值是{}'.format(args, kwargs))


test2()  # args的值是(),kwargs的值是{}
test2(1, 2, 3)  # args的值是(1, 2, 3),kwargs的值是{}
test2(a=1, b=2, c=3)  # args的值是(),kwargs的值是{'a': 1, 'b': 2, 'c': 3}
test2(1, 2, 3, a=4, b=5, c=6)  # args的值是(1, 2, 3),kwargs的值是{'a': 4, 'b': 5, 'c': 6}
