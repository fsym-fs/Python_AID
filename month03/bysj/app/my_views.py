from flask import request, render_template
from app.my_models import Person


def public_view():
    return render_template('public_html.html')


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




# def users_view():
#     users = User.query.all()
#     print(users)
#     return "<br>".join(["{0}: {1}".format(user.uname, user.email) for user in users])


# def user_view(id):
#     user = User.query.filter_by(id=id).one()
#     return "{0}: {1}".format(user.uname, user.email)
