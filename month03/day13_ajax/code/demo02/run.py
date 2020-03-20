from flask import Flask,render_template

app = Flask(__name__)

@app.route('/cross')
def cross_view():
    return render_template('cross.html')

if __name__ == "__main__":
    app.run(debug=True)