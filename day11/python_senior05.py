"""
-------------------------------------------------
   File Name:python_senior05
   Author:Lee
   date: 2021/6/8-14:38
-------------------------------------------------
"""

from day11.db_utils03 import DBUtils

# 创建DBUtils类的对象  自动获取conn链接对象和 cursor游标对象
db = DBUtils()
cud = db.cud("insert into account(name,age,nickName) values(%s,%s,%s)", ("小马", 20, "小马驹"))
print(cud)  # 获取受影响的行数

db.close()
