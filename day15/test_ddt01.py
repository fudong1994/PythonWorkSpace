"""
-------------------------------------------------
   File Name:test_ddt01
   Author:Lee
   date: 2021/6/15-14:05
-------------------------------------------------
"""
"""
ddt 可以参数化测试数据,把不同的数据进行参数化,做到代码逻辑和测试数据分离
使用方法:
1.将测试类使用@ddt进行标记
2.将需要循环使用测试数据的测试方法,用@data进行标记
"""
import unittest
from ddt import ddt, data


# 不使用ddt测试add函数
def add(a, b):
    return a + b


# 不使用ddt、unittest第三方测试包进行测试  需要查看控制台的结果，比较累
# res1 = add(1, 2)
# print(res1)  # 3
#
# res2 = add(-1, -3)
# print(res2)  # -4


# 使用unittest进行测试，进行自动比对
# class TestDdt01(unittest.TestCase):
#
#     def test_add01(self):
#         res1 = add(1, 2)
#         self.assertEqual(3, res1)
#
#     def test_add02(self):
#         res2 = add(-1, -3)
#         self.assertEqual(-4, res2)


#
# if __name__ == "__main__":
#     unittest.main()

# 使用unittest框架进行测试的同时，有大量的重复性代码，所以我们需要把测试数据和测试逻辑进行分离，优化代码


cases = [{"param1": 1, "param2": 2, 'exp': 3},
         {"param1": 2, "param2": 2, 'exp': 4},
         {"param1": -1, "param2": -2, 'exp': -3},
         {"param1": 4, "param2": 20, 'exp': 24},
         {"param1": 0, "param2": -2, 'exp': -2},
         {"param1": 0, "param2": 2, 'exp': 2}]  # 如果测试多条数据，只需要在cases中添加数据就ok


@ddt
class TestDdt02(unittest.TestCase):
    @data(*cases)  # 代表该方法循环使用cases中的测试数据，cases有多少条，该方法执行多少次，*代表拆包
    def test_add(self, case):  # 拆包后的数据会循环赋值case，并且执行该方法
        res = add(case['param1'], case['param2'])
        self.assertEqual(case['exp'], res)


if __name__ == "__main__":
    unittest.main()
