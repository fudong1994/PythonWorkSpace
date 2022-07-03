"""
-------------------------------------------------
   File Name:python_basic84
   Author:Lee
   date: 2021/6/3-16:42
-------------------------------------------------
"""
"""
1、父类如果有__init__方法，子类创建对象时，必须调用父类的__init__方法
2、父类如果有__init__方法,子类也有__init__方法，这时候子类的__init__方法中，必须调用父类的__init__方法
    格式 父类类名.__init__(入参1，入参2....)  例如：Animal.__init__(self,country,name,age)
"""


class Animal:

    def __init__(self, country, name, age):  # __init__创建对象时被调用，也叫构造方法
        self.country = country
        self.name = name
        self.age = age

    def walk(self):
        print('父类的walk方法' % self.name)

    def say(self):
        print('%s正在咆哮' % self.name)


class Dog(Animal):  # Dog类继承了Animal类
    def walk(self):
        print('子类的walk方法')


d1 = Dog('中国', '大黄', 1)  # 创建子类的对象，调用父类的__init__方法
print(d1.country, d1.name, d1.age)  # 中国 大黄 1


# 如果父类中有__init__方法，子类也有__init__方法，这时候子类的__init__方法中，必须调用父类的__init__方法
class Cat(Animal):
    def __init__(self, color, country, name, age):
        self.color = color
        Animal.__init__(self, country, name, age)  # 调用父类的构造方法

    def catch_mouse(self):
        print('抓老鼠')


cat1 = Cat('黑色', '中国', 'Tom', 10)  # 子类也有__init__方法，这时候子类的__init__方法中，必须调用父类的__init__方法
print(cat1.name, cat1.country, cat1.color, cat1.age)  # Tom 中国 黑色 10
