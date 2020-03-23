from flask import Flask, request, render_template
import json,time

webapp = Flask(__name__)


@webapp.route('/index')
@webapp.route('/')
@webapp.route('/index.html')
def index_view():
    return render_template('My_index.html')


@webapp.route("/data")
def index_data_view():
    size = request.args.get('size')
    with open("month03/month03/day15_project_front/demo/comment.data","r") as f: 
        datas = f.read()
        datas = json.loads(datas)
    if not size:
        datas = datas[:10]
    else:
        size = int(size)
        datas = datas[size:size+10]
    if datas:
        return json.dumps({"code": 200, "datas": datas})
    else:
        return json.dumps({"code":201,"data":"当前已经没有数据了!"})

@webapp.route('/add',methods = ['POST','GET'])
def add_data_view():
    username = request.json.get('username')
    content = request.json.get('content')
    with open('month03/month03/day15_project_front/demo/comment.data',"r") as f:
        all_data = json.loads(f.read())
    with open('month03/month03/day15_project_front/demo/comment.data',"w") as f:
        new_data = {
            'num':len(all_data)+1,
            'username':username,
            'time':time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()),
            'content':content
        }
        all_data.append(new_data)
        f.write(json.dumps(all_data))
    return json.dumps({"code":200,"msg":"内容发布完成!"})

if __name__ == "__main__":
    webapp.run(debug=True)
