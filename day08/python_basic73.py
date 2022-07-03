"""
-------------------------------------------------
   File Name:python
   Author:Lee
   date: 2021/6/2-16:45
-------------------------------------------------
"""
"""
知识点:类属性分为：类属性和实例属性
        1.类属性声明在类体中，类属性是每个对象共同享有的属性。类属性可以通过 类名.属性名直接访问
        2.实例属性,在创建对象之后声明的属性，该属性是某个对象独有的属性，只能通过对象去调用
"""


class Emp:
    emp_no = ''  # 类属性
    emp_name = ''
    emp_sal = 0
    __emp_age = 0  # 如果属性前有__,代表私有属性，只能在该类中使用

    # 计算年薪
    def year_sal(self):
        return self.emp_sal * 12

    # 计算请假天数的扣款
    def fine(self, day):
        return self.emp_sal / 22 * day

    print(__emp_age)  # 私有属性只能在类的内部访问


Emp.emp_sal = 2480  # 类属性可以通过类名.属性名直接访问，我们可以在类的外面修改类属性的值

emp01 = Emp()
print(emp01.emp_sal)  # 2480
print(emp01.year_sal())  # 29760

emp02 = Emp()
print(emp02.emp_sal)  # 2480

emp03 = Emp()
emp03.comm = 2000  # comm为实例属性，属于emp03的对象独有的属性，只能通过emp03调用
print(emp03.comm)  # 2000

emp01.emp_sal = 3000
print(emp01.emp_sal)  # 3000  # 此处的emp01对象的emp_sal是实例属性

print(emp02.emp_sal)  # 2480
print(Emp.emp_sal)  # 2480
