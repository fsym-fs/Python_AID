import sys

from app import *
from app.my_views import *
from flask import url_for


@webapp.route('/public')
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
def about():
    url_for(sys._getframe().f_code.co_name)
    return signel_view()


@webapp.route('/cart', methods=['GET', 'POST'])
def about():
    url_for(sys._getframe().f_code.co_name)
    return cart_view()


@webapp.route('/test', methods=['GET', 'POST'])
def test():
    url_for(sys._getframe().f_code.co_name)
    return test_view()


# 查询
@webapp.route('/user')
def users():
    url_for(sys._getframe().f_code.co_name)
    return users_view()


@webapp.route('/user/<int:id>')
def user(id):
    url_for(sys._getframe().f_code.co_name, name=id)
    return user_view(id)


@webapp.route('/persons')
def persons():
    url_for(sys._getframe().f_code.co_name)
    return person_view()
