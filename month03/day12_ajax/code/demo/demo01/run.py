from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index_view():
    return "Hello,index!"


# @app.route('/post', methods=['get', 'post'])
# def ajax_post_view():
#     return render_template('ajax_post.html')


# @app.route('/post_server', methods=['get', 'post'])
# def post_server_view():
#     uname = request.form.get('uname')
#     return "欢迎%s" % uname

@app.route('/post',methods=['GET','POST'])
def post_view():
    #get请求，显示页面
    #post请求,处理数据
    if request.method == 'GET':
        return render_template('ajax_post.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        return "欢迎%s" % uname
        

if __name__ == "__main__":
    app.run(debug=True)
