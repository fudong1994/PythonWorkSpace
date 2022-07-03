"""
-------------------------------------------------
   File Name:python_senior_demo
   Author:Lee
   date: 2021/6/8-17:10
-------------------------------------------------
"""
'''
1、使用python语言操作 test库中的emp表
2、通过占位符方式查询出SMith所在的部门名称,并且打印在控制台
3、通过占位符的方式查询出20部门的所有员工的信息。
4、通过占位符的方式查询出job为 SALESMAN的工资总和
5、查询出部门编号20有多少人？
6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
8、删除部门编号为 50的部门
'''
from day11.db_utils03 import DBUtils

db = DBUtils()

# 1、使用python语言操作 test库中的emp表
find_all = db.find_all('select * from emp;')
print(find_all)

# 2、通过占位符方式查询出SMith所在的部门名称,并且打印在控制台
data = db.find_one('select d.dname from emp e,dept d where e.deptno = d.deptno and e.ename = %s', ('SMITH',))
print(data)

# 3、通过占位符的方式查询出20部门的所有员工的信息。
data = db.find_all('select * from emp where deptno = %s', (20,))
print(data)

# 4、通过占位符的方式查询出job为 SALESMAN的工资总和
data = db.find_one('select sum(sal) from emp where job = %s', ("SALESMAN",))
print(data)

# 5、查询出部门编号20有多少人？
data = db.find_one('select count(*) from emp where deptno = %s;', (20,))
print(data[0])

data = db.find_count('select * from emp where deptno = %s', (20,))
print(data)

# 6、为dept表增加部门编号为 50 部门名称为 Test， Loc为‘ShangHai’
# data = db.cud('insert into dept values(%s,%s,%s);', (50, 'Test', 'ShangHai'))
# print(data)

# 7、批量更新dept表中编号为50的部门名称为TestSoftW,30部门的部门名称为SLS
# cud = db.cud('update dept set dname = %s where deptno = %s;', [("SoftwareTest", 50), ("SLS", 30)])
# print(cud)

# 8、删除部门编号为 50的部门
data = db.cud('delete from dept where deptno = %s', (50,))
print(data)

db.close()
