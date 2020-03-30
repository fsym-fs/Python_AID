from django.conf.urls import url
from .views import *
urlpatterns = [
      url(r'^all_books$',find_all_books_view,name='all_books'),
      url(r'^update_book/(\d+)$',update_book),
      url(r'^delete_book/(\d+)$',delete_book)
]