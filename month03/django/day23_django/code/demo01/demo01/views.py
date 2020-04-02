import os
import time

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page

from django.http import HttpResponse

from django.conf import settings

import hashlib

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
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---post is ok---')


def test_page(request):
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    # /test_page?page=x
    cur_page = request.GET.get('page', 1)
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        file_obj = request.FILES.get('myfile')
        file_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)
        with open(file_path, 'wb') as f:
            data = file_obj.file.read()
            f.write(data)
        return HttpResponse(file_obj.name + 'is OK!')
    else:
        pass


def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="test01.csv"'
    all_data = [
        {'id': 1, 'title': 'Python'},
        {'id': 2, 'title': 'Java'},
        {'id': 3, 'title': 'C'},
    ]
    import csv
    writer = csv.writer(response)
    writer.writerow(['id', 'title'])
    for data in all_data:
        writer.writerow([data['id'], data['title']])
    return response


