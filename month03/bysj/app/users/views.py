from flask import request, render_template
# from flask import Response
from flask import jsonify
from app.my_models import Person
from app.my_models import db
# import json
import hashlib
from app.users.m_token import make_token


# 1101-
def login_view():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
        # 'uname':$('#l_uname').val(),
        # 'pwd':$('#pwd').val(),
        uname = request.json.get('uname')
        pwd = request.json.get('pwd')
        old_user = Person.query.filter(Person.uname == uname,
                                       Person.pwd == pwd).all()
        if old_user:
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
        data = {'code': 1101, 'error': '用户名或密码错误!'}
        return jsonify(data)
    else:
        pass


# 1201-
def register_view():
    if request.method == 'GET':
        return render_template('users/register.html')
    elif request.method == 'POST':
        usname = request.json.get('uname')
        this = request.json.get('this')
        # print(usname, this)
        if this:
            old_user = Person.query.filter(Person.uname == usname).all()
            if old_user:
                data = {'code': 1201, 'error': '用户名已存在!'}
                return jsonify(data)
            data = {'code': 200}
            return jsonify(data)
        else:
            # print('556')
            pwd = request.json.get('pwd')
            if len(pwd) > 11:
                data = {'code': 1202, 'error': '您输入的密码大于11位!'}
                # data = json.dumps(data)
                # return Response(data, conten_type='application/json')
                return jsonify(data)
            elif pwd == '':
                data = {'code': 1203, 'error': '请正确输入密码!'}
                return jsonify(data)
            else:
                email = request.json.get('email')
                phone = request.json.get('phone')
                old_user = Person.query.filter(Person.uname == usname).all()
                if old_user:
                    data = {'code': 1201, 'error': '用户名已存在!'}
                    return jsonify(data)
                m = hashlib.md5()
                m.update(pwd.encode())
                try:
                    pserson = Person(uname=usname,
                                     pwd=pwd,
                                     phone=phone,
                                     email=email)
                    db.session.add(pserson)
                    db.session.commit()
                except Exception as e:
                    print('----error----')
                    print(e)
                    data = {'code': 1201, 'error': '用户名已存在!'}
                    return jsonify(data)
                # token
                token = make_token(usname)
                data = {
                    'code': 200,
                    'uname': usname,
                    'data': {
                        'm_token': token,
                        'cart': 0
                    }
                }
                # print(token)
                return jsonify(data)

    else:
        pass


# 1301-
def personal_view():
    if request.method == 'GET':
        return render_template('users/personal.html')
    elif request.method == 'POST':
        this = request.json.get('this')
        uname = request.json.get('uname')
        if this:
            try:
                user = Person.query.filter(Person.uname == uname).all()
                data = {
                    'code': 200,
                    'email': user[0].email,
                    'phone': user[0].phone,
                    'pwd': user[0].pwd
                }
                return jsonify(data)
            except Exception as e:
                return jsonify({'code': 1301, 'error': '身份验证失败,请重新登录!'})
        else:
            try:
                old_name = request.json.get('old_name')
                user = Person.query.filter(Person.uname == old_name).all()
                pwd01 = request.json.get('pwd01')
                if pwd01 == user[0].pwd:
                    # pwd02 = request.json.get('pwd02')
                    user[0].uname = request.json.get('uname')
                    user[0].pwd = request.json.get('pwd02')
                    user[0].email = request.json.get('email')
                    user[0].phone = request.json.get('phone')
                    db.session.commit()
                else:
                    return jsonify({'code': 1302, 'error': '您的原始密码输入错误!'})
            except Exception as e:
                print('--------------')
                print(e)
                return jsonify({'code': 1303, 'error': '用户名已重复，请重新输入!'})
            token = make_token(request.json.get('uname'))
            return jsonify({
                'code': 200,
                'data': {
                    'token': token,
                    'uname': request.json.get('uname'),
                },
            })
    else:
        pass


def cart_view():
    if request.method == 'GET':
        return render_template('users/cart.html')
    elif request.method == 'POST':
        pass
    else:
        pass
