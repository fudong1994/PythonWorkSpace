"""
-------------------------------------------------
   File Name:python_senior01
   Author:Lee
   date: 2021/6/8-9:34
-------------------------------------------------
"""

"""
知识点：python操作mysql,查询(查询单条，查询多条，查询所有)
"""
# 第一步：导入第三方模块，pymysql是一个第三方的模块(我们需要先进行安装),再导包，然后通过pymysql操作myslq数据库
import pymysql

# 第二步：获取连接对象(我们需要指定mysql服务器的ip地址、端口号、用户名、密码、指定的库名)
# mysql的默认端口号3306、 Oracle默认的是1521、 http默认的端口是80
# 127.0.0.1和localhost都是代表本机地址
# db是database的缩写，代表数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)  # <pymysql.connections.Connection object at 0x00000244B9C79780> # 代表Connection类的对象

# 第三步：获取一个游标对象
cursor = conn.cursor()  # 游标能够存储结果集

# 第四步：通过游标对象执行sql语句，把结果存在cursor里，并且返回条目数
count = cursor.execute('select * from tb_user')
print(count)  # 6 获取的结果集的条目数

# 第五步：获取查询结果
# 第一种：获取结果集中的一行数据
# data = cursor.fetchone()  # 返回一行数据，并且包装成元组
# print(data)  # (100000, 'AutoTrue', 'AutoTrue', '预留数据@qq.com', '男', datetime.date(2021, 1, 30), 10000, '15888888888', 101)

# 第二种：获取结果集中的多行数据
# data = cursor.fetchmany(2)  # 获取结果集的2行数据
# print(data)  # 返回多条数据  格式为：((元组1),(元组2).....)

# 第三种：获取所有
data = cursor.fetchall()
print(data)  # 返回结果集中所有的内容，格式为：((元组1),(元组2).....)

# 第六步:关闭游标
cursor.close()

# 第七步:关闭链接
conn.close()
