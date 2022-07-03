"""
-------------------------------------------------
   File Name:test_login06
   Author:Lee
   date: 2021/6/16-14:02
-------------------------------------------------
"""

import unittest, requests
from ddt import ddt, data
from day15.excel_utils05 import ReadExcel

cases = ReadExcel.read_data_all(r'./cases.xlsx', 'Login')
for case in cases:
    print(case.case_id, case.url, case.case_data, case.expect)


@ddt
class LoginTest(unittest.TestCase):
    @data(*cases)
    def test_login01(self, case):
        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()
        self.assertEqual(eval(case.expect), res_body)


if __name__ == '__main__':
    unittest.main()
