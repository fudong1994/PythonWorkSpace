"""
-------------------------------------------------
   File Name:test_regist07
   Author:Lee
   date: 2021/6/17-10:28
-------------------------------------------------
"""
import unittest, requests
from ddt import ddt, data
from autotest01.comms.db_utils import DBUtils
from autotest01.comms.log_utils import logger
from autotest01.comms.excel_utils import ReadExcel


@ddt
class RegisterTest(unittest.TestCase):
    cases = ReadExcel.read_data_all(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Register')

    @data(*cases)
    def test_register(self, case):
        db = DBUtils()
        # 正确流程
        if case.case_id == 1:
            username = eval(case.case_data)["username"]  # 获取传入的用户名
            db.cud('delete from tb_user where name = %s', (username,))
        elif case.case_id == 5:  # 用户名已存在的case
            username = eval(case.case_data)["username"]  # 获取传入的用户名
            password = eval(case.case_data)["password"]
            email = eval(case.case_data)["email"]
            phone = eval(case.case_data)["phone"]
            db.cud('delete from tb_user where name = %s', (username,))
            db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)',
                   (username, password, email, phone))
        db.close()

        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()
        try:
            self.assertEqual(eval(case.expect), res_body)
        except AssertionError as e:
            ReadExcel.write_data(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Register', case.case_id, 7,
                                 '失败')
            logger.error('测试编号{},测试用例标题{},执行失败,实际结果：{}'.format(case.case_id, case.case_title, res_body))
            logger.exception(e)
            raise e  # 手动抛出异常 不然断言可能为通过
        else:
            ReadExcel.write_data(r'D:\Tools\PythonWorkSpace\autotest01\datas\cases.xlsx', 'Register', case.case_id, 7,
                                 '成功')
            logger.info('测试编号{},测试用例标题{},执行成功'.format(case.case_id, case.case_title))

