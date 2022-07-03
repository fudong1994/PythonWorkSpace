"""
-------------------------------------------------
   File Name:log_utils
   Author:Lee
   date: 2021/6/16-17:25
-------------------------------------------------
"""
"""
log工具类
"""

# 第一步：导入logging
import logging


def get_logger():
    # 第二步：创建日志对象
    logger = logging.getLogger('logging')
    logger.setLevel('DEBUG')  # 设置默认的日志级别

    # 第三步：设置输出方向

    # 输出到控制，并且级别INFO，代表把info级别及以后的内容打印控制台
    sh1 = logging.StreamHandler()
    sh1.setLevel("INFO")  # 输出info及info以上级别的内容

    # 输出到 ./info.log 文件，并且内容为追加写入，级别INFO设置为INFO及以后的内容
    sh2 = logging.FileHandler(filename=r'D:\Tools\PythonWorkSpace\autotest01\logs\info.log', mode='a', encoding='utf-8')
    sh2.setLevel("INFO")

    # 输出 ./error.log文件，并且内容为追加写入，级别error设置为error及以后的内容
    sh3 = logging.FileHandler(filename=r'D:\Tools\PythonWorkSpace\autotest01\logs\error.log', mode='a', encoding='utf-8')
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

    return logger


logger = get_logger()
