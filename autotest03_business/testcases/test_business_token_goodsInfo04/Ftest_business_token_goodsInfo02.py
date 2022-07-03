"""
-------------------------------------------------
   File Name:test_business_token_goodsInfo01
   Author:Lee
   date: 2021/6/24-16:22
-------------------------------------------------
"""

"""
1.正常流程
2.解决数据会滚和数据验证
"""
import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import get_token, replace_data
from comms.log_utils import logger


@ddt
class TestTokenGoodsInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_all(DATA_FILE, 'business_token_goodsInfo')

    @data(*cases)
    def test_token_goods_info(self, case):
        if "#token#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        try:
            if case.case_id == 1:
                self.assertIn(case.expect, str(res))  # 判定响应结果包含 查询成功
                # 判断条目数是否正确
                # 1.获取返回结果的条目数
                re_count = len(res["goods_tiems"])
                db_count = self.db.find_count('select * from tb_goods;')
                self.assertEqual(re_count, db_count)  # 响应的结果条目数和数据库中的商品条目数进行比对
            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goodsInfo', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goodsInfo', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功!'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
