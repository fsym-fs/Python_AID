from app import *
from app.my_views import *


@webapp.route('/public')
def public():
    return public_view()


@webapp.route('/index', methods=['GET', 'POST'])
@webapp.route('/', methods=['GET', 'POST'])
def index():
    return index_view()


@webapp.route('/login', methods=['GET', 'POST'])
def login():
    return login_view()


@webapp.route('/register', methods=['GET', 'POST'])
def register():
    return register_view()


# 查询
@webapp.route('/user')
def users():
    return users_view()


@webapp.route('/user/<int:id>')
def user(id):
    return user_view(id)


@webapp.route('/persons')
def persons():
    return person_view()
