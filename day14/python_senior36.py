"""
-------------------------------------------------
   File Name:python_senior36
   Author:Lee
   date: 2021/6/11-15:44
-------------------------------------------------
"""
import unittest


class TestFixture(unittest.TestCase):

    def setUp(self):  # 每条测试用例执行之前执行
        print('每条测试用例执行之前执行！')

    def tearDown(self):  # 每条测试用例执行之后执行
        print("每条测试用例执行之后执行！！！")

    # @classmethod
    # def setUpClass(cls):  # 每个测试类执行之前执行
    #     print('每个测试类执行之前执行')
    #
    # @classmethod
    # def tearDownClass(cls):  # 每个测试类执行之前执行
    #     print('每个测试类执行之后执行！！！')

    def test_fun1(self):
        print('test_fun1')

    def test_fun2(self):
        print('test_fun2')
