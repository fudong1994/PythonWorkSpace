"""
-------------------------------------------------
   File Name:python_senior
   Author:Lee
   date: 2021/6/8-10:37
-------------------------------------------------
"""
"""
知识点：python操作mysql，通过占位符查询
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

# 第四步：把活的数据通过%s进行占位，在通过元组进行赋值[这种方式更加安全，他会先在发送sql语句结构，再发送数据]
count = cursor.execute('select * from tb_user where name = %s and sex = %s', ('xiaohua', '女'))  # 预防sql注入
print(count)  # 1

# 第五步：获取查询结果
data = cursor.fetchone()
print(data)  # (100018, 'xiaohua', 'a123456', '123456@qq.com', '女', datetime.date(1995, 5, 5), None, '15866666666', 101)

# 第六步：关闭游标
cursor.close()

# 第七步:关闭链接
conn.close()
