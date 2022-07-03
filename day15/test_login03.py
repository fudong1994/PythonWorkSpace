"""
-------------------------------------------------
   File Name:test_login03
   Author:Lee
   date: 2021/6/15-14:40
-------------------------------------------------
"""
"""
将字典转换为对象
"""
import unittest, requests
from ddt import ddt, data

dict1 = {'username': 'xiaohua', 'password': 'a123456'}

print(dict1.items())  # 将字典中的每一对数据都存放在元组中返回  [('username', 'xiaohua'), ('password', 'a123456')]


class CaseData(object):
    def __init__(self, dict_case):  # 获取字典中的每一对数据，并且进行遍历  [('username', 'xiaohua'), ('password', 'a123456')]
        for i in dict_case.items():  # 值遍历
            # print(i[0],i[1])
            setattr(self, i[0], i[1])  # 动态的为对象的属性赋值 username  xiaohua


# 将字典转换为对象
cd = CaseData(dict1)
print(cd.username, cd.password)

# 将cases中所有的字典转换为对象，并且存放到一个列表里
cases = [{"case_data": "{'username':'xiaohua','password':'a123456'}", 'exp': '{"code": 9999, "msg": "登录成功"}'},
         {"case_data": "{'username':'','password':'a123456'}", 'exp': '{"code": 1001, "msg": "用户名不能为空"}'},
         {"case_data": "{'username':'xiaohua','password':''}", 'exp': '{"code": 1002, "msg": "密码不能为空"}'},
         {"case_data": "{'username':'xiaohua','password':'a1234567'}", 'exp': '{"code": 1003, "msg": "用户名或密码错误"}'}]

allCase = []
for case in cases:
    ca = CaseData(case)  # 把字典转换为对象
    allCase.append(ca)  # 把对象存放在列表中
print(allCase)  # 是存放了对象的列表


@ddt
class TestLogin(unittest.TestCase):
    @data(*allCase)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/login',
                                 data=eval(case.case_data))  # 识别()中的python表达式，把字符串转成字典
        res_body = response.json()
        self.assertEqual(eval(case.exp), res_body)


if __name__ == "__main__":
    unittest.main()
