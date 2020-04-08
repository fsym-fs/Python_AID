from django.db import models


# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=11)
    age = models.IntegerField(default=0)
