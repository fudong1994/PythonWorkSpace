"""
-------------------------------------------------
   File Name:test_business_goods_promote01
   Author:Lee
   date: 2021/6/28-16:19
-------------------------------------------------
"""

"""
分析:该接口会对数据库数据进行更改，我们可以造一条数据进行验证，或者使用配置文件进行实现
当前我们可以从数据库捞数据进行测试
1.捞一条 已经上架并且未开启促销的数据进行测试
2.捞一条 未上架未开启促销状态的数据进行测试

核心测试点：
1.促销时间必须大于当前时间
2.促销结束时间必须大于促销开始时间
3.商品已经开启促销不能再次开启促销

注意：1代表未开启促销

1.正常流程

"""

import unittest, requests
from ddt import ddt, data
from comms.db_utils import DBUtils
from comms.excel_utils import ReadExcel
from comms.constants import DATA_FILE
from comms.log_utils import logger
from comms.public_api import get_token, get_ini_data, replace_data


@ddt
class TestGoodsPromote(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = DBUtils()

    cases = ReadExcel.read_data_pl(DATA_FILE, 'business_token_goods_promote', 1, 1)

    @data(*cases)
    def test_goods_promote(self, case):

        # 查询数据库随机获取一条测试数据，并且不能和配置文件的goodsId冲突
        res = self.db.find_one('select * from tb_goods where isPromote = 1 and isOnSale = 0 and goodsId != %s'
                               'order by rand() limit 1', (get_ini_data('goods1', 'goodsId'),))
        goodsId = res["goodsId"]
        # print('goodsId是：', goodsId)  goodsId是： 100130
        if '#token#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'token', get_token())
        if '#goodsId#' in case.case_data:
            case.case_data = replace_data(case.case_data, 'goodsId', goodsId)

        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()

        try:
            self.assertEqual(eval(case.expect), res)

        except AssertionError as e:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_promote', case.case_id, 7, '失败')
            logger.error('测试编号:{},测试用例标题:{},执行失败,实际结果为:{}'.format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e
        else:
            ReadExcel.write_data(DATA_FILE, 'business_token_goods_promote', case.case_id, 7, '成功')
            logger.info('测试编号:{},测试用例标题:{},执行成功!'.format(case.case_id, case.case_title))

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
