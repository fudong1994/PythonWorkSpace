"""
-------------------------------------------------
   File Name:test_business_goods_inputs01
   Author:Lee
   date: 2021/6/26-15:57
-------------------------------------------------
"""
"""
1.正常流程
"""
import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.public_api import replace_data, get_token


@ddt
class TestGoodsInput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_goods_input', 1, 1)

    @data(*cases)
    def test_goods_input(self, case):
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        print(case.case_data)

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_input', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功!'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
