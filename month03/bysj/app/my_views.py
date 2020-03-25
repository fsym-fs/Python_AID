from flask import request, render_template


def public_view():
    return render_template('public_html.html')


def login_view():
    return render_template('login.html')
