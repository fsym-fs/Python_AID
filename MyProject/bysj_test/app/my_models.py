# from app import *

# 定义ORM
import time

from . import *

db = SQLAlchemy(webapp)


# 创建客户表
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(20), unique=True, nullable=False)
    # nullable 是否可以为空
    pwd = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), unique=False, default='')
    phone = db.Column(db.String(11), unique=False, nullable=False)
    signature = db.Column(db.String(200))
    address = db.Column(db.String(200))
    # is_online = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, uname, pwd, phone, email):
        self.uname = uname
        self.pwd = pwd
        self.phone = phone
        self.email = email

    # def __repr__(self):
    #     return '<User %r>' % self.uname


# 订单表
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    o_id = db.Column(db.String(100), unique=True, nullable=False)
    # nullable 是否可以为空
    name = db.Column(db.String(11), nullable=False)
    account = db.Column(db.Float, unique=False, default='')
    phone = db.Column(db.String(21), unique=False, nullable=False)
    address = db.Column(db.String(200))
    uid = db.Column(db.Integer)
    # is_online = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self):
        pass


# cart表
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    number = db.Column(db.Integer)
    # is_active = db.Column(db.Boolean, default=True)


# Comment表
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    message = db.Column(db.String(300), nullable=False)
    create_at = db.Column(db.String(300), default=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# 创建商品表
class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    g_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(100), nullable=False)
    # nullable 是否可以为空
    price = db.Column(db.String(20), default=20.00)
    title = db.Column(db.String(50), unique=False, default='')
    inventory = db.Column(db.Integer, unique=False, default=100)
    weight = db.Column(db.Integer, unique=False, default=50)
    loc = db.Column(db.String(200))
    # is_online = db.Column(db.Boolean, default=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Good %r>' % self.name


# 创建商品图片表
class Good_pic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    default_pic = db.Column(db.String(100), unique=False, nullable=False, default='default.jpg')
    gid = db.Column(db.Integer)

    def __init__(self):
        pass


# 创建商品销售表
class Good_sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sales_num = db.Column(db.Integer, unique=False)
    gid = db.Column(db.Integer)

    def __init__(self):
        pass

# 创建表格、插入数据
@webapp.before_first_request
def create_db():
    db.create_all()
    # #
    # try:
    #     # 创建数据表
    #     db.create_all()
    #     # admin = User('admin', 'admin@example.com')
    #     # db.session.add(admin)
    #     guestes = [User('guest1', 'guest1@example.com'),
    #                User('guest2', 'guest2@example.com'),
    #                User('guest3', 'guest3@example.com'),
    #                User('guest4', 'guest4@example.com')]
    #     db.session.add_all(guestes)
    #     db.session.commit()
    #     # test_person = Person('Tom', '123456')
    #     # db.session.add(test_person)
    #     # db.session.commit()
    # except:
    #     pass
