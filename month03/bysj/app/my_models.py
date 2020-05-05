# from app import *


# 定义ORM
from . import *

db = SQLAlchemy(webapp)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(80), unique=True)
    # nullable 是否可以为空
    pwd = db.Column(db.String(11), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, name, pwd, email,phone):
        self.uuname = name
        self.pwd = pwd
        self.email = email
        self.phone = phone

    # 显示属性
    def __repr__(self):
        return '<User %r>' % self.name


# 创建客户表
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True, nullable=False)
    # nullable 是否可以为空
    pwd = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), unique=False, default='')
    phone = db.Column(db.String(11), unique=True,nullable=False)
    signature = db.Column(db.String(200))
    address = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, uname, pwd,phone):
        self.uname = uname
        self.pwd = pwd
        self.phone = phone

    def __repr__(self):
        pass


# 创建表格、插入数据
@webapp.before_first_request
def create_db():
    #
    try:
        # 创建数据表
        db.create_all()
        # admin = User('admin', 'admin@example.com')
        # db.session.add(admin)
        # guestes = [User('guest1', 'guest1@example.com'),
        #            User('guest2', 'guest2@example.com'),
        #            User('guest3', 'guest3@example.com'),
        #            User('guest4', 'guest4@example.com')]
        # db.session.add_all(guestes)
        # db.session.commit()
        # test_person = Person('Tom', '123456')
        # db.session.add(test_person)
        # db.session.commit()
    except:
        pass
