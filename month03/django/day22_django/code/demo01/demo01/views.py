import time

from django.shortcuts import render
from django.views.decorators.cache import cache_page

from django.http import HttpResponse


# 10秒刷新
@cache_page(10)
def test_cache(request):
    t1 = time.time()
    return HttpResponse('t1 is %s' % (t1))
    # return render(request,'test_cache.html',locals())


def test_mv(request):
    print('-----mw view do')
    return HttpResponse('---test middleware---')


def exc_mv(request):
    return HttpResponse('---ok---')

def test_csrf(request):
    if request.method == 'GET':
        return render(request,'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---post is ok---')
