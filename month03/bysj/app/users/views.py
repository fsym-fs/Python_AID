from flask import request, render_template
from app.my_models import User
from app.my_models import Person


def login_view():
    if request.method == 'GET':
        return render_template('users/login.html')
    elif request.method == 'POST':
        pass
    else:
        pass

def register_view():
    if request.method == 'GET':
        return render_template('users/register.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def personal_view():
    if request.method == 'GET':
        return render_template('users/personal.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def cart_view():
    if request.method == 'GET':
        return render_template('users/cart.html')
    elif request.method == 'POST':
        pass
    else:
        pass
