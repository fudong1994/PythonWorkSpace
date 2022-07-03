"""
-------------------------------------------------
   File Name:python_senior03
   Author:Lee
   date: 2021/6/8-10:50
-------------------------------------------------
"""
"""
知识点：python操作mysql，进行增删改
"""
# 第一步：导入第三方模块，pymysql是一个第三方的模块(我们需要先进行安装),再导包，然后通过pymysql操作myslq数据库
import pymysql

# 第二步：获取连接对象(我们需要指定mysql服务器的ip地址、端口号、用户名、密码、指定的库名)
# mysql的默认端口号3306、 Oracle默认的是1521、 http默认的端口是80
# 127.0.0.1和localhost都是代表本机地    址
# db是database的缩写，代表数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)  # <pymysql.connections.Connection object at 0x00000244B9C79780> # 代表Connection类的对象

# 第三步：获取一个游标对象
cursor = conn.cursor()  # 游标能够存储结果集

# 第四步：通过游标对象执行sql语句
# count = cursor.execute('insert into account(name,age,nickName) values("xiaohong",20,"红红")')
# count = cursor.execute('insert into account(name,age,nickName) values(%s,%s,%s)', ('xiaohong', 20, 'honghong'))
# count = cursor.execute('update account set name = "大红" where name = "xiaohong"')
# count = cursor.execute('update account set name = %s where name = %s', ('dahong', 'xiaohong'))
count = cursor.execute('delete from account where name = %s', ('dahong',))
print(count)

# 第五步：增删改都需要提交，不能忘记，否则数据库不变
conn.commit()
# 第六步：关闭游标
cursor.close()
# 第七步:关闭链接
conn.close()
