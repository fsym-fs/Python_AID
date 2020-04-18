import sys

from app import *
from app.my_views import *
from flask import url_for
from app.users.views import *
from app.admin.views import *


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


@webapp.route('/personal', methods=['GET', 'POST'])
def personal():
    url_for(sys._getframe().f_code.co_name)
    return personal_view()


@webapp.route('/about', methods=['GET', 'POST'])
def about():
    url_for(sys._getframe().f_code.co_name)
    return about_view()


@webapp.route('/single', methods=['GET', 'POST'])
def signle():
    url_for(sys._getframe().f_code.co_name)
    return single_view()


@webapp.route('/cart', methods=['GET', 'POST'])
def cart():
    url_for(sys._getframe().f_code.co_name)
    return cart_view()


@webapp.route('/test', methods=['GET', 'POST'])
def test():
    url_for(sys._getframe().f_code.co_name)
    return test_view()


# # 查询
# @webapp.route('/user')
# def users():
#     url_for(sys._getframe().f_code.co_name)
#     return users_view()

# @webapp.route('/user/<int:id>')
# def user(id):
#     url_for(sys._getframe().f_code.co_name, name=id)
#     return user_view(id)


@webapp.route('/pa')
def pa():
    url_for(sys._getframe().f_code.co_name)
    return pa_view()
