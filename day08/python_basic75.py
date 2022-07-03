"""
-------------------------------------------------
   File Name:python_basic75
   Author:Lee
   date: 2021/6/3-11:16
-------------------------------------------------
"""
"""
构造方法：  方法名为： __init__ 会在创建类的时候自动执行，利用该特性，我们可以在创建实例对象的同时做一些操作

一般写一个类，如果不声明__init__时会自动使用默认的，默认构造方法一般不显示，如果声明了 __init__方法，会覆盖默认的
注意：不能同时有两个__init__方法
"""


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2480

    # 计算年薪
    def year_sal(self):  # 实例方法特点：必须要第一个参数默认self，绑定调用方法的实例对象
        return self.emp_sal * 12

    # def __init__(self):  # 在创建Emp类的实例对象时，python会自动调用Emp类中的__init__函数,我们重写了以后，会自动完成我们预期的操作
    #     print('构造函数，在创建对象时调用')

    def __init__(self, emp_no, emp_name, emp_sal):  # 在创建Emp类的实例对象时，python会自动调用Emp类中的__init__函数
        self.emp_no = emp_no  # 重写了__init__方法，要求在创建实例对象时传入3个参数，并且给绑定的实例对象的3个实例属性赋值
        self.emp_name = emp_name
        self.emp_sal = emp_sal
        print('创建对象时按要求传参数')


# print(dir(Emp))  # 打印Emp类中所有的属性和方法
# print(dir(str))  # 打印str类中所有的属性和方法
# emp01 = Emp()  # 创建一个实例对象      没有重写__init__方法时，使用默认的__init__

emp02 = Emp(1001, 'scott', 2480)  # 当__init__方法被重写时，必须要按照重写后的要求传参数才能创建对象
# 创建对象的时，自动调用了__init__方法，并且为属性赋值

print(emp02.emp_no, emp02.emp_name, emp02.emp_sal)  # 1001 scott 2480
