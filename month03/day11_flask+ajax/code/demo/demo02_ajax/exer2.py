from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/exer2')
def exer2_view():
    return render_template('exer2.html')


@app.route('/exer2_server', methods=['GET', 'POST'])
def exer2_server_view():
    uname = request.args.get('uname')
    pwd = request.args.get('pwd')
    if uname == "Tom":
        return "该用户已存在!"
    else:
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)
