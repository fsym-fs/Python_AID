from flask import Flask, request, Response, render_template

app = Flask(__name__, template_folder="temp")


@app.route('/test01')
def test01_view():
    # user = {'username':'duke'}
    #将需要展示的数据传递给模板进行显示
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render_template('test01.html', world="go",test_list = test_list)


if __name__ == "__main__":
    app.run(debug=True)
