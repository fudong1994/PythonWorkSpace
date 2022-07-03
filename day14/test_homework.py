"""
-------------------------------------------------
   File Name:test_homework
   Author:Lee
   date: 2021/6/11-15:53
-------------------------------------------------
"""

"""
对注册接口进行测试：
1、使用postman进行测试，并且保留测试数据
2、使用unittest进行测试
3、将测试案例添加到测试套件中，并且生成html格式测试结果报告
"""
import requests, unittest
from day11.db_utils03 import DBUtils


class RegisterTest(unittest.TestCase):
    # 1.正确流程
    def test_register01(self):
        db = DBUtils()
        db.cud('delete from tb_user where name = "xiaohua"')
        db.close()
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={"username": "xiaohua", "password": "a123456", "re_password": "a123456",
                                       "email": "123@139.com", "phone": "18656031111"})
        res_body = response.json()
        self.assertEqual({"code": 9999, "msg": "注册成功！"}, res_body)

    # 2.用户名为空
    def test_register02(self):
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={"username": "", "password": "a1234567", "re_password": "a1234567",
                                       "email": "12345@139.com", "phone": "18656031122"})
        res_body = response.json()
        self.assertEqual({"code": 1001, "msg": "用户名不能为空"}, res_body)

    # 密码为空
    def test_register03(self):
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={"username": "牛牛", "password": "", "re_password": "a12345678",
                                       "email": "123456@139.com", "phone": "18656031222"})
        res_body = response.json()
        self.assertEqual({"code": 1002, "msg": "密码不能为空"}, res_body)

    # 用户名已存在
    def test_register04(self):  # 数据回滚
        db = DBUtils()
        db.cud('delete from tb_user where name = "xiaoting"')
        db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)',
               ('xiaoting', 'a77777', '666@136.com', '18155112222'))
        db.close()
        response = requests.post(url='http://127.0.0.1:5000/register',
                                 data={"username": "xiaoting", "password": "a777778", "re_password": "a777778",
                                       "email": "6667@136.com", "phone": "18155112228"})
        res_body = response.json()
        self.assertEqual({"code": 1008, "msg": "用户名已存在"}, res_body)
