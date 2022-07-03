"""
-------------------------------------------------
   File Name:python_basic11
   Author:Lee
   date: 2021/5/25-9:43
-------------------------------------------------
"""

"""
本章讲解：str字符串类型
"""

#  知识点1：字符串定义、声明的方式
str1 = 'xiaohua'
str2 = "xiaohua"
str3 = '''xiaohua'''
str4 = """xiaohua"""

# 知识点2：字符串和数字类型互相转换，保证值为数字才能转换

# 数字转字符串
age = 18
age = str(age)  # 数字转字符串
print(age)
print('age的类型是：', type(age))  # age的类型是： <class 'str'>

# 字符串转数字
name = 'xiaohua'
# name = int(name) # ValueError 报错值错误

name = '17'
print(type(name))  # <class 'str'>
name = int(name)  # 字符串里面的字符必须是纯数字才可以转换为数字类型
print(type(name))  # <class 'int'>

# 知识点3： 字符串转布尔类型
name = 'xiaohua'
bo1 = bool(name)
print(bo1)  # True

name2 = ''
bo2 = bool(name2)
print(bo2)  # False

"""
总结：非0即真，非空即真
"""

# 知识点4：字符串可以使用+号拼接，结果还是一个字符串
str1 = '今天'
str2 = '天气'
str3 = '很好'
str4 = '很适合学习python'

str5 = str1 + str2 + str3 + str4
print(str5)  # 今天天气很好很适合学习python  #通过拼接四个字符串成为了一个新的字符串

name = 'xiaohua'
age = 18
# print(name + age) # 数字无法和字符串相加
print(name + str(age))  # xiaohua18

# 字符串可以和整数进行乘法
print('小刘 ' * 5)

# 知识点5：字符串的索引，字符串对每个字符做了编号，从前往后从0开始，从后往前从-1开始
str6 = '我是个机智的小天才'
print(str6[0])  # 我　 []这个代表位置
print(str6[5])  # 的
print(str6[-2])  # 天
# print(str6[9])  # IndexError 下标越界异常

# 知识点6：字符串的切片(截取)    str[开始下标：结束下标]   注意：前包含，后不包含
print(str6[0:5])  # 我是个机智
print(str6[5:-1])  # 的小天
# print(str6[5:-6]) # 没有截取到数据,什么都没打印
print(str6[5:])  # 的小天才  截取了下标从5开始到结束
print(str6[:6])  # 我是个机智的   从下标0开始截取到下标6，但不包含下标6的元素

# 特殊切片
print(str6[:])  # 我是个机智的小天才

str7 = 'abcdefghi'
print(str7[1:5])  # bcde
print(str7[1:5:2])  # bd   2是步长
print(str7[:])
print(str7[::2])  # acegi  截取所有的元素步长是2
print(str7[1:7])  # bcdefg
print(str7[1:7:3])  # be

# 知识点7：字符串的转义： 在python里 \n代表换行  \t 代表制表符 相当于一个tab
str8 = 'abcd\nefghi\tjklmn'
print(str8)  # 输出的结果就加上了 换行 和 制表符

# 关闭转义：可以在字符串前面加   r/R
str9 = R'abcd\nefghi\tjklmn'
print(str9)

# 知识点8：字符串常用的方法   常用的API
# (1) join() 拼接()中的每一个元素，但是括号中的内容必须为字符串
a = '*'
b = a.join('12345')
print(b)  # 1*2*3*4*5

a = '--'
b = a.join('abc')
print(b)  # a--b--c

print('@'.join('123'))  # 1@2@3

# (2) find()  查找括号中的元素在字符串中第一次出现的位置，返回int类型
str10 = 'python_py'
res1 = str10.find('t')
print(res1)  # 2

res2 = str10.find('p')  # 在str10字符串中 查找p第一次出现的位置
print(res2)  # 0

res3 = str10.find('a')
print(res3)  # -1   如果在字符串中没有找到对应的元素，那么返回-1

# (3) replace(a,b)  查找字符串中的元素，将字符串中的a 替换为 b
str11 = '我爱学python_py'
str12 = str11.replace('t', 'T')
print(str12)  # 我爱学pyThon_py

str13 = str11.replace('py', 'www')
print(str13)  # 我爱学wwwthon_www

# 如下字符串，如何去除里面的空格
str14 = 'dashdkuah  saidh alhdsak;l a l;h as haslhdaslk sa daslhdb '
str15 = str14.replace(' ', '')
print(str15)  # dashdkuahsaidhalhdsak;lal;hashaslhdaslksadaslhdb

# (4) count()  统计元素在字符串中出现的次数
str16 = 'qwerqwerqwer'
res4 = str16.count('A')
print(res4)  # 0

res5 = str16.count('qw')
print(res5)  # 3

# (5) .upper()  / .lower()  大小写转换
str17 = 'aaaAAAbbbAAAAcccDDD31213'
str18 = str17.upper()
print(str18)  # AAAAAABBBAAAACCCDDD31213

print(str17.lower())  # aaaaaabbbaaaacccddd31213

# (6) len()  求字符串的长度   length
str19 = 'dfhas'
res6 = len(str19)
print(res6)  # 5

# (7) .isnumeric() 判断字符串是否为纯数字，如果是返回True，否则返回False
str20 = '1234'
print(str20.isnumeric())  # True

str21 = 'a1234c'
print(str21.isnumeric())  # False

# 知识点9：填充
# (1) .format()
str22 = '小花来自{},年龄{},{}来上海工作'  # {}用来占位
str23 = str22.format('北京', 18, '2020年')  # 填充的值要和{}数量对应
print(str23)  # 小花来自北京,年龄18,2020年来上海工作

# (2) 填充数据，保留N位小数，{:.2f} 表示保留2位小数
str22 = '小花来自{},年龄{},{}来上海工作,目前年薪{:.2f}万'
str23 = str22.format('北京', 18, '2020年', 20.66666666666)
print(str23)

# (3) 通过下标进行填充 format() 后面的每一个数据下标位1/2/3/4/5
str22 = '小花来自{0},年龄{1},{1}年来上海工作'
str23 = str22.format('北京', 18)
print(str23)  # 小花来自北京,年龄18,18年来上海工作

# (4) 通过参数进行填充
str22 = '小花来自{a},年龄{b},{b}年来上海工作'
str23 = str22.format(a='beijing', b=18)
print(str23)  # 小花来自beijing,年龄18,18年来上海工作

# (5)传统方式填充
# %s代表字符串类型  %d代表整数类型   %f代表浮点数类型
str22 = '小花来自%s,年龄%d,%d年来上海工作,目前年薪%f万' % ('北京', 18, 18, 12.777)
print(str22)  # 小花来自北京,年龄18,18年来上海工作,目前年薪12.777000万

# str23 = '小花来自%s,年龄%d,%d年来上海工作,目前年薪%f万' % ('北京', 18, '18', 12.777) # TypeError 填充的数据需要和标识一致

str22 = '小花来自%s,年龄%d,%d年来上海工作,目前年薪%f万' % ('北京', 18, 18, 12.7778888888888)
print(str22)  # 小花来自北京,年龄18,18年来上海工作,目前年薪12.777889万

"""
如何声明一个变量,不进行赋值
"""

a = str()
print(type(a))  # <class 'str'>
print(a)  # 打印了一个空

a = bool()
print(type(a))  # bool
print(a)  # False

a = int()
print(type(a))  # int
print(a)  # 0

a = float()
print(type(a))  # float
print(a)  # 0.0
