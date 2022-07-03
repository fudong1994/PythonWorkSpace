"""
-------------------------------------------------
   File Name:assert_33
   Author:Lee
   date: 2021/6/11-10:36
-------------------------------------------------
"""
"""
unittest的断言
"""
import unittest


class Test(unittest.TestCase):

    def test01(self):
        a = b = 1
        self.assertEqual(a, b)  # 断言a和b相等

    def test02(self):
        list1 = [1, 2, 3]
        self.assertIn(2, list1)  # 断言2是否在list1中

    def test03(self):
        self.assertTrue(1 > 0)  # 断言()是否为真

    def test04(self):
        self.assertIsNone(None)  # 断言()是否为空

    # 案例
    def test05(self):
        dict1 = {"code": 9999, "msg": "休息休息", "token": "sdhasdhsakldhaslkdhusaldsalkdbhlkwqedbhkjad=="}
        self.assertIn("token", dict1, msg='断言错误，响应报文没有返回token')
