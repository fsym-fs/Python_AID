from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route('/index')
def index_view():
    pass


@app.route('/load')
def load_view():
    return render_template('load.html')


@app.route('/load_server',methods = ['GET','POST'])
def load_server_view():
    # uname = request.args.get('uname')
    # age = request.args.get('age')
    # print(uname, age)
    uname2 = request.form.get('uname')
    age2 = request.form.get('age')
    print(uname2,age2)
    return render_template('load_server.html')


if __name__ == "__main__":
    app.run(debug=True)
