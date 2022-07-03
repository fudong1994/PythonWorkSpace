"""
-------------------------------------------------
   File Name:python_senior22
   Author:Lee
   date: 2021/6/10-14:21
-------------------------------------------------
"""
"""
requests模拟json请求(请求体数据为json格式的请求)
"""
import requests, json

# 发送json请求需要三个入参:
# 1、url
# 2、json格式的入参(使用json.dumps(入参数据),把字典类型的入参，转换为json)
# 3、必须添加请求头信息："Content-Type":"application/json"，表明请求体数据的内容类型为json格式

response = requests.post(url='http://127.0.0.1:6666/business/regist_json',
                         data=json.dumps({
                             "username": "qingshu2",
                             "password": "a123456",
                             "re_password": "a123456",
                             "phone": "16655558882",
                             "sex": "女",
                             "birthday": "",
                             "qq": "",
                             "email": "1239991@qq.com"
                         }),
                         headers={"Content-Type": "application/json"})

res_body = response.content.decode('utf-8')
print(res_body)  # {"code": 1000, "msg": "注册成功"}
