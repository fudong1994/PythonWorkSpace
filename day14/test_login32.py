"""
-------------------------------------------------
   File Name:test_login32
   Author:Lee
   date: 2021/6/11-10:13
-------------------------------------------------
"""
import unittest, requests

"""
使用框架进行测试，解决自动比对
注意使用unittest框架步骤：
    1、定义测试类，类名最好和被测试的接口匹配，并且测试类需要继承TestCase类
    2、所有的测试方法必须以test 开头
    3、我们可以使用断言对结果进行比对
"""


class LoginTest(unittest.TestCase):  # 测试类需要继承TestCase类，这是当前的类就是测试类
    def test_login01(self):  # 所有的测试方法必须以test开头
        # 正确流程
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data={"username": "xiaohua", "password": "a123456"})
        res_body = response.json()  # 把实际结果转成字典方便比对
        # assertEqual(A,B) 断言A和B是否相等，在这里实际上判断预期结果和实际结果是否相等
        self.assertEqual({"code": 9999, "msg": "登录成功"}, res_body)  # assert是断言的意思， Equal是相等、比较的意思

    def test_login02(self):
        # 用户名错误
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data={"username": "xiaohua@@", "password": "a123456"})
        res_body = response.json()
        self.assertEqual({"code": 1003, "msg": "用户名或密码错误"}, res_body)

    def test_login03(self):
        # 用户名为空
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data={"username": "", "password": "a123456"})
        res_body = response.json()
        self.assertEqual({"code": 1001, "msg": "用户名不能为空"}, res_body)

    def test_login04(self):
        # 密码错误
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data={"username": "xiaohua", "password": "a12345678"})
        res_body = response.json()
        self.assertEqual({"code": 1003, "msg": "用户名或密码错误"}, res_body)

    def test_login05(self):
        # 密码为空
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data={"username": "xiaohua", "password": ""})
        res_body = response.json()
        self.assertEqual({"code": 1002, "msg": "密码不能为空"}, res_body)


if __name__ == '__main__':
    unittest.main()

