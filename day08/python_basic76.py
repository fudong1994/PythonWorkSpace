"""
-------------------------------------------------
   File Name:python_basic76
   Author:Lee
   date: 2021/6/3-11:40
-------------------------------------------------
"""
"""
魔法方法:
python中的魔法方法：就是可以给你的类添加魔力的特殊方法
如果你实现了这些方法中的某一个，那么这个方法就会在特殊的情况下被python调用
你可以定义自己想要的行为，这一切都是自动发生的，他们经常是两个下划线包围来命名
比如： __init__ / __new__ / __del__ / __len__ / __eq__ 等等，魔法方法的功能是很强大的

简单的说就是你重写魔法方法后，在进行某些操作时，会自动调用这些方法
魔法方法十分强大，使用时需要十分谨慎
"""


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2480

    # def __init__(self):  # 在创建Emp类的实例对象时，python会自动调用Emp类中的__init__函数,我们重写了以后，会自动完成我们预期的操作
    #     print('构造函数，在创建对象时调用')

    def __init__(self, emp_no, emp_name, emp_sal):  # 在创建Emp类的实例对象时，python会自动调用Emp类中的__init__函数
        self.emp_no = emp_no  # 重写了__init__方法，要求在创建实例对象时传入3个参数，并且给绑定的实例对象的3个实例属性赋值
        self.emp_name = emp_name
        self.emp_sal = emp_sal
        print('创建对象时按要求传参数')


emp01 = Emp(1001, 'scott', 2480)  # 在创建实例对象时调用__init__方法


class T1:
    def __del__(self):  # 重写了T1类的__del__()方法，在销毁实例对象时会触发调用，打印'该对象被销毁'
        print('该对象被销毁')


# __del__() 触发条件：
# 1. 手动使用del 函数功能时会调用当前类的__del__()
# 2. python的垃圾回收机制会触发__del__()函数 相当于我们手动del每一个变量和方法或对象

t2 = T1()
del t2  # 该对象被销毁

str1 = '12345'
print(len(str1))  # 5
print(str1.__len__())  # 5


class T3(object):
    def __len__(self):  # 重写了T3类的__len__方法，当调用len(t4) / __len_() 触发返回50
        return 50

    def __eq__(self, other):
        return True


t4 = T3()
print(len(t4))  # 50

t5 = T3()
print(t4 == t5)


# 在python中怎么判断两个对象相等？


# 反射
class Emp1:
    emp_name = ''
    emp_sal = 2480

    def add(self, a, b):
        print(a + b)


emp02 = Emp1()
emp02.emp_name = 'xiaohua'
emp02.emp_sal = 5000

emp02.emp_comm = 2000  # 为emp02创建实例属性，该属性是emp02独有的属性
print(emp02.emp_comm)  # 2000

# 利用反射动态设置属性，只有在代码运行时，才给emp02对象设置属性
setattr(emp02, 'emp_no', 1001)  # setattr(对象名称，属性名，属性值)
print(emp02.emp_no)  # 1001

# 利用反射动态获取属性， getattr(对象名，属性名)
print(getattr(emp02, 'emp_comm'))  # 2000
print(getattr(emp02, 'emp_name'))  # xiaohua  # 获取返回该实例对象已存在属性值
print(getattr(emp02, 'emp_no'))  # 1001

# 利用反射动态删除属性 delattr(对象名，属性名)
delattr(emp02, 'emp_no')
# print(emp02.emp_no)  # AttributeError: 'Emp1' object has no attribute 'emp_no'
