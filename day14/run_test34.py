"""
-------------------------------------------------
   File Name:run_test34
   Author:Lee
   date: 2021/6/11-10:43
-------------------------------------------------
"""
import unittest
from day14.test_login32 import LoginTest

"""
使用测试套件管理和运行测试用例
好处：
1、可以自由的执行多个模块的测试类
2、可以配置图形化的结果报告
"""

# 1、创建测试套件(测试套件的作用：我们可以把需要运行的测试案例，添加在测试套件中)
suite = unittest.TestSuite()

# 2、将测试用例添加到测试套件
# 2.1 添加测试方法到测试套件
# suite.addTest(LoginTest('test_login02'))   # 把LoginTest类下的 test_login02方法加入到测试套件中
# suite.addTest(LoginTest('test_login03'))

# 2.2 添加整个测试类到测试套件
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(LoginTest))  # 加载整个测试类到测试套件

# 2.3 添加整个目录下的测试类到测试套件，注意测试类必须以test开头
loader = unittest.TestLoader()
suite.addTest(loader.discover(r'D:\Tools\PythonWorkSpace\day14'))

# 3、获取runner对象，并且调用run方法运行测试案例
runner = unittest.TextTestRunner()
runner.run(suite)  # 通过unittest的runner对象运行测试套件

