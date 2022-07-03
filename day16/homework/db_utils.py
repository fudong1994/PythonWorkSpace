"""
-------------------------------------------------
   File Name:db_utils03
   Author:Lee
   date: 2021/6/8-14:21
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
        self.conn.commit()
        try:
            if params is None:
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count
        except Exception as e:
            print('增删改执行失败:', e)

    # 封装查询一条数据  注意： execute(sql)  execute(sql,params)
    def find_one(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句，并且把结果存在cursor
                return self.cursor.fetchone()  # 从结果集里获取一条数据
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchone()
        except Exception as e:
            print('查询单条数据失败：', e)

    # 封装查询所有数据
    def find_all(self, sql, params=None):
        self.conn.commit()
        try:
            if params is None:
                self.cursor.execute(sql)  # 执行sql语句，并且把结果存在cursor
                return self.cursor.fetchall()  # 从结果集里获取一条数据
            elif params is not None:
                self.cursor.execute(sql, params)
                return self.cursor.fetchall()
        except Exception as e:
            print('查询所有数据失败：', e)


if __name__ == '__main__':
    db = DBUtils()
    count = db.find_count('select * from tb_user')
    print(count)  # 5

    # cud = db.cud('delete from tb_user where name = %s', ('xiaoxu',))
    # print(cud)  # 1

    one = db.find_one('select * from tb_user where name = %s', [('xiaohua',)])
    print(
        one)  # (100018, 'xiaohua', 'a123456', '123456@qq.com', '女', datetime.date(1995, 5, 5), None, '15866666666', 101)

    find_all = db.find_all('select * from tb_user where sex = %s', ('女',))
    print(find_all)

    db.close()
