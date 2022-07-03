"""
-------------------------------------------------
   File Name:test_business_token_items01
   Author:Lee
   date: 2021/6/25-15:50
-------------------------------------------------
"""

import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.public_api import replace_data, get_token
from comms.table_datas import get_tb_order
from comms.log_utils import logger

"""
1.正常流程
"""


@ddt
class TestOrderItems(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_order_items', 1, 1)

    @data(*cases)
    def test_token_orderItems(self, case):
        result = get_tb_order(1)
        orderId = result[0].orderId
        print(orderId)

        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if "#orderId#" in case.case_data:
            case.case_data = replace_data(case.case_data, 'orderId', orderId)

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()
        # 四表链接查询orderId数据，如果查询多条和goods_tiems作比较，如果查询单条数据，判断返回报文包含查询成功，如果没查到数据，判断返回报文包含查询无结果
        try:
            if case.case_id == 1:
                sql = 'select * from tb_user u,tb_order o,tb_goods g,tb_order_goods og ' \
                      'where u.userId = o.userId and o.orderId = og.orderId and og.goodsId = g.goodsId ' \
                      'and o.orderId = %s;'
                count = self.db.find_count(sql, (orderId,))
                if count > 0:
                    self.assertEqual(count, len(res["goods_tiems"]))
                    self.assertIn('查询成功', str(res))
                elif count == 0:
                    self.assertIn('查询无结果', str(res))
            else:
                self.assertEqual(eval(case.expect), res)
        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_order_items', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_order_items', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功!'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
