from flask import Flask, request, render_template
import json

webapp = Flask(__name__)


@webapp.route('/public')
def public_view():
    pass


@webapp.route('/login', methods=['GET', 'POST'])
def login_view():
    return render_template('login.html')


if __name__ == '__main__':
    webapp.run(debug=True)
