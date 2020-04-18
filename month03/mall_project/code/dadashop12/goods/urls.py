from django.conf.urls import url

from . import views

from django.views.decorators.cache import cache_page
urlpatterns = [
    url(r'^/index$', cache_page(600,cache='goods')(views.GoodsIndexView.as_view())),
    url(r'^/catalogs/(?P<catalog_id>\d+)', views.GoodsListView.as_view()),
    url(r'^/detail/(?P<sku_id>\d+)$', views.GoodsDetailView.as_view()),
]