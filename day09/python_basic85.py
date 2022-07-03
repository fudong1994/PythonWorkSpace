"""
-------------------------------------------------
   File Name:python_basic85
   Author:Lee
   date: 2021/6/3-17:01
-------------------------------------------------
"""
"""
1、多继承：一个子类可以继承多个父类
2、多继承的情况下，子类会先在自己类中去找需要的内容，找不到去父类中去找
    该顺序按照 __mro__提供的顺序去找
"""


class Father(object):
    def f1(self):
        print('这是父类01')


class Mother(object):
    def f1(self):
        print('这是父类02')


class Baby(Father, Mother):
    pass


by = Baby()
by.f1()  # 这是父类01
print(Baby.__mro__)  # 查看继承顺序


# (<class '__main__.Baby'>, <class '__main__.Father'>, <class '__main__.Mother'>, <class 'object'>)


# 菱形继承
class A:
    def test(self):
        print('from A')


class B(A):
    def test(self):
        print('from B')


class C(A):
    def test(self):
        print('from C')


class D(B, C):
    pass
    # def test(self):
    #     print('from D')


dd = D()
dd.test()  # 查找顺序 D、B、C、A、O
print(D.__mro__)


# 钻石继承
class A:
    def test(self):
        print('from A')


class B(A):
    # def test(self):
    #     print('from B')
    pass


class C(A):
    def test(self):
        print('from C')


class D(B):
    pass
    # def test(self):
    #     print('from D')


class E(C):
    def test(self):
        print('from E')


class F(D, E):
    pass
    # def test(self):
    #     print('from F')


ff = F()
ff.test()  # 查找顺序 F、D、B、E、C、A、O
print(F.__mro__)

# 查看继承的父类 __bases__
print(F.__bases__)  # (<class '__main__.D'>, <class '__main__.E'>)
print(D.__bases__)  # (<class '__main__.B'>,)

# isinstance()  判断第一个参数是否是第二参数的实例对象，返回bool类型
print(isinstance(123, int))  # True
print(isinstance(ff, F))  # True

# issubclass()  判断第一个参数是否是第二个参数的 派生类,返回bool类型
print(issubclass(F, A))  # True
print(issubclass(F, D))  # True
