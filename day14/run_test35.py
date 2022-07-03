"""
-------------------------------------------------
   File Name:run_test35
   Author:Lee
   date: 2021/6/11-14:11
-------------------------------------------------
"""
"""
HTML类型的结果报告
# 1、下载HTMLTestRunner文件，存放到python安装目录下的Lib下
# 2、在代码中 import该模块
"""
import unittest, HTMLTestRunnerNew

# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案例，添加在测试套件中)
suite = unittest.TestSuite()

# 2.3 添加整个目录下的测试类到测试套件，注意测试类必须以test开头
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'D:\Tools\PythonWorkSpace\day14'))

# 2.4使用HTMLTestRunner运行测试案例，并且生成html类型的结果报告
with open(r'./report.html', 'wb') as fb:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=fb,
                                              title='登录接口测试报告',
                                              description='系统登录测试用例执行',
                                              tester="Lee")
    runner.run(suite)  # 运行测试用例
