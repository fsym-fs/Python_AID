from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


def page01_view(request):
    html = '<h1>Hello,World!</h1>'
    # return JsonResponse(html,safe=False)
    # return HttpResponse(html)
    # 依靠响应头里的Location,告知浏览器此次跳转的目的地
    return HttpResponseRedirect('/page02')


def page02_view(requset):
    html = '<h1>page02</h1>'
    return HttpResponse(html)


def page03_view(requset):
    html = '<h1>page03</h1>'
    return HttpResponse(html)


def page_view(requset, n):
    # n-> 是 str
    # print(type(n))
    html = 'page' + n
    return HttpResponse(html)


def page_test_view(request, n1, s, n2):
    print(n1, s, n2)
    if s == "add":
        result = int(n1) + int(n2)
    elif s == "sub":
        result = int(n1) - int(n2)
    elif s == "mul":
        result = int(n1) * int(n2)
    else:
        result = "404 error!"
    return HttpResponse('<h1>%d<h1>' % result)


def person_view(requset, name, age):
    return HttpResponse("姓名:%s,年龄:%s" % (name, age))


def test2_view(request, year, month, day):
    print(request.path_info)
    # 请求头
    print(request.META)
    print(request.method)
    return HttpResponse("生日是%s年%s月%s日" % (year, month, day))
