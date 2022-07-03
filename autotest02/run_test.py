"""
-------------------------------------------------
   File Name:run_test
   Author:Lee
   date: 2021/6/11-14:11
-------------------------------------------------
"""

import unittest, HTMLTestRunnerNew
from autotest02.comms.constants import CASE_DIR, REPORT_FILE

# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案例，添加在测试套件中)
suite = unittest.TestSuite()

# 2.3 添加整个目录下的测试类到测试套件，注意测试类必须以test开头
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

# 2.4使用HTMLTestRunner运行测试案例，并且生成html类型的结果报告
with open(REPORT_FILE, 'wb') as fb:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fb,
                                              title='接口自动化测试报告',
                                              description='2021年06月17日,螃蟹在剥我的壳，笔记本在写我。漫天的我落在枫叶上雪花上。而你在想我。',
                                              tester="Lee")
    runner.run(suite)  # 运行测试用例
