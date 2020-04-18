from flask import request, render_template
# from flask import Response
from flask import jsonify
from app.my_models import Person
from app.my_models import db
# import json
import hashlib
from app.users.m_token import make_token


# 2101-
def admin_login_view():
    if request.method == 'GET':
        return render_template('admin/login.html')
    elif request.method == 'POST':
        uname = request.json.get('uname')
        pwd = request.json.get('pwd')
        if uname == 'tom' and pwd == 'tom123':
            data = {'code': 200, 'data': {'uname': uname}}
            return jsonify(data)
        else:
            return jsonify({'code': 2101, 'error': '用户名或密码错误!'})
    else:
        pass

def admin_index_view():
    if request.method == 'GET':
        return render_template('admin/index.html')
    elif request.method == 'POST':
        pass
    else:
        pass

def admin_home_view():
    if request.method == 'GET':
        return render_template('admin/views/console.html')
    elif request.method == 'POST':
        pass
    else:
        pass