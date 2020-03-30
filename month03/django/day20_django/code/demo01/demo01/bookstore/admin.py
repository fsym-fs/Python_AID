from django.contrib import admin
from .models import Book, Author


# Register your models here.

# 类模型管理器
class BookManage(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price', 'is_active']

    list_display_links = ['title']

    list_filter = ['title', 'pub', 'is_active']

    list_editable = ['is_active']

    search_fields = ['title']


class AuthorManage(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'email', 'is_active']

    list_display_links = ['name']

    list_filter = ['is_active', 'age']

    list_editable = ['is_active','age']

    search_fields = ['name']


admin.site.register(Book, BookManage)
admin.site.register(Author,AuthorManage)
