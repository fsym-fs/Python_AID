from flask import request, render_template
from app.my_models import User


def public_view():
    return render_template('public_html.html')


def login_view():
    return render_template('login.html')


def users_view():
    users = User.query.all()
    return "<br>".join(["{0}: {1}".format(user.name, user.email) for user in users])


def user_view(id):
    user = User.query.filter_by(id=id).one()
    return "{0}: {1}".format(user.name, user.email)
