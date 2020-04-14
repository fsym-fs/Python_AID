from flask import request, render_template
from flask import Response
from flask import jsonify
from app.my_models import Person
from app.my_models import *
import json
import hashlib
from app.users.m_token import make_token

# 1101-


def login_view():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
        pass
    else:
        pass


# 1201-
def register_view():
    if request.method == 'GET':
        return render_template('users/register.html')
    elif request.method == 'POST':
        usname = request.json.get('uname')
        this = request.json.get('this')
        print(usname, this)
        if this:
            old_user = Person.query.filter(Person.uname == usname).all()
            if old_user:
                pass
            print(old_user)
            return jsonify('dd')
            # old_name = old_user.uname
            # if old_name == uname:
            #     data = {'code': 1201, 'error': '用户名已存在!'}
            #     # data = json.dumps(data)
            #     return jsonify(data)
            #     # return Response(data, conten_type='application/json')
        else:
            pwd = request.json.get('pwd')
            if len(pwd) > 11:
                data = {'code': 1202, 'error': '用户名已存在!'}
                # data = json.dumps(data)
                # return Response(data, conten_type='application/json')
                return jsonify(data)
            elif pwd == '':
                data = {'code': 1203, 'error': '请正确输入密码!'}
                return jsonify(data)
            else:
                email = request.json.get('email')
                phone = request.json.get('phone')
                old_user = Person.query.filter_by(uname=uname).one()
                old_name = old_user.uname
                if old_name == uname:
                    data = {'code': 1201, 'error': '用户名已存在!'}
                    return jsonify(data)
                m = hashlib.md5()
                m.updata(pwd.encode())
                try:
                    pserson = Person(uname, pwd, phone, email=email)
                    db.session.add(pserson)
                    db.session.commit()
                except Exception as e:
                    print('----error----')
                    print(e)
                    data = {'code': 1201, 'error': '用户名已存在!'}
                    return jsonify(data)
                # token
                token = make_token(uname)
                data = {
                    'code': 200,
                    'uname': uname,
                    'data': {
                        'm_token': token,
                        'cart': 0
                    }
                }
                return jsonify(data)

    else:
        pass


def personal_view():
    if request.method == 'GET':
        return render_template('users/personal.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def cart_view():
    if request.method == 'GET':
        return render_template('users/cart.html')
    elif request.method == 'POST':
        pass
    else:
        pass
