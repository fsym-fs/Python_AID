from flask import Flask, request, render_template

#Flask(import_name,template_folder='templates')
#html文件需要放入同级目录下的templates文件夹下
#静态文件放在同级目录下的static文件夹下

app = Flask(__name__)


@app.route('/demo01')
def demo01_view():
   return render_template('demo01.html', world="demo01")


if __name__ == "__main__":
    app.run(debug=True)
