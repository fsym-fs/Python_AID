"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # http://127.0.0.1:8000/page01
    url(r'^page01$', views.page01_view),
    url(r'^page02$', views.page02_view),
    url(r'^page03$', views.page03_view),
    # http://127.0.0.1:8000/page3--100
    # 普通分组（）-> 位置参数的方式 传递给视图函数
    url(r'^page(\d+)', views.page_view),
    url(r'^(\d+)/(\w+)/(\d+)', views.page_test_view),
    # 可以用正则表达式分组 (?P<name>pattern) 提取参数后用函数关键字传参传递给视图函数
    url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
    url(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})',views.test2_view),
    url(r'^birthday/(?P<day>\d{1,2})/(?P<month>\d{1,2})/(?P<year>\d{4})',views.test2_view),
]
