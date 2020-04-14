from flask import Flask
import os
# 链接数据库
from flask_sqlalchemy import SQLAlchemy

# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
webapp = Flask(__name__)
from app import my_urls

# # 引入config配置
# webapp.config.from_object('config')
# # 链接数据库
# db = SQLAlchemy(webapp, use_native_unicode='utf8')
# db.create_all()

"""
    链接数据库
"""
# 获取当前文件的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# 拼接数据库的ＵＲＬ路径
#  os.path.join　把basedir和data.sqlite的路径拼接起来#
# data.sqlite为数据库文件，若该文件夹下没有这个文件会自动创建

webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bysj.sqlite')
# 配置这个键之后，每次请求结束之后都会提交数据库的变动
webapp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

