"""
-------------------------------------------------
   File Name:db_utils02
   Author:Lee
   date: 2021/6/8-11:23
-------------------------------------------------
"""
import pymysql


class DBUtils:
    count = -1

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

    # 封装查询结果集有多少条数据   条目数
    # 如果execute()只传一个参数，我们需要运行count = cursor.execute(sql)
    # 如果execute()传2个参数，我们需要运行 count = cursor.execute(sql,占位符数据(元组))
    def find_count(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
                return self.count
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
                return self.count
        except Exception as e:
            print('查询数据库条目数失败:', e)

    # 封装增删改
    # 如果execute()只传一个参数，我们需要运行count = cursor.execute(sql)
    # 如果execute()传2个参数，我们需要运行 count = cursor.execute(sql,占位符数据(元组))
    def cud(self, sql, params=None):
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            elif params is not None:
                self.count = self.cursor.execute(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print('增删改执行失败:', e)


if __name__ == "__main__":
    db = DBUtils()

    # 调用封装好的查询条目数
    count = db.find_count('select * from account')
    print(count)  # 4

    count = db.find_count('select * from account where name = %s', ('小牛',))
    print(count)  # 1

    # 调用封装好的增删改
    # count = db.cud('delete from account where name = "dahua"')
    # print(count)  # 1

    count = db.cud('delete from account where name = %s', ('小红',))
    print(count)

    db.close()
