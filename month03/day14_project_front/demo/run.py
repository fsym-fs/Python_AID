from flask import Flask, render_template, request

webapp = Flask(__name__)


@webapp.route('/demo')
def demo_view():
    return render_template('demo.html')
@webapp.route('/index')
def index_view():
    return render_template('index.html')

if __name__ == "__main__":
    webapp.run(debug=True)
