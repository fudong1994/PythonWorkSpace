"""
-------------------------------------------------
   File Name:python_basic74
   Author:Lee
   date: 2021/6/2-17:06
-------------------------------------------------
"""
"""
实例方法：最少需要包含一个self参数,用来绑定调用此方法的实例对象
类方法：用修饰器 @classmethod 来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以cls 作为第一个参数，可以通过类本身和实例对象去访问
静态方法：用修饰器 @staticmethod 来标识其为静态方法，静态方法没有self、cls这样的特殊参数，静态方法无法调用任何类属性和类方法
魔法方法
"""
import time


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 2480
    __emp_age = 0  # 如果属性前有__,代表私有属性，只能在该类中使用

    # 计算年薪
    def year_sal(self):  # 实例方法特点：必须要第一个参数默认self，绑定调用方法的实例对象
        return self.emp_sal * 12

    # 计算请假天数的扣款
    @classmethod
    def fine(cls, day):  # 类方法，第一个参数代表类本身
        return cls.emp_sal / 22 * day

    @staticmethod
    def showtime():  # 静态方法，没又self、cls这样的特殊参数。无法使用类的属性和方法
        # print(emp_no)  会报错，静态方法无法使用类的属性和方法
        return time.strftime('%H:%M:%S', time.localtime())


# 实例方法：不能使用 类名.方法名直接调用(必须通过实例对象调用)
# res = Emp.year_sal()  会报错 TypeError: year_sal() missing 1 required positional argument: 'self'

emp01 = Emp()
res = emp01.year_sal()  # 用实例对象去调用，会默认绑定调用的实例对象
print(res)  # 29760


# 类方法：推荐使用 类名.方法名 直接调用
sal1 = Emp.fine(22)
print(sal1)  # 2480.0

emp02 = Emp()
emp02.emp_sal = 300
print(emp02.fine(22))  # 2480.0  还是Emp类本身的emp_sal变量的值 2480

Emp.emp_sal = 5000
print(emp02.fine(22))  # 5000.0  还是Emp类本身的emp_sal变量的值 5000

# 静态方法： 推荐使用 类名.方法名 直接调用
print(Emp.showtime())  # 17:25:11

emp03 = Emp()
print(emp03.showtime())  # 17:25:47  也可以通过实例对象调用，但不推荐
