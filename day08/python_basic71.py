"""
-------------------------------------------------
   File Name:python_basic71
   Author:Lee
   date: 2021/6/2-14:36
-------------------------------------------------
"""
"""
知识点1：面向对象：面向对象是一个编程思想(一切皆对象)
知识点2：类和对象
    类：具有相同特征的一类事物的描述
            比如订单，所有订单都应该有以下的功能：
                静态的内容：商品编号、商品价格、商品数量、商品信息.....
                动态的内容：加入商品、删除商品、修改数量.....
            
    对象：对象是类的一个具体实例(比如：小王的订单、小刘的订单、小李的订单....)
    
    对象和类的关系：一个类可以有无数个对象

知识点3：类的构成
    类中包含属性和方法：
    属性：把静态的内容抽象出来，并且使用变量进行声明(类中的变量就是属性)
    方法：把动态的内容抽象出来，并且使用函数进行声明(类中的函数就是方法)
    
知识点4：self 代表当前对象
"""


# 创建一个类
class Cat:
    color = ''
    name = ''
    sex = ''

    def eat(self, food):
        print(food, '很好吃')

    def run(self):
        print('小样，来追我啊~')


# 创建实例对象
cat1 = Cat()
cat2 = Cat()
cat3 = Cat()


# 为对象的属性赋值
cat1.color = '粉色'
cat1.name = 'kitty'

# 对象可以调用类的方法
cat1.eat('小鱼')
cat1.eat('杰瑞')
cat1.run()

cat2.eat('面条')

# 定义一个类，并且声明属性和方法，创建该类的对象，并且为该对象的属性赋值，在调用该对象的方法