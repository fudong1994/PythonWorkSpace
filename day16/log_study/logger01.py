"""
-------------------------------------------------
   File Name:logger01
   Author:Lee
   date: 2021/6/16-15:29
-------------------------------------------------
"""

"""
log/日志：用来记录软件运行的轨迹。我们可以把需要记录的内容记录在文件中，方便以后查看
日志的级别：
debug:记录详细信息，主要用来调试
info:记录正确情况下，重要的日志
warning:记录告警信息
error:记录错误信息
"""

# 第一步：导入logging
import logging

# 第二步：创建日志对象
logger = logging.getLogger('logging')
logger.setLevel('DEBUG')  # 设置默认的日志级别

# 第三步：设置输出方向

# 输出到控制，并且级别INFO，代表把info级别及以后的内容打印控制台
sh1 = logging.StreamHandler()
sh1.setLevel("INFO")  # 输出info及info以上级别的内容

# 输出到 ./info.log 文件，并且内容为追加写入，级别INFO设置为INFO及以后的内容
sh2 = logging.FileHandler(filename='./info.log', mode='a', encoding='utf-8')
sh2.setLevel("INFO")

# 输出 ./error.log文件，并且内容为追加写入，级别error设置为error及以后的内容
sh3 = logging.FileHandler(filename='./error.log', mode='a', encoding='utf-8')
sh3.setLevel("ERROR")

# 第四步：添加输出方向到logger对象
logger.addHandler(sh1)
logger.addHandler(sh2)
logger.addHandler(sh3)

# 第五步：指定日志的输出格式
fmt_str = '%(asctime)s - [%(filename)s -->line:%(lineno)d] - %(levelname)s:%(message)s'
my_fmt = logging.Formatter(fmt_str)  # 设置样式
sh1.setFormatter(my_fmt)  # 把样式添加到输出方向中
sh2.setFormatter(my_fmt)
sh3.setFormatter(my_fmt)

# 第六步：如何使用
logger.debug('debug级别的信息')  # 代表我需要在此处记录debug级别的信息
logger.info('info级别的信息')  # 代表我需要在此处记录info级别的信息
logger.warning('warning级别的信息')
logger.error('error级别的信息')

# # 实际意义上的应用
try:
    num = input('请输入除数：')
    res = 20 / int(num)
except Exception as e:
    logger.error('该方法报异常！！')  # 记录错误信息到文件中
    logger.exception(e)
else:
    logger.info('该方法正常!')  # 记录重要方法运行信息到文件
