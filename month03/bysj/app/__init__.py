from flask import Flask

# 创建app应用,__name__是python预定义变量，被设置为使用本模块.
webapp = Flask(__name__,template_folder='../templates',static_folder='../static')
from app import my_urls
