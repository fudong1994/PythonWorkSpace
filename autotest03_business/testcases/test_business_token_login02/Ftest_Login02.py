"""
-------------------------------------------------
   File Name:test_Login_Teacher
   Author:Lee
   date: 2021/6/22-11:23
-------------------------------------------------
"""
import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger

"""
1.主流程
2.数据会滚
"""

@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_all(DATA_FILE, '登录1')

    @data(*cases)
    def test_login(self, case):

        # 数据回滚
        if case.case_id == 1:
            uname = eval(case.case_data)["username"]
            passwd = eval(case.case_data)["password"]
            self.db.cud('delete from tb_user where name = %s or email = %s or phone = %s',
                        (uname, 'test19@qq.com', '18656032222'))
            self.db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)',
                        (uname, passwd, 'test19@qq.com', '18656032222'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))
            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, '登录1', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, '登录1', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功！'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
