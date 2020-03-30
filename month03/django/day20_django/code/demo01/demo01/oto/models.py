from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=11, verbose_name='作家姓名')


class Wife(models.Model):
    name = models.CharField('妻子姓名', max_length=11)
    author = models.OneToOneField(Author)