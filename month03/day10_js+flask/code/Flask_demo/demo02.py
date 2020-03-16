from flask import Flask, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index_view():
    return "这是一个项目的首页"


@app.route('/detail')
def detail():
    return "这是一个项目的详情页"


@app.route('/show/<uname>/<int:age>')
def show_view(uname, age):
    # return "欢迎%s" % unames
    return "姓名:%s,年龄:%s" % (uname, age)


@app.route('/server', methods=['get', 'post'])
def server_view():
    #接收get请求,from falsk import request
    #request.args保存了所有get数据内容(类字典)
    #request.form保存了post提交的数据(类字典)
    # [('uname', '发方法'),('a','b')] l
    print(request.form)
    # uname = request.form['uname']
    #字典里同样可以使用该get方法
    uname = request.form.get('uname', '名字没有找到!')
    return "欢迎%s" % uname


if __name__ == "__main__":
    app.run(debug=True)
