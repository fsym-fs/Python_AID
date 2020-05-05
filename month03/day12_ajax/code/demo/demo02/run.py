from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@app.route('/music_index.html', methods=['GET', 'POST'])
def get_data():
    """
        flask 允许的响应的类型有字符串，字典，元组和其他封装好的响应类型
        dict: flask1.1后可以使用
        tuple: 指flask返回值时的参数可以用元组的形式添加，但数据不能是自定义元组
                eg:return {(),200}
    """
    if request.method == 'GET':
        return render_template('get_data.html')
    elif request.method == 'POST':
        lis = ["Tom", "Jarry", "Lily"]
        # separators设置分隔符，默认：含有空格(', ',': ')
        #sort_keys=True:设置为按显示顺序排序
        data = json.dumps(lis, separators=(',', ':'), sort_keys=True)
        return data
    else:
        pass


@app.route('/get_server', methods=['GET', 'POST'])
def get_server():
    lis = ["Tom", "Jarry", "Lily"]
    # separators设置分隔符，默认：含有空格(', ',': ')
    #sort_keys=True:设置为按显示顺序排序
    data = json.dumps(lis, separators=(',', ':'), sort_keys=True)
    return data


@app.route('/exer1', methods=['GET', 'POST'])
def exer1_view():
    return render_template('exer1.html')


lis = [
    ("Tom", "123456"),
    ("Jarry", "111111"),
    ("Lily", "000000")
]


@app.route('/exer1_server', methods=['GET', 'POST'])
def exer1_server_view():
    if request.method == 'GET':
        uname = request.args.get('uname')
        for i in lis:
            if uname in i:
                return json.dumps({"note": 1000, "msg": "用户名已存在!"}, separators=(',', ':'))
        return json.dumps({"note": 1001, "msg": "OK!"}, separators=(',', ':'))
    elif request.method == 'POST':
        # # 表单数据
        # uname = request.form.get('uname')
        # pwd = request.form.get('pwd')
        # json数据
        uname = request.json.get('uname')
        pwd = request.json.get('pwd')
        lis.append((uname, pwd))
        return json.dumps("注册成功!")
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)
