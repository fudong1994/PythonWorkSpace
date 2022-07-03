"""
-------------------------------------------------
   File Name:python_senior23
   Author:Lee
   date: 2021/6/10-15:02
-------------------------------------------------
"""
"""
requests 模拟接口之间的关联
"""
import requests

# 1、先进行登录
response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                         data={"username": "qingshu", "password": "a123456", "typeId": "101"})
res_body = response.json()  # 获取json格式的响应体数据
print(res_body)
print(type(res_body))  # <class 'dict'>
tk = res_body["token"]  # 获取json格式数据中的key对应的value值，并且保存到变量


# 2、在调用商品信息查询接口
response = requests.post(url="http://127.0.0.1:6666/business/token_goodsInfo",
                         data={"token": tk, "goodsId": "100055", "isOnSale": "", "isPromote": ""})
res_body = response.json()  # 获取json格式的响应体数据
print(res_body)
