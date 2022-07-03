"""
-------------------------------------------------
   File Name:python_basic87
   Author:Lee
   date: 2021/6/4-10:29
-------------------------------------------------
"""
"""
封装：
第一层面的封装：把属性和方法组合成一个类，就是简单的封装
第二层面的封装：类中把某些属性和方法隐藏起来(或者说定义为私有的),只能在类的内部使用、外部无法访问，或者留下少量的函数供外部访问
"""

# 小花 这个学生
name = '小花'
sex = '女'
age = 20


# 这种方式用三个变量去形容小花这个同学，这有什么弊端？
# 弊端：太零散，如果学生太多，需要不断的新建变量去描述

class Student(object):
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


one = Student('老刘', '男', 36)
two = Student('徐迟', '男', 28)
three = Student('小王', '男', 30)

print("姓名：{},性别:{},年龄：{}".format(two.name, two.sex, two.age))  # 姓名：徐迟,性别:男,年龄：28


# 第二层的封装：控制访问的权限
# 我们可以把所有的属性私有，不在允许对象访问

class Stu(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age


four = Stu('小花', '女', 20)


# print(four.name)  # 该行代码报错，AttributeError: 'Stu' object has no attribute '__name'

# 问题来了：现在我们把name、age、sex设置为私有属性，但是我又想他们通过我指定接口(方法)去访问或修改我的属性，该怎么办？

class Stu1(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


# 这样有效的控制了访问、修改的权限，只有name和age属性允许访问和修改，而sex不可以
five = Stu1('小李', '猛男', 26)
print(five.get_name(), five.get_age())  # 小李 26
five.set_name('Lee')
five.set_age(25)
print(five.get_name(), five.get_age())  # Lee 25


# 上面的写法太麻烦，我们可以使用装饰器：property (是属性，表示可以通过类实例直接访问)  和 setter (代表设置属性的值)
class Stu2(object):
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


six = Stu2('尊龙', '男', 26)
six.name = '焦恩俊'
six.age = 30
print("姓名：{},年龄：{}".format(six.name, six.age))  # 姓名：焦恩俊,年龄：30


# 把一个类的函数直接定义成属性，实例对象在使用时候可以通过 object.name 调用，根本无法擦觉自己的name是执行了一个函数
# 这种特性的使用方式遵循了统一访问控制权限的原则、增强了安全性

class Room(object):
    def __init__(self, length, width, high):
        self.length = length
        self.width = width
        self.high = high

    @property
    def area(self):
        return self.length * self.width

    @property
    def vm(self):
        return self.length * self.width * self.high


r1 = Room(10, 6, 3)
# print(r1.area()) # 60 以前的调用方法

print('r1房间的面积:', r1.area)  # 可以像访问属性一样去访问area方法，这其实会触发area函数的执行，动态计算出一个值
print('r1房间的体积:', r1.vm)  # r1房间的体积: 180





