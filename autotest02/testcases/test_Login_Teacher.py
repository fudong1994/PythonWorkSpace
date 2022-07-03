"""
-------------------------------------------------
   File Name:test_Login_Teacher
   Author:Lee
   date: 2021/6/22-11:23
-------------------------------------------------
"""
import unittest, requests
from ddt import ddt, data
from autotest02.comms.constants import DATA_FILE
from autotest02.comms.excel_utils import ReadExcel
from autotest02.comms.log_utils import logger
from autotest02.comms.db_utils import DBUtils


@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # 该方法是unittest的测试夹具，整个测试类运行之前运行
        cls.db = DBUtils()  # 创建db对象并且赋值给当前类的db属性(db属性是类属性、可以类名调用，也可以对象调用)

    cases = ReadExcel.read_data_all(DATA_FILE, '登录')

    @data(*cases)
    def test_login01(self, case):
        # 正确流程
        if case.case_id == 1:
            username = eval(case.case_data)["username"]
            password = eval(case.case_data)["password"]
            self.db.cud('delete from tb_user where name = %s', (username,))
            self.db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)',
                        (username, password, '8888@169.com', '19988882222'))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res_body = response.json()

        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res_body))
            else:
                self.assertEqual(eval(case.expect), res_body)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, '登录', case.case_id, 7, '失败')
            logger.error('测试编号{},测试用例的标题为:{},执行失败！实际结果为:{}'.format(case.case_id, case.case_title, res_body))
            logger.exception(e)
            raise e  # 手动抛出异常
        else:
            ReadExcel.write_data(DATA_FILE, '登录', case.case_id, 7, '成功')
            logger.info('测试编号{},测试用例的标题为:{},执行成功！'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):  # 整个测试类运行结束后运行
        cls.db.close()


if __name__ == '__main__':
    unittest.main()
