"""
-------------------------------------------------
   File Name:read_properties
   Author:Lee
   date: 2021/6/17-15:44
-------------------------------------------------
"""
from configparser import ConfigParser  # 导入模块

# 创建一个解析器对象
cnp = ConfigParser()

# 读取文件
cnp.read(r'./config.ini', encoding='utf-8')
host = cnp.get('mysql', 'host')
print(host)  # 127.0.0.1

passwd = cnp.get('mysql','password')
print(passwd)  # 123456
print(type(passwd))    # <class 'str'>

# 注意get读取的默认数据都是字符串，我们也可以读取成其它类型
port = cnp.getint('mysql','port')
print(port)  # 3306
print(type(port))  # <class 'int'>


