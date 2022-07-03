"""
-------------------------------------------------
   File Name:public_api
   Author:Lee
   date: 2021/6/22-14:49
-------------------------------------------------
"""
from configparser import ConfigParser
from comms.constants import CONF_FILE
import requests


# 数据替换
def replace_data(my_dict, key, new_value):
    """
    :param my_dict: 需要替换的字符串类型的字典
    :param key: 需要替换的key
    :param new_value: 替换数据
    :return: 替换后的字符串类型的字典
    """
    try:
        my_data = eval(my_dict)
        my_data[key] = new_value
        return str(my_data)
    except Exception as e:
        print("替换数据失败！", e)


# 从ini文件读取数据
def get_ini_data(section, option):
    try:
        cnp = ConfigParser()
        cnp.read(CONF_FILE, encoding='utf-8')
        return cnp.get(section, option)
    except Exception as e:
        print("从ini文件读取测试数据失败！", e)


# 获取token值
def get_token():
    try:
        response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                                 data={"username": get_ini_data('user3', 'name'),
                                       "password": get_ini_data('user3', 'password'), "typeId": '101'})
        res = response.json()
        return res["token"]
    except Exception as e:
        print('获取token失败！', e)


if __name__ == "__main__":
    data = get_ini_data('user', 'name')
    print(data)
    print(get_token())
