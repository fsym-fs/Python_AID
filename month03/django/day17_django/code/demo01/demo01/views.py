from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.shortcuts import render


def page01_view(request):
    if request.method == 'GET':
        a = request.GET.get('a', 'null')
        a_list = request.GET.getlist('a')
        print(a_list)
        return HttpResponse('a=%s,OK!' % a)
    elif request.method == 'POST':
        pass
    else:
        pass
    return HttpResponse('ERROR')


def page02_view(request):
    if request.method == 'GET':
        html = """
        <form method='post' action="/test_post">
            姓名:<input type="text" name="uname">
            <input type='submit' value='登陆'>
        </form>
        """
        return HttpResponse(html)
    elif request.method == 'POST':
        username = request.POST['uname']
        print('---test--post---')
        print(username)
        return HttpResponse('OK!')
    else:
        pass


def test_html(request):
    # # 加载html
    # t = loader.get_template('test_html.html')
    # # 执行render 转化成字符串
    # html = t.render()
    # # 响应给浏览器
    # return HttpResponse(html)
    dic = {
        'username': 'Tom',
        'age': 20,
        'lis': ['1', '2', '3'],
        'd': {'a': 11, 'b': 12},
    }
    # xss注入攻击
    return render(request, 'test_html.html', dic)


def num_test01_view(request):
    if request.method == 'GET':
        return render(request, 'test01.html')
    elif request.method == 'POST':
        try:
            x = int(request.POST['x'])
            y = int(request.POST['y'])
            op = request.POST['op']
            if op == 'add':
                result = x + y
            elif op == 'sub':
                result = x - y
            elif op == 'mul':
                result = x * y
            elif op == 'div':
                result = x / y
            else:
                result = "???"
            # dic = {
            #     'x': x,
            #     'y': y,
            #     'result': result,
            # }
            # 将当前方法体里的变量组成字典
            # locals()
            return render(request, 'test01.html', locals())
        except:
            return HttpResponse('<h1>404 Error:请输入数字!</h1>')
