from flask import Flask, request, render_template

webapp = Flask(__name__)


@webapp.route('/index')
@webapp.route('/')
@webapp.route('/index.html')
def index_view():
    return render_template('My_index.html')


if __name__ == "__main__":
    webapp.run(debug=True)
