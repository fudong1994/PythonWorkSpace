"""
-------------------------------------------------
   File Name:python_senior12
   Author:Lee
   date: 2021/6/9-14:24
-------------------------------------------------
"""
import flask, json
from autotest02.comms.db_utils import DBUtils

app = flask.Flask(__name__)


@app.route('/login', methods=['get', 'post'])
def login():
    data = flask.request.values  # 接收请求发送过来的数据
    print(data)  # CombinedMultiDict([ImmutableMultiDict([('username', "'xiaohua'"), ('password', "'a123456'")])])
    uname = data.get('username')  # 获取请求中的username对应的值
    pwd = data.get('password')  # 获取请求中的password对应的值

    if len(uname) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(pwd) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    # 查询数据库，看看当前传入的用户名密码在数据库中是否存在
    else:
        db = DBUtils()
        # 从数据库里查询用户名等于 接口传入的用户名 并且密码等于 从接口传入的密码
        count = db.find_count('select * from tb_user where name = %s and passwd = %s', (uname, pwd))
        db.close()
        print(count)
        if count == 0:
            return json.dumps({"code": 1003, "msg": "用户名或密码错误"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 9999, "msg": "登录成功"}, ensure_ascii=False)


# 注册接口
@app.route('/register', methods=['get', 'post'])
def register():
    data = flask.request.values
    username = data.get('username')
    password = data.get('password')
    re_password = data.get('re_password')
    email = data.get('email')
    phone = data.get('phone')

    print('传入username的值:', username, '传入的password的值：', password, '传入的re_password的值:', re_password)
    if len(username) == 0:
        return json.dumps({"code": 1001, "msg": "用户名不能为空"}, ensure_ascii=False)
    elif len(password) == 0:
        return json.dumps({"code": 1002, "msg": "密码不能为空"}, ensure_ascii=False)
    elif len(re_password) == 0:
        return json.dumps({"code": 1003, "msg": "确认密码不能为空"}, ensure_ascii=False)
    elif not (6 <= len(username) <= 18 and 6 <= len(password) <= 18):
        return json.dumps({"code": 1004, "msg": "用户名和密码必须在6-18位之间"}, ensure_ascii=False)
    elif password != re_password:
        return json.dumps({"code": 1005, "msg": "确认密码必须和密码输入一致"}, ensure_ascii=False)
    elif len(email) == 0:
        return json.dumps({"code": 1006, "msg": "邮箱不能为空"}, ensure_ascii=False)
    elif len(phone) == 0:
        return json.dumps({"code": 1007, "msg": "手机号不能为空"}, ensure_ascii=False)
    db = DBUtils()
    count = db.find_count('select * from tb_user where name = %s', (username,))
    count1 = db.find_count('select * from tb_user where phone = %s;', (phone,))
    if count1 != 0 and count == 0:
        db.close()
        return json.dumps({"code": 1009, "msg": "手机号已被注册"}, ensure_ascii=False)
    if count != 0:
        db.close()
        return json.dumps({"code": 1008, "msg": "用户名已存在"}, ensure_ascii=False)
    else:
        count = db.cud('insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s);',
                       (username, password, email, phone))
        db.close()
        if count == 1:
            return json.dumps({"code": 9999, "msg": "注册成功！"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 0000, "msg": "插入数据失败"}, ensure_ascii=False)


app.run(debug=True)
