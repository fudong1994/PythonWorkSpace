"""
-------------------------------------------------
   File Name:db_utils01
   Author:Lee
   date: 2021/6/8-11:14
-------------------------------------------------
"""

import pymysql


class DBUtils:
    # 封装链接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('工具类链接出现异常，请检查DBUtils中的__init__方法')
            print(e)

    # 封装关闭游标和链接
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    db = DBUtils()
    db.close()
