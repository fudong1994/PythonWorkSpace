"""
-------------------------------------------------
   File Name:test_login07
   Author:Lee
   date: 2021/6/16-14:09
-------------------------------------------------
"""

import unittest, requests
from ddt import ddt, data
from autotest01.comms.db_utils import DBUtils
from autotest01.comms.log_utils import logger
from autotest01.comms.excel_utils import ReadExcel

cases = ReadExcel.read_data_all(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Login')


# for case in cases:
#     print(case.case_id, case.url, case.case_data, case.expect)


@ddt
class LoginTest(unittest.TestCase):
    @data(*cases)
    def test_login01(self, case):
        # 正确流程
        if case.case_id == 1:
            username = eval(case.case_data)["username"]
            password = eval(case.case_data)["password"]
            db = DBUtils()
            db.cud('delete from tb_user where name = %s', (username,))
            db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)',
                   (username, password, '8888@169.com', '19988882222'))
            db.close()

        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()

        try:
            self.assertEqual(eval(case.expect), res_body)
        except AssertionError as e:
            ReadExcel.write_data(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Login', case.case_id, 7,
                                 '失败')
            logger.error('测试编号{},测试用例的标题为:{},执行失败！实际结果为:{}'.format(case.case_id, case.case_title, res_body))
            logger.exception(e)
            raise e  # 手动抛出异常
        else:
            ReadExcel.write_data(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Login', case.case_id, 7,
                                 '成功')
            logger.info('测试编号{},测试用例的标题为:{},执行成功！'.format(case.case_id, case.case_title))


if __name__ == '__main__':
    unittest.main()
