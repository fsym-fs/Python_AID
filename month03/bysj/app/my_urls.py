from app import *
from app.my_views import *


@webapp.route('/public')
def public():
    return public_view()


@webapp.route('/login', methods=['GET', 'POST'])
def login():
    return login_view()
