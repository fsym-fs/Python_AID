from flask import request, render_template
# from flask import Response
from flask import jsonify
from app.my_models import Person
from app.my_models import *
from app.my_models import db
import base64
# import json
import hashlib
import time
from app.users.m_token import make_token
from .pay import *

basepath = os.path.dirname(__file__)


# 1101-
def login_view():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
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
                    'm_token': token.decode(),
                    'cart': 0
                }
            }
            return jsonify(data)
        data = {'code': 1101, 'error': '用户名或密码错误!'}
        return jsonify(data)


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
                # m = hashlib.md5()
                # m.update(pwd.encode())
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
                        'm_token': token.decode(),
                        'cart': 0
                    }
                }
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
                # print('5556')
                # print(user[0].email)
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
                    'token': token.decode(),
                    'uname': request.json.get('uname'),
                },
            })
    else:
        pass


def cart_view():
    if request.method == 'GET':
        uname = request.args.get('uname')
        result = 0
        try:
            request_data = {k: request.args[k] for k in request.args.keys()}
            del request_data['uname']
            # print(request_data)
            alipay_view(request_data)
        except Exception as e:
            pass
        if uname:
            carts_list = []
            try:
                User = Person.query.filter(Person.uname == uname).all()
                # print('hhh')
                uid = User[0].id
                # print('id:', uid)
                carts = Cart.query.filter(Cart.uid == uid).all()
                # print(carts)
                # print(len(carts))
                count = len(carts)
                for item in carts:
                    dic = {}
                    good = Good.query.filter(Good.g_id == item.gid).first()
                    dic['gid'] = good.g_id
                    dic['name'] = good.name
                    dic['price'] = good.price
                    good_pic = Good_pic.query.filter(
                        Good_pic.gid == item.gid).first()
                    dic['pic'] = good_pic.default_pic
                    dic['num'] = item.number
                    dic['all_price'] = int(item.number) * good.price
                    result += dic['all_price']
                    carts_list.append(dic)
                # print(carts_list)
                # print(carts)
                return render_template('users/cart.html',
                                       carts=carts_list,
                                       result=result,
                                       count=count)
            except Exception as e:
                print('----------------')
                print(e)
        return render_template('users/cart.html')
    elif request.method == 'DELETE':
        print('delete')
        uname = request.json.get('uname')
        gid = request.json.get('gid')
        gid_lis = request.json.get('gid_lis')
        print(uname, gid)
        print(gid_lis)
        if uname and gid:
            try:
                user = Person.query.filter(Person.uname == uname).first()
                uid = user.id
                cart = Cart.query.filter(Cart.uid == uid,
                                         Cart.gid == gid).first()
                print(cart)
                db.session.delete(cart)
                db.session.commit()
                data = {'code': 200}
                return jsonify(data)
            except Exception as e:
                print('----------------------')
                print(e)
                data = {'code': 1401, 'error': '服务器正忙,请稍后再试!'}
                # print()
                return jsonify(data)
        elif uname and gid_lis:
            try:
                user = Person.query.filter(Person.uname == uname).first()
                uid = user.id
                for i in gid_lis:
                    cart = Cart.query.filter(Cart.uid == uid,
                                             Cart.gid == i).first()
                    print(cart)
                    db.session.delete(cart)
                db.session.commit()
                data = {'code': 200}
                return jsonify(data)
            except Exception as e:
                print('----------------------')
                print(e)
                data = {'code': 1401, 'error': '服务器正忙,请稍后再试!'}
                return jsonify(data)
        else:
            return jsonify({'code': 14003})


def encode_oid(o_str):
    s = o_str.encode()
    b_s = base64.b64encode(s)
    ss = base64.b64decode(b_s)
    return b_s.decode()


def decode_oid(o_id):
    ss = base64.b64decode(o_id)
    return ss


# gid_uid_time
def paying_view():
    if request.method == 'GET':
        uname = request.args.get('uname')
        gid_str = request.args.get('gid_str')
        print(uname, gid_str)
        oid = ''
        # User = Person.query.filter(Person.uname == uname).first()
        # uid = User.id
        carts_list = []
        result = 0
        all_num = 0
        if uname and gid_str:
            now = int(time.time())
            oid = encode_oid(gid_str +'_'+ str(now))
            print(oid)
            try:
                User = Person.query.filter(Person.uname == uname).all()
                # print('hhh')
                uid = User[0].id
                print('id:', uid)
                gid_lis = gid_str.split('_')
                print(gid_lis)
                gid_lis = gid_lis[:-1]
                print(gid_lis)
                for item in gid_lis:
                    dic = {}
                    gid = int(item)
                    print(gid)
                    cart = Cart.query.filter(Cart.uid == uid, Cart.gid == gid).first()
                    print(cart)
                    print(cart.number)
                    dic['num'] = cart.number
                    dic['gid'] = cart.gid
                    good = Good.query.filter(Good.g_id == item).first()
                    dic['name'] = good.name
                    dic['price'] = good.price
                    good_pic = Good_pic.query.filter(Good_pic.gid == item).first()
                    dic['pic'] = good_pic.default_pic
                    dic['account'] = int(cart.number) * good.price
                    result += int(cart.number) * good.price
                    all_num += cart.number
                    carts_list.append(dic)
                print(carts_list)
            except Exception as e:
                print('----------------')
                print(e)
        return render_template('users/paying.html',
                               carts_list=carts_list, result=result, all_num=all_num, oid=oid, usname=uname)
    elif request.method == 'POST':
        oid = request.json.get('oid')
        result = request.json.get('result')
        uname = request.json.get('uname')
        print(oid, result, uname)
        ALIPAY_RETURN_URL = 'http://127.0.0.1:5000/cart?uname=' + uname
        ALIPAY_NOTIFY_URL = 'http://127.0.0.1:5000/cart?uname=' + uname
        url = get_trade_url(oid, result, ALIPAY_RETURN_URL, ALIPAY_NOTIFY_URL)
        print(url)
        return jsonify({'code': 200, 'pay_url': url})


# gid_gid_...._uid_time
def order_view():
    if request.method == 'GET':
        uname = request.args.get('uname')
        page = request.args.get('page')
        print(uname, page)
        lis = []
        if not page:
            page = 1
        try:
            user = Person.query.filter(Person.uname == uname).first()
            uid = user.id
            print(uid)
            try:
                order_list = Order.query.filter(Order.uid == uid).paginate(page, 6)
            except Exception as e:
                page = 1
                order_list = Order.query.filter(Order.uid == uid).paginate(page, 6)
            # print(order_list)
            # 返回当前页数
            # print(order_list.page)
            # 判断是否有下一页
            # print(order_list.has_next)
            # print(order_list.total)
            # print(order_list.count)
            for item in order_list.items:
                dic = {}
                dic['oid'] = item.o_id
                dic['name'] = item.name
                dic['phone'] = item.phone
                dic['address'] = item.address
                dic['account'] = item.account
                print('11')
                print(item.name)
                lis.append(dic)
        except Exception as e:
            pass
        print(lis)
        return render_template('users/order.html', lis=lis, page=page)


def alipay_view(request_data):
    result = 0
    # if request.method == 'GET':
    # request_data = {k: request.args[k] for k in request.args.keys()}
    """
    
    {
    'charset': 'utf-8', 'out_trade_no': 'MTAwMDVfdG9tMTU4ODQ3NTAwMw==', 
    'method': 'alipay.trade.page.pay.return', 
    'total_amount': '36.00', 
    'sign': 'WHBqq8VhVYsOS+ujzxXFkS6+B3XKE7vSD6Q45D3UGpOdCB5pKsHy8Gw7V7x7Wqeh06T96uHY7JbVcGUe/emWIV0SWcywrgskB0vvd/X3GLxiEx2ujHR/SnKh4RYFS/+37+yYHGTEULkbwX3QplbRuT9DOJe5dl9ako8zADeQE0A5rp2LWtdIgd076ZRwd8YbAy5MCteeTz4Y7xQJgf9AgxiOKjss3djnagqps2SddQ+iy0Kr+MiysuH2hSVkkwcRq7UPv9kv0Gufzm/SrZR/JV5fQodhoUKm3k6aj04pDr7PKxqYm0IQtF+RPo/Mk7fr9x/RJ1ItTVbiiGqRyh6f+w==', 'trade_no': '2020050322001412010500505866', 'auth_app_id': '2016102300747970', 
    'version': '1.0', 
    'app_id': '2016102300747970', 'sign_type': 'RSA2', 
    'seller_id': '2088102180823098', 'timestamp': '2020-05-03 11:03:58'}

    
    """
    # print(request_data)
    # 获取支付宝订单处理的返回结果标志
    sign = request_data.pop('sign')
    # print(sign)
    # 查询结果
    is_verify = get_verify_result(request_data, sign)
    # print(is_verify)
    if is_verify:
        # 消息来源可靠
        order_id = request_data.get('out_trade_no')
        # 去自己数据库中查询该订单的状态;例如 dashop12中订单状态案例，此时订单状态应该进入到 ‘待发货/已付款’
        if ORDER_STATUS == 2:
            result = 1
        else:
            # 触发主动查询
            res = get_trade_result(order_id)
            if res:
                # print('11111')
                result = 1
                # 支付是成功的，更改订单状态
            else:
                pass
    if result == 1:
        d_oid_str = decode_oid(order_id).decode()
        # 7_tom_1588479117
        gid_lis = d_oid_str.split('_')[:-2]
        uname = d_oid_str.split('_')[-2]
        try:
            if Order.query.filter(Order.o_id == order_id).first():
                return
            user = Person.query.filter(Person.uname == uname).first()
            order = Order()
            db.session.add(order)
            order.o_id = order_id
            order.name = uname
            order.account = request_data['total_amount']
            order.address = ''
            order.phone = '123456789'
            uid = user.id
            order.uid = uid
            order.is_active = True
            for i in gid_lis:
                cart = Cart.query.filter(Cart.uid == uid,
                                         Cart.gid == i).first()
                print(cart)
                db.session.delete(cart)
            db.session.commit()
        except Exception as e:
            print('----------------------')
            print('pay')
            print(e)
        return 1