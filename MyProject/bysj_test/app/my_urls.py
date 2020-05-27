import sys

from app import *
from app.my_views import *
from flask import url_for
from app.users.views import *
from app.admin.views import *
from app.mall.views import *


@webapp.route('/admin', methods=['GET', 'POST'])
@webapp.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    url_for(sys._getframe().f_code.co_name)
    return admin_login_view()


@webapp.route('/admin/index', methods=['GET', 'POST'])
def admin_index():
    url_for(sys._getframe().f_code.co_name)
    return admin_index_view()


@webapp.route('/admin/home', methods=['GET', 'POST'])
def admin_home():
    url_for(sys._getframe().f_code.co_name)
    return admin_home_view()


@webapp.route('/admin/user/home', methods=['GET', 'POST', 'DELETE'])
def admin_user_home():
    url_for(sys._getframe().f_code.co_name)
    return admin_user_home_view()


@webapp.route('/admin/user/form', methods=['GET', 'POST'])
def admin_user_form():
    url_for(sys._getframe().f_code.co_name)
    return admin_user_form_view()


@webapp.route('/admin/goods/home', methods=['GET', 'POST', 'DELETE'])
def admin_goods_home():
    url_for(sys._getframe().f_code.co_name)
    return admin_goods_home_view()


@webapp.route('/admin/goods/form', methods=['GET', 'POST'])
def admin_goods_form():
    url_for(sys._getframe().f_code.co_name)
    return admin_goods_form_view()


# ----------------------------------------------------------------------------

@webapp.route('/public', methods=['GET', 'POST'])
def public():
    url_for(sys._getframe().f_code.co_name)
    return public_view()


@webapp.route('/index', methods=['GET', 'POST'])
@webapp.route('/', methods=['GET', 'POST'])
def index():
    url_for(sys._getframe().f_code.co_name)
    return index_view()


@webapp.route('/login', methods=['GET', 'POST'])
def login():
    url_for(sys._getframe().f_code.co_name)
    return login_view()


@webapp.route('/register', methods=['GET', 'POST'])
def register():
    url_for(sys._getframe().f_code.co_name)
    return register_view()


@webapp.route('/send_code', methods=['GET', 'POST'])
def send_code():
    url_for(sys._getframe().f_code.co_name)
    return send_code_view()


@webapp.route('/personal', methods=['GET', 'POST'])
def personal():
    url_for(sys._getframe().f_code.co_name)
    return personal_view()


@webapp.route('/about', methods=['GET', 'POST'])
def about():
    url_for(sys._getframe().f_code.co_name)
    return about_view()


@webapp.route('/single', methods=['GET', 'POST'])
def single():
    url_for(sys._getframe().f_code.co_name)
    return single_view()


@webapp.route('/add_content', methods=['GET', 'POST'])
def add_content():
    url_for(sys._getframe().f_code.co_name)
    return add_content_view()


@webapp.route('/cart', methods=['GET', 'POST', 'DELETE'])
def cart():
    url_for(sys._getframe().f_code.co_name)
    return cart_view()


@webapp.route('/all', methods=['GET', 'POST'])
def all():
    url_for(sys._getframe().f_code.co_name)
    return all_view()


@webapp.route('/paying', methods=['GET', 'POST'])
def paying():
    url_for(sys._getframe().f_code.co_name)
    return paying_view()


# @webapp.route('/result', methods=['GET', 'POST'])
# def result():
#     url_for(sys._getframe().f_code.co_name)
#     return alipay_view()


@webapp.route('/order', methods=['GET', 'POST'])
def order():
    url_for(sys._getframe().f_code.co_name)
    return order_view()


@webapp.route('/search', methods=['GET', 'POST'])
def search():
    url_for(sys._getframe().f_code.co_name)
    return search_view()


@webapp.route('/pa')
def pa():
    url_for(sys._getframe().f_code.co_name)
    return pa_view()


@webapp.route('/tt', methods=['GET', 'POST'])
def tt():
    url_for(sys._getframe().f_code.co_name)
    return tt_view()
