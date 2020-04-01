from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User
import hashlib


# Create your views here.

def reg_view(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        print(pwd1, pwd2)
        # 参数检查
        if pwd1 != pwd2:
            error = '用户名已存在或者密码不一致!'
            return render(request, 'user/register.html', locals())

        old_user = User.objects.filter(username=username)
        if old_user:
            error = '用户名已存在或者密码不一致!'
            return render(request, 'user/register.html', locals())

        # 将明文密码转化为哈希值
        # 哈希算法
        # 1,定长定值的输出-->算法不变的情况下，无论输入多少，输出定长/算法不变的情况下，输入不变，则输出的值不变
        # 2,不可逆-->hash结果,反算不出明文结果
        # 3,,雪崩效应-->明文改变，则输出的值一定改变 - eg:文件完整性校验(大文件抽样)

        m = hashlib.md5()
        m.update(pwd1.encode())
        pwd_h = m.hexdigest()
        try:
            # 由于username有唯一索引,所以此处可能有插入异常
            user = User.objects.create(username=username, password=pwd_h)
        except Exception as e:
            error = '注册失败!'
            return render(request, 'user/register.html', locals())
        # 保存状态
        request.session['uid'] = user.id
        request.session['username'] = username
        return HttpResponse('OK')
    else:
        pass


def login_view(request):
    if request.method == 'GET':
        # 优先检查session
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('已登录!')
        # 检查cookies
        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        if username and uid:
            # 回写session
            request.session['uid'] = uid
            request.session['username'] = username
            return HttpResponse('已登录!!')
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        username = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            error = '用户名或密码错误!'
            return render(request, 'user/login.html', locals())
        m = hashlib.md5()
        m.update(pwd.encode())
        m_pwd = m.hexdigest()
        if m_pwd != old_user.password:
            error = '用户名或密码错误!'
            return render(request, 'user/login.html', locals())
        ## 存储状态
        request.session['uid'] = old_user.id
        request.session['username'] = username
        if 'rem_name' in request.POST:
            resp = HttpResponse('OK')
            resp.set_cookie('username', username, 3600 * 24 * 3)
            resp.set_cookie('uid', old_user.id, 3600 * 24 * 3)
            return resp
    else:
        pass
    return HttpResponse('OK')
