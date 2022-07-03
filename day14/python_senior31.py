"""
-------------------------------------------------
   File Name:python_senior31
   Author:Lee
   date: 2021/6/11-10:06
-------------------------------------------------
"""
"""
不使用框架进行测试，我们也能测试，但是比较麻烦
"""
import requests

# 1、正确流程
response = requests.post(url='http://127.0.0.1:5000/login',
                         data={"username": "xiaohua", "password": "a123456"})
res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 9999, "msg": "登录成功"}

# 2、用户名错误
response = requests.post(url='http://127.0.0.1:5000/login',
                         data={"username": "xiaohua@@", "password": "a123456"})
res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 1003, "msg": "用户名或密码错误"}

# 3、用户名为空
response = requests.post(url='http://127.0.0.1:5000/login',
                         data={"username": "", "password": "a123456"})
res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 1001, "msg": "用户名不能为空"}

# 4、密码错误
response = requests.post(url='http://127.0.0.1:5000/login',
                         data={"username": "xiaohua", "password": "a12345678"})
res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 1003, "msg": "用户名或密码错误"}

# 5、密码为空
response = requests.post(url='http://127.0.0.1:5000/login',
                         data={"username": "xiaohua", "password": ""})
res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 1002, "msg": "密码不能为空"}
