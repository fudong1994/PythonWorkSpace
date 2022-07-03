"""
-------------------------------------------------
   File Name:python_senior11
   Author:Lee
   date: 2021/6/9-10:36
-------------------------------------------------
"""
"""
flask框架介绍：该框架为后端服务框架，能够部署服务，这样我们的接口/代码就能够使用http协议来调用
"""

# 第一步:通过pip install 导入该库
import flask
from day11.db_utils03 import DBUtils

# 第二步：创建app对象，把当前的python文件当成一个服务，__name__代表当前的python文件
app = flask.Flask(__name__)


# 第三步：将我们接口发布成服务，route是路由的意思
# @app.route('/login', methods=['get', 'post'])
# def login():
#     return 'hello world'


# 第三步：将我们接口发布成服务，route是路由的意思
# @app.route('/user_login', methods=['get', 'post'])
# def login():
#     data = flask.request.values  # 接收请求发送过来的数据
#     print(data)  # CombinedMultiDict([ImmutableMultiDict([('username', "'xiaohua'"), ('password', "'a123456'")])])
#     uname = data.get('username')  # 获取请求中的username对应的值
#     pwd = data.get('password')  # 获取请求中的password对应的值
#     if len(uname) == 0:
#         return {"code": 1001, "msg": "用户名不能为空"}
#     elif len(pwd) == 0:
#         return {"code": 1002, "msg": "密码不能为空"}
#     elif uname == 'xiaohua' and pwd == 'a123456':
#         return {"code": 9999, "msg": "登录成功"}
#     else:
#         return {"code": 1003, "msg": "用户名或密码错误"}


# 第三步：将我们接口发布成服务，route是路由的意思,methods用来指定接口访问方式
@app.route('/user_login', methods=['get', 'post'])
def login():
    data = flask.request.values  # 接收请求发送过来的数据
    print(data)  # CombinedMultiDict([ImmutableMultiDict([('username', "'xiaohua'"), ('password', "'a123456'")])])
    uname = data.get('username')  # 获取请求中的username对应的值
    pwd = data.get('password')  # 获取请求中的password对应的值

    if len(uname) == 0:
        return {"code": 1001, "msg": "用户名不能为空"}
    elif len(pwd) == 0:
        return {"code": 1002, "msg": "密码不能为空"}
    # 查询数据库，看看当前传入的用户名密码在数据库中是否存在
    else:
        db = DBUtils()
        # 从数据库里查询用户名等于 接口传入的用户名 并且密码等于 从接口传入的密码
        count = db.find_count('select * from tb_user where name = %s and passwd = %s', (uname, pwd))
        db.close()
        print(count)
        if count == 0:
            return {"code": 1003, "msg": "用户名或密码错误"}
        else:
            return {"code": 9999, "msg": "登录成功"}


if __name__ == '__main__':
    app.run(debug=True)  # 启动服务(使用debug模式启动服务，debug是可调式模式)
