from flask import request, render_template
from app.my_models import User
from app.my_models import Person




def public_view():
    return render_template('public_html.html')


def index_view():
    return render_template('index.html')


def login_view():
    return render_template('login.html')


def register_view():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        pass
    else:
        pass


def personal_view():
    if request.method == 'GET':
        return render_template('personal.html')
    elif request.method == 'POST':
        pass
    else:
        pass

def about_view():
    if request.method == 'GET':
        return render_template('about.html')
    elif request.method == 'POST':
        pass
    else:
        pass

def test_view():
    if request.method == 'GET':
        return render_template('test.html')
    elif request.method == 'POST':
        pass
    else:
        pass




def person_view():
    persons = Person.query.all()
    return "<br>".join(["{0}: {1}".format(person.uname, person.pwd) for person in persons])


def users_view():
    users = User.query.all()
    return "<br>".join(["{0}: {1}".format(user.name, user.email) for user in users])


def user_view(id):
    user = User.query.filter_by(id=id).one()
    return "{0}: {1}".format(user.name, user.email)
