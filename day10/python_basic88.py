"""
-------------------------------------------------
   File Name:python_basic88
   Author:Lee
   date: 2021/6/4-14:07
-------------------------------------------------
"""

# 模拟数据库数据，假设数据库中只有如下数据
users = {"username": "小花", "password": "123456"}


# 注册功能
def register(username, password, re_password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif username == users.get('username'):
        return {"code": 1002, "msg": "用户名已注册"}
    elif len(password) == 0:
        return {"code": 1003, "msg": "密码不能为空"}
    elif password != re_password:
        return {"code": 1004, "msg": "两次密码输入不一致"}
    elif not (6 <= len(username) <= 18 and 6 <= len(password) <= 18):
        return {"code": 1005, "msg": "用户名和密码必须在6-18位之间"}
    else:
        return {"code": 0000, "msg": "注册成功"}


# 登录功能
def login(username, password):
    if len(username) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif len(password) == 0:
        return {"code": 1002, "msg": "密码不能为空"}
    elif username == users.get('username') and password == users.get('password'):
        return {"code": 9999, "msg": "登录成功"}
    else:
        return {"code": 1003, "msg": "用户名或密码错误"}


