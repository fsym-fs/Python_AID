from flask import request, render_template
from flask import jsonify
from app.my_models import Person
from app.users.m_token import de_token
import time


# 1001-
def public_view():
    if request.method == 'GET':
        return render_template('public_html.html')
    elif request.method == 'POST':
        uname = request.json.get('uname')
        token = request.json.get('token')
        now = time.time()
        d_token = de_token(token)
        d_uname = d_token.get('username')
        exp = d_token.get('exp')
        if exp > now and d_uname == uname:
            data = {'code': 200}
            return jsonify(data)
        else:
            data = {'code': 1001, 'error': '身份验证失败!'}
            return jsonify(data)


def index_view():
    return render_template('mall/index.html')


# def login_view():
#     return render_template('users/login.html')
#
#
# def register_view():
#     if request.method == 'GET':
#         return render_template('users/register.html')
#     elif request.method == 'POST':
#         pass
#     else:
#         pass

# def personal_view():
#     if request.method == 'GET':
#         return render_template('users/personal.html')
#     elif request.method == 'POST':
#         pass
#     else:
#         pass


def about_view():
    if request.method == 'GET':
        return render_template('mall/about.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def single_view():
    if request.method == 'GET':
        return render_template('mall/single.html')
    elif request.method == 'POST':
        pass
    else:
        pass


# def cart_view():
#     if request.method == 'GET':
#         return render_template('users/cart.html')
#     elif request.method == 'POST':
#         pass
#     else:
#         pass


def test_view():
    if request.method == 'GET':
        return render_template('mall/test.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def pa_view():
    per = Person.query.all()
    return "<br>".join(["{0}: {1}".format(p.uname, p.pwd) for p in per])


# def users_view():
#     users = User.query.all()
#     print(users)
#     return "<br>".join(["{0}: {1}".format(user.uname, user.email) for user in users])

# def user_view(id):
#     user = User.query.filter_by(id=id).one()
#     return "{0}: {1}".format(user.uname, user.email)
