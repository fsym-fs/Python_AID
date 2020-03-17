from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/demo01')
@app.route('/demo01.html')
def demo01_view():
    return render_template('demo01.html')


@app.route('/server')
def server_view():
    return "server_view"


@app.route('/exer')
def exer_view():
    return render_template('exer1.html')


@app.route('/exer_server', methods=['GET', 'POST'])
def exer_server_view():
    uname = request.args.get('uname')
    return '和%s有关的数据!' % uname


if __name__ == "__main__":
    app.run(debug=True)
