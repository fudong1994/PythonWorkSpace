"""
-------------------------------------------------
   File Name:logger02
   Author:Lee
   date: 2021/6/16-17:29
-------------------------------------------------
"""
from day16.log_study.log_utils import logger

# # 实际意义上的应用
try:
    num = input('请输入除数：')
    res = 20 / int(num)
except Exception as e:
    logger.error('该方法报异常！！')  # 记录错误信息到文件中
    logger.exception(e)
else:
    logger.info('该方法正常!')  # 记录重要方法运行信息到文件
