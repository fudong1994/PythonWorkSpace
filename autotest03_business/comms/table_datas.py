"""
-------------------------------------------------
   File Name:table_datas.py
   Author:Lee
   date: 2021/6/24-15:56
-------------------------------------------------
"""
"""
从数据库过滤捞取数据
"""
from comms.db_utils import DBUtils


class CaseData(object):
    def __init__(self, dict_case):
        for i in dict_case.items():
            setattr(self, i[0], i[1])  # 利用反射添加属性


# 链接tb_user表  拿数据
def get_tb_user(num):
    """
    :param num: 需要读取数据的条目数
    :return: 把每行的数据以对象形式返回
    """
    db = DBUtils()
    allCase = []
    find_all = db.find_all('select * from tb_user limit %s;', (num,))
    # print(find_all)
    for i in find_all:
        if i['typeId'] == 101:  # 把咱们的typeId字段理解为过滤数据的一个标识符
            data = CaseData(i)
            allCase.append(data)
    db.close()
    return allCase


# 链接tb_order表 拿数据
def get_tb_order(num):
    """
    :param num: 需要读取数据的条目数
    :return: 把每行的数据以对象形式返回
    """
    db = DBUtils()
    allCase = []
    find_all = db.find_all("select * from tb_order order by rand() limit %s;", (num,))
    # print(find_all)
    for i in find_all:
        # if i["status"] == 4:  # 数据库状态4 代表已完成的订单
        data = CaseData(i)
        allCase.append(data)
    db.close()
    return allCase


if __name__ == "__main__":
    allCase = get_tb_order(1)
    # print(allCase[0].orderId)
