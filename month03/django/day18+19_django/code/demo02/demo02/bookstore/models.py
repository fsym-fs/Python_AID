from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='', unique=True)
    price = models.DecimalField("图书定价", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField('图书零售价', max_digits=7, decimal_places=2, default=0.0)
    pub = models.CharField('出版社', max_length=200, default='')
    is_active = models.BooleanField('是否活跃',default=True)

    def __str__(self):
        return '%s_%s_%s_%s' % (self.title, self.price, self.pub, self.market_price)


class Author(models.Model):
    name = models.CharField('姓名', default='', max_length=11)
    age = models.IntegerField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)
    is_active = models.BooleanField('是否活跃', default=True)
