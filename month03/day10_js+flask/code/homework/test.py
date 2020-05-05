from flask import Flask
app = Flask(__name__)


@app.route('/test')
def test_view():
    f = open("/home/tarena/桌面/month03/month03/day10_js+flask/note/homework/test.html","rb")
    return f.read()


if __name__ == "__main__":
    app.run(debug=True)
