"""
-------------------------------------------------
   File Name:python_senior21
   Author:Lee
   date: 2021/6/10-10:40
-------------------------------------------------
"""
"""
requests 用来模拟http请求
为什么要学习requests：因为我们要脱离工具的测试，改成使用代码调用接口进行测试
使用步骤：
1、pip install requests
2、导入该包 import requests
3、使用requests模拟请求
"""

import requests

# 发送get请求
response = requests.get(url='http://www.baidu.com')  # 发送请求
# res_body = response.text  # 获取响应体内容方式1
res_body = response.content.decode('utf-8')  # 获取响应体内容方式1

# 案例：通过requests调用我们自己的登录接口
response = requests.get(url='http://127.0.0.1:5000/login?username=xiaohua&password=a123456')
res_body1 = response.content.decode('utf-8')
print(res_body1)  # {"code": 9999, "msg": "登录成功"}

# 发送post请求
# 注意：发送post请求，因为请求数据放在请求体中，所以需要传入一个字典 存放请求数据
response = requests.post(url='http://127.0.0.1:5000/login', data={'username': 'xiaohei', 'password': 'a123456'})
# res_body1 = response.content.decode('utf-8')
res_body1 = response.json()
print(res_body1)  # {"code": 9999, "msg": "登录成功"}

wd = input('请输入您想搜索的内容：')
response = requests.get(url='http://www.baidu.com/s?wd=%s' % wd)
res_body1 = response.content.decode('utf-8')
print(res_body1)
