from django.db import models


# Create your models here.

class Publisher(models.Model):
    # 一
    name = models.CharField('名字', max_length=20)


class Book(models.Model):
    # 多
    title = models.CharField('书名', max_length=11)
    publisher = models.ForeignKey(Publisher)