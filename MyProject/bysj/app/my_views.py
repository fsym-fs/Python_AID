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
        # print(token)
        try:
            d_token = de_token(token.encode())
            # print(d_token)
        except Exception as e:
            data = {'code': 1001, 'error': '身份验证失败!'}
            return jsonify(data)
        d_uname = d_token.get('username')
        exp = d_token.get('exp')
        if exp > now and d_uname == uname:
            data = {'code': 200}
            return jsonify(data)
        else:
            data = {'code': 1002, 'error': '身份验证失败!'}
            return jsonify(data)


def about_view():
    if request.method == 'GET':
        return render_template('mall/about.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def pa_view():
    per = Person.query.all()
    return "<br>".join(["{0}: {1}".format(p.uname, p.pwd) for p in per])
