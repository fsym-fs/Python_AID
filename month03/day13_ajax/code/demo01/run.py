from flask import Flask, request, render_template
import json,time

app = Flask(__name__)


@app.route('/index')
def index_view():
    pass


@app.route('/load')
def load_view():
    return render_template('load.html')


@app.route('/load_server', methods=['GET', 'POST'])
def load_server_view():
    # uname = request.args.get('uname')
    # age = request.args.get('age')
    # print(uname, age)
    uname2 = request.form.get('uname')
    age2 = request.form.get('age')
    print(uname2, age2)
    return render_template('load_server.html')


@app.route('/get')
def get_view():
    return render_template('ajax_get.html')


@app.route('/get_server')
def get_server_view():
    uname = request.args.get('uname')
    age = int(request.args.get('age'))
    if age < 18:
        data = {"note": 201, "msg": "未成年，禁止访问!"}
    elif age >= 18:
        data = {"note": 200, "msg": "允许访问!"}
    return json.dumps(data)
    # return "欢迎%s" % uname


@app.route('/post', methods=['GET', 'POST'])
def post_view():
    if request.method == 'GET':
        return render_template('ajax_post.html')
    elif request.method == 'POST':
        uname = request.form.get('uname')
        age = request.form.get('age')
        return json.dumps({"note": 200, "msg": "允许访问!"})
    else:
        pass


@app.route('/ajax')
def ajax_view():
    return render_template('ajax_ajax.html')


@app.route('/ajax_server',methods = ['GET','POST'])
def ajax_server_view():
    time.sleep(3)
    if request.method == 'GET':
        uname = request.args.get('uname')
    elif request.method == 'POST':
        # uname = request.form.get('uname')
        uname = request.json.get('uname')
    return json.dumps({"note": 200, "msg": "OK!"+uname})


if __name__ == "__main__":
    app.run(debug=True)
