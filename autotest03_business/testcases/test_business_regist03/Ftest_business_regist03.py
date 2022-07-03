"""
-------------------------------------------------
   File Name:test_business_regist01
   Author:Lee
   date: 2021/6/23-15:17
-------------------------------------------------
"""

"""
1.正常流程
2.解决数据回滚和数据验证
3.追加其他case
"""

import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.log_utils import logger
from comms.constants import DATA_FILE


@ddt
class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_all(DATA_FILE, '注册1')

    @data(*cases)
    def test_register(self, case):

        # 数据回滚
        if case.case_id in (1, 3, 10):
            uname = eval(case.case_data)["username"]
            email = eval(case.case_data)["email"]
            phone = eval(case.case_data)["phone"]
            self.db.cud('delete from tb_user where name = %s or email = %s or phone = %s;', (uname, email, phone))
        if case.case_id == 8:  # 考虑用户名重复、手机号和邮箱不重复的场景
            uname = eval(case.case_data)["username"]
            email = eval(case.case_data)["email"]
            phone = eval(case.case_data)["phone"]
            self.db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);',
                        (uname, 'a123123', 'qqq@qq.com', '19955558888'))
            self.db.cud('delete from tb_user where email = %s or phone = %s;', (email, phone))
        if case.case_id == 20:  # 考虑手机号重复、用户名和邮箱不重复
            uname = eval(case.case_data)["username"]
            email = eval(case.case_data)["email"]
            self.db.cud('delete from tb_user where name = %s or email = %s;', (uname, email))

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)  # 判定响应结果
            # 数据验证
            if case.case_id in (1, 3, 10):
                count = self.db.find_count('select * from tb_user where name = %s;', (uname,))
                self.assertEqual(1, count)

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, '注册1', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, '注册1', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功!'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
