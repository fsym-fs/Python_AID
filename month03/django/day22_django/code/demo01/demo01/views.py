import time
from django.views.decorators.cache import cache_page

from django.http import HttpResponse

# 10秒刷新
@cache_page(10)
def test_cache(request):
    t1 = time.time()
    return HttpResponse('t1 is %s' % (t1))
