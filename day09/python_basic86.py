"""
-------------------------------------------------
   File Name:python_basic86
   Author:Lee
   date: 2021/6/4-10:12
-------------------------------------------------
"""
"""
1.我们可以使用raise自己触发异常  raise [Exception[,args[,traceback]]]
2.自定义异常:
    实际的工程项目中，我们有时候需要定义一个区别于系统的异常类，还好python为我们提供了一个可以自己定义异常类的方法，我们来看下面的代码

"""


# num = int(input('请输入0-100的整数：'))
# if not 0 <= num <= 100:
#     raise Exception('输入无效的数字')  # 主动抛出异常
# elif 0 <= num < 60:
#     print('不及格')
# else:
#     print('及格')


# 自定义异常
class NotValidNumber(Exception):
    pass


num = int(input('请输入0-100的整数：'))
if not 0 <= num <= 100:
    raise NotValidNumber('用户输入了无效的数字！！')  # 主动抛出异常
elif 0 <= num < 60:
    print('不及格')
else:
    print('及格')








