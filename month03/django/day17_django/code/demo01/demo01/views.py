from django.http import HttpResponse, HttpRequest


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
