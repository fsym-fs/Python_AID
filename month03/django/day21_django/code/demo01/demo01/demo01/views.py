from django.http import HttpResponse
from django.shortcuts import render


def test_static(request):
    return render(request, 'test_static.html')


def test_cookies(request):
    username = request.COOKIES.get('sessionid', 'hhhh')
    print(username)
    resp = HttpResponse('---哈哈---')
    # resp.set_cookie('username', '123456', 300)
    return resp


def set_session(request):
    request.session['uname'] = 'Tom'
    return HttpResponse('--set session is ok--')


def get_session(requset):
    name = requset.session['uname']
    return HttpResponse('--get session values is %s--' % (name))
