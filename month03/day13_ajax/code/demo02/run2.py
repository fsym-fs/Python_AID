from flask import Flask,request

app = Flask(__name__)

@app.route('/cross_server',methods = ['GET'])
def cross_server_view():
    a = request.args.get('name')
    print(a)
    # return 'this is 5001'
    # 法一
    return "print('this is 5001')"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
