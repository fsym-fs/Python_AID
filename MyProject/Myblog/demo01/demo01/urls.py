"""demo01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import logout
from demo.views import  index, detail,index_login,index_register,about_me,personal,write#引入view模块里的first_try方法（用于页面的代码）

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('detail/(?P<page_num>\d+)$', detail, name='detail'),
    path('login/', index_login,name='login'),
    path('register/', index_register,name='register'),
    path('logout/',logout,{'next_page':'/register'},name='logut'),
    path('about/', about_me, name='about_me'),
    path('personal/',personal,name='personal'),
    path('write/',write,name='write'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)