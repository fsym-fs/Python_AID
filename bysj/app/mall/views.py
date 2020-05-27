from flask import request, render_template
# from flask import Response
from flask import jsonify
from app.my_models import *
# from aap.my_models import Good
from app.my_models import db
import time
# import json
import hashlib
from app.users.m_token import make_token


def index_view():
    if request.method == 'GET':
        goods = Good.query.filter(Good.is_active == True).all()
        news = (Good.query.filter(Good.is_active == True).order_by(Good.id.desc()).all())[:4]
        # print(goods)
        # print(goods02)
        goods = goods[-7:-1]
        goods_list = []
        news_list = []
        for i in goods:
            lis = {}
            lis['gid'] = i.g_id
            lis['name'] = i.name
            lis['price'] = i.price
            pic_obj = Good_pic.query.filter(Good_pic.gid == i.g_id).all()
            lis['pic'] = pic_obj[0].default_pic
            goods_list.append(lis)
        # print(goods_list)
        for i in news:
            lis = {}
            lis['gid'] = i.g_id
            lis['name'] = i.name
            lis['price'] = i.price
            pic_obj = Good_pic.query.filter(Good_pic.gid == i.g_id).all()
            lis['pic'] = pic_obj[0].default_pic
            news_list.append(lis)
        print(goods_list)
        return render_template('mall/index.html', goods_list=goods_list, news_list=news_list)


def all_view():
    if request.method == 'GET':
        # 每页3个，查询第2页的数据
        # ret = paginate(页码，每一页的数据量)
        try:
            page = int(request.args.get('page', 1))
            # print(page)
        except Exception as e:
            page = 1
        print('??', page)
        try:
            result = Good.query.filter(Good.is_active == True).paginate(page, 9)
            print('...', page)
        except Exception as e:
            print('-------')
            print(e)
            page = 1
            result = Good.query.filter(Good.is_active == True).paginate(page, 9)
        print(result.items)
        goods_list = []
        for i in result.items:
            lis = {}
            lis['gid'] = i.g_id
            lis['id'] = i.id
            lis['name'] = i.name
            lis['price'] = i.price
            pic_obj = Good_pic.query.filter(Good_pic.gid == i.g_id).all()
            # print(pic_obj)
            lis['pic'] = pic_obj[0].default_pic
            goods_list.append(lis)
        print(goods_list)
        return render_template('mall/allgoods.html', goods_list=goods_list, page=page)
    elif request.method == 'POST':
        # 每页3个，查询第2页的数据
        # ret = paginate(页码，每一页的数据量)
        try:
            page = int(request.form.get('page', 1))
            # print(page)
        except Exception as e:
            page = 1
        print(page)
        return jsonify({'code': 200, 'page': page})


def single_view():
    if request.method == 'GET':
        try:
            gid = request.args.get('gid')
            print(gid)
        except Exception as e:
            print('--------------')
            print(e)
            gid = 1
        print(555)
        good_obj = Good.query.filter(Good.g_id == gid).all()
        print('666')
        if not good_obj:
            print('--------------')
            good_obj = Good.query.filter(Good.g_id == 1).all()
        print(good_obj)
        lis = {}
        com = Comments.query.filter(Comments.gid == gid).all()
        print(len(com))
        com_len = len(com)
        lis['name'] = good_obj[0].name
        lis['gid'] = good_obj[0].g_id
        lis['title'] = good_obj[0].title
        lis['price'] = good_obj[0].price
        lis['inventory'] = good_obj[0].inventory
        lis['weight'] = good_obj[0].weight
        lis['loc'] = good_obj[0].loc
        pic_obj = Good_pic.query.filter(Good_pic.gid == good_obj[0].g_id).all()
        lis['pic'] = pic_obj[0].default_pic
        print(lis)
        return render_template('mall/single.html', lis=lis,com_len = com_len)
    elif request.method == 'POST':
        uname = request.json.get('uname')
        gid = request.json.get('gid')
        num = request.json.get('num')
        print(uname, gid, num)
        try:
            user = Person.query.filter(Person.uname == uname).first()
            uid = user.id
            good = Good.query.filter(Good.g_id == gid).first()
            old_cart = Cart.query.filter(Cart.uid == uid, Cart.gid == gid).first()
            if old_cart:
                cart = old_cart
                num = cart.number + num
            else:
                cart = Cart()
                db.session.add(cart)
                db.session.commit()
            if num <= good.inventory:
                cart.number = num
                # db.session.commit()
            else:
                cart.number = good.inventory
            cart.uid = uid
            cart.gid = gid
            # good.inventory = good.inventory - cart.number
            db.session.commit()
        except Exception as e:
            print('-----------------------------')
            print(e)
            return jsonify({'code': 5001})
        return jsonify({'code': 200})
    else:
        pass


def add_content_view():
    if request.method == 'GET':
        uname = request.args.get('uname')
        gid = request.args.get('gid')
        size = request.args.get('size')
        datas = []
        try:
            result = Comments.query.filter(Comments.gid == gid).paginate(size, 10)
        except Exception as e:
            # try:
            #     result = Comments.query.filter(Comments.gid == gid).paginate(1, 10)
            # except Exception as e:
            print('------------')
            print(e)
            return jsonify({"code": 201, "data": "当前已经没有数据了!"})
        # print(result.items)
        i = 1
        for items in result.items:
            dic = {}
            uid = items.uid
            user = Person.query.filter(Person.id == uid).first()
            dic['num'] = i
            dic['username'] = user.uname
            dic['time'] = items.create_at
            dic['content'] = items.message
            # print(items.message)
            datas.append(dic)
            i += 1
        print(datas)
        return jsonify({"code": 200, "datas": datas})
    elif request.method == 'POST':
        uname = request.json.get('username')
        content = request.json.get('content')
        gid = request.json.get('gid')
        print(uname,gid,content)
        time01 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        try:
            user = Person.query.filter(Person.uname == uname).first()
            uid = user.id
            comm = Comments()
            db.session.add(comm)
            comm.uid = uid
            comm.gid = gid
            comm.message = content
            comm.create_at = time01
            db.session.commit()
        except Exception as e:
            return jsonify({'code': 201, 'error': '服务器正忙,请稍后再试!'})
        return jsonify({"cdoe": 200, "msg": "内容发布完成!"})
        # print(time01)
        # return '555'
