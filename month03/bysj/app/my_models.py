# from app import *


# 定义ORM
from . import *

db = SQLAlchemy(webapp)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name


# 创建表格、插入数据
# @webapp.before_first_request
# def create_db():
#     #
#     try:
#         db.create_all()
#         admin = User('admin', 'admin@example.com')
#         db.session.add(admin)
#         guestes = [User('guest1', 'guest1@example.com'),
#                    User('guest2', 'guest2@example.com'),
#                    User('guest3', 'guest3@example.com'),
#                    User('guest4', 'guest4@example.com')]
#         db.session.add_all(guestes)
#         db.session.commit()
#     except:
#         pass
