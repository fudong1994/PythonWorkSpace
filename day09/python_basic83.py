"""
-------------------------------------------------
   File Name:python_basic83
   Author:Lee
   date: 2021/6/3-16:01
-------------------------------------------------
"""
"""
方法重写/方法覆盖：子类继承父类，子类和父类具有相同的方法
"""


class Animal:
    country = ''
    name = ''
    age = 0

    def walk(self):
        print('父类的walk方法')

    def say(self):
        print('%s正在咆哮' % self.name)


class Dog(Animal):  # Dog类继承了Animal类
    def walk(self):
        print('子类的walk方法')


am1 = Animal()
am1.walk()  # 调用父类的walk方法

dog1 = Dog()
dog1.walk()  # 子类的walk方法
# 多态 子类的对象调用父类的方法
super(Dog, dog1).walk()  # 父类的walk方法