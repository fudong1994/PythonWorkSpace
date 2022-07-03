"""
-------------------------------------------------
   File Name:test_login07
   Author:Lee
   date: 2021/6/16-14:09
-------------------------------------------------
"""

import unittest, requests
from ddt import ddt, data
from day15.excel_utils05 import ReadExcel

cases = ReadExcel.read_data_all(r'./cases.xlsx', 'Login')


# for case in cases:
#     print(case.case_id, case.url, case.case_data, case.expect)


@ddt
class LoginTest(unittest.TestCase):
    @data(*cases)
    def test_login01(self, case):
        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()

        try:
            self.assertEqual(eval(case.expect), res_body)
        except AssertionError as e:
            ReadExcel.write_data('cases.xlsx', 'Login', case.case_id, 7, '失败')
        else:
            ReadExcel.write_data(r'./cases.xlsx', 'Login', case.case_id, 7, '成功')


if __name__ == '__main__':
    unittest.main()
