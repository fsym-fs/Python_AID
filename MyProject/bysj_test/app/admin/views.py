from flask import request, render_template
from flask import jsonify
from app.my_models import Person
from app.my_models import Good
from app.my_models import Good_pic
from app.my_models import db
from app import config


# import json


# 2101-
def admin_login_view():
    if request.method == 'GET':
        return render_template('admin/login.html')
    elif request.method == 'POST':
        uname = request.json.get('uname')
        pwd = request.json.get('pwd')
        if uname == 'admin' and pwd == 'admin':
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
        # this = request.args.get('this')
        # print(this)
        users = Person.query.all()
        # online_user = Person.query.filter(is_online==True)
        # online_user_count = len(online_user)
        goods = Good.query.all()
        goods_count = len(goods)
        # print(users)
        users_count = len(users)
        return render_template('admin/views/console.html',
                               users_count=users_count, goods_count=goods_count)
    elif request.method == 'POST':
        pass
    else:
        pass


def admin_user_home_view():
    if request.method == 'GET':
        return render_template('admin/views/user.html')
    elif request.method == 'POST':
        this = request.json.get('this')
        # print(this)
        users = Person.query.filter(Person.is_active == True)
        # print(users)
        data = []
        for user in users:
            user_data = {}
            user_data['id'] = user.id
            user_data['username'] = user.uname
            user_data['email'] = user.email
            user_data['sign'] = user.signature
            user_data['phone'] = user.phone
            user_data['address'] = user.address
            if user.is_active:
                user_data['is_active'] = '已激活'
            else:
                user_data['is_active'] = '未激活'
            data.append(user_data)

        # return data
        # return Response(data)
        data = {
            "code": 0,
            "msg": "",
            "count": len(data),
            "data": data,
        }
        return jsonify(data)
    elif request.method == 'DELETE':
        uname = request.json.get('username')
        print(uname)
        try:
            user = Person.query.filter(Person.uname == uname)
            if user:
                user[0].is_active = False
            else:
                return jsonify({'code': 2001, 'error': '未查询到该用户!'})
        except Exception as e:
            return jsonify({'code': 2002, 'error': '未查询到该用户!'})
        return jsonify({'code': 200})


# 1001-
def admin_user_form_view():
    if request.method == 'GET':
        return render_template('admin/views/form.html')
    elif request.method == 'POST':
        uname = request.json.get('name')
        pwd = request.json.get('pwd')
        email = request.json.get('email')
        address = request.json.get('address')
        phone = request.json.get('phone')
        sign = request.json.get('sign')
        old_user = Person.query.filter(Person.uname == uname).all()
        if old_user:
            data = {'code': 1001, 'error': '用户名已重复!'}
        try:
            pserson = Person(uname=uname, pwd=pwd, phone=phone, email=email)
            db.session.add(pserson)
            user = Person.query.filter(Person.uname == uname).all()
            user[0].address = address
            user[0].sign = sign
            db.session.commit()
        except Exception as e:
            print('----error----')
            print(e)
            data = {'code': 1002, 'error': '用户名已存在!'}
            return jsonify(data)
        return jsonify({'code': 200})
    else:
        pass


# 3101-
def admin_goods_home_view():
    if request.method == 'GET':
        return render_template('admin/views/goods.html')
    elif request.method == 'POST':
        goods = Good.query.filter(Good.is_active == True)
        # print(users)
        data = []
        for good in goods:
            good_data = {}
            good_data['gid'] = good.g_id
            good_data['name'] = good.name
            good_data['price'] = str(good.price)
            good_data['title'] = good.title
            good_data['weight'] = good.weight
            good_data['loc'] = good.loc
            good_data['inventory'] = good.inventory
            if good.is_active:
                good_data['is_active'] = '已激活'
            else:
                good_data['is_active'] = '未激活'
            data.append(good_data)

        # return data
        # return Response(data)
        data = {
            "code": 0,
            "msg": "",
            "count": len(data),
            "data": data,
        }
        return jsonify(data)
    elif request.method == 'DELETE':
        gid = request.json.get('g_id')
        print(gid)
        try:
            good = Good.query.filter(Good.g_id == gid)
            if good:
                good[0].is_active = False
            else:
                return jsonify({'code': 2001, 'error': '未查询到该商品!'})
        except Exception as e:
            return jsonify({'code': 2002, 'error': '未查询到该商品!'})
        return jsonify({'code': 200})


# 4101-
def admin_goods_form_view():
    if request.method == 'GET':
        print(56)
        return render_template('admin/views/goods_form.html')
    elif request.method == 'POST':
        print('222')
        name = request.form.get('name')
        title = request.form.get('title')
        g_id = request.form.get('g_id')
        price = request.form.get('price')
        inventory = request.form.get('inventory')
        weight = request.form.get('weight')
        loc = request.form.get('loc')
        image = request.files.get('image')
        old_good = Good.query.filter(Good.g_id == g_id).all()
        if old_good:
            print(1)
            data = {'code': 1001, 'error': '该商品已存在!'}
            return jsonify(data)
        try:
            good = Good(name=name)
            db.session.add(good)
            this_good = Good.query.filter(Good.name == name).all()
            this_good[0].title = title
            this_good[0].g_id = g_id
            this_good[0].price = price
            this_good[0].inventory = inventory
            this_good[0].weight = weight
            this_good[0].loc = loc
            good_pic = Good_pic()
            db.session.add(good_pic)
            good_pic.gid = g_id
            good_pic.default_pic = str(g_id) + '.jpg'
            filename = config.basepath + '/static/goods_pic/' + str(g_id) + '.jpg'
            db.session.commit()
        except Exception as e:
            print('----error----')
            print(e)
            data = {'code': 1002, 'error': '该商品已存在!'}
            return jsonify(data)
        with open(filename,'wb') as f:
            f.write(image.read())
        print(3)
        # data = {'code': 1002, 'error': '该商品已存在!'}
        return jsonify({'code':200})
    else:
        pass

