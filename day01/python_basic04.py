"""
-------------------------------------------------
   File Name:python_basic04
   Author:Lee
   date: 2021/5/24-16:38
-------------------------------------------------
"""
"""
本章讲解：数字类型、布尔类型
"""

# 数字类型 分为 int/float
a = 10
b = 10 / 3
print(a)  # 10
print(b)  # 3.3333333333333335

# 查看类型的函数 type()
print('a的变量类型为：', type(a))  # a的变量类型为： <class 'int'>
print('b的变量类型为：', type(b))  # b的变量类型为： <class 'float'>

# 布尔类型(bool)：只有2个值  True (真、成立)  False (假、不成立)
bo1 = 10 < 3
print(bo1)  # False

bo2 = 10 > 3
print(bo2)  # True
print('变量bo2的类型：', type(bo2))  # 变量bo2的类型： <class 'bool'>

# 类型的强制转换，使用   类型()
c = int(False)
print(c)  # 0
d = int(True)
print(d)  # 1

# 整数转布尔
# 除了0以外，其余所有整数转换bool类型都是True
bo3 = bool(0)
print(bo3)  # False

print(bool(5))  # True

# 浮点数转布尔
# 除了0.0以外，其余所有浮点数转换bool类型都是True
bo5 = bool(0.00000)
print(bo5)  # False

print(bool(1.0))  # True

"""
总结：非0为真
"""

# 字符串：用来保存一串字符  str
str1 = 'xiaohua'
str2 = "xiaohua"
str3 = '''xiaohua'''
str4 = """xiaohua"""

print(str1, str2, str3, str4)

# 字符串在使用过程中的一些注意事项

# 1. 单引号和双引号可以配合使用，但是需要符合书写规范
print("王琰同学是个'优秀'的测试工程师！")  # 王琰同学是个'优秀'的测试工程师！   单引号变成字符串里的成员了
print('"xiaohua"')  # "xiaohua"

# 2.字符串过长可以使用反斜杠进行换行，仍然是一行
str5 = 'dahksdhlahdajlknc' \
       'zjxk.ncjkzxncjkldhuiqlwghdad' \
       'n.sdbajsbdkjfgedy' \
       'kqwfeqwkvekjwqvevdsah,dvsah,d'
print(str5)

# 3.在print()中，字符串过长可以直接敲回车换行，结果仍是一行
print('dalkshdaklsdlkasbgdlkqbwk'
      'lebgqledbqwlebwqlebdlwqbedlqwbed')

# 4.原样输出字符串，取消所有的编译
print("""
第一行
第二行
第三行
第四行
""")

# input() 这个函数用来读控制台的输入，可以接收控制台的输入内容，并且保存在变量中
name = input('请输入您的姓名：')  # 变量name接收input()函数输入的数据
print('输入的姓名是：', name)
print(type(name))  # <class 'str'>

age = input('请输入您的年龄：')  # input()读取的所有从控制台的输入都是字符串类型
print('姓名是：', name, '年龄是：', age)
print(type(age))  # <class 'str'>

# 设计一个简单的两位整数加法运算器
num1 = input('请输入第一个整数：')
num2 = input('请输入第二个整数：')
sm = int(num1) + int(num2)
print('两个整数之和是：', sm)
