"""
-------------------------------------------------
   File Name:test_login02
   Author:Lee
   date: 2021/6/15-14:27
-------------------------------------------------
"""
"""
使用框架进行测试，解决自动比对
注意使用unittest框架步骤：
    1、定义测试类，类名最好和被测试的接口匹配，并且测试类需要继承TestCase类
    2、所有的测试方法必须以test 开头
    3、我们可以使用断言对结果进行比对
"""
import unittest, requests
from ddt import ddt, data

cases = [{"case_data": "{'username':'xiaohua','password':'a123456'}", 'exp': '{"code": 9999, "msg": "登录成功"}'},
         {"case_data": "{'username':'','password':'a123456'}", 'exp': '{"code": 1001, "msg": "用户名不能为空"}'},
         {"case_data": "{'username':'xiaohua','password':''}", 'exp': '{"code": 1002, "msg": "密码不能为空"}'},
         {"case_data": "{'username':'xiaohua','password':'a1234567'}", 'exp': '{"code": 1003, "msg": "用户名或密码错误"}'}]


@ddt
class TestLogin(unittest.TestCase):
    @data(*cases)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data=eval(case['case_data']))  # 识别()中的python表达式，把字符串转成字典
        res_body = response.json()
        self.assertEqual(eval(case['exp']), res_body)
