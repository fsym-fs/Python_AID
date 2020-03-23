from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Aritcle(models.Model):#新增
    headline = models.CharField(null=True, blank=True,max_length=500)#新增
    name = models.CharField(null=True, blank=True, max_length=200)
    content = models.TextField(null=True, blank=True)#新增
    TAG_CHOICES = (('tech', 'Tech'), ('life', 'Life'))
    tag = models.CharField(null=True, blank=True, max_length=5, choices=TAG_CHOICES)
    def __str__(self):#新增
        return self.headline#新增

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    belong_to = models.ForeignKey(to=Aritcle, related_name='under_comment', null=True, blank=True, on_delete=models.CASCADE)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.comment

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='profile', on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='profile_image') 

class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200,default="")
    password = models.CharField(null=False, blank=False,max_length=200,default="")
    Email = models.CharField(null=False, blank=False, max_length=200,default="")
    birth = models.CharField(null=True, blank=True, max_length=200,default="")
    个性签名 = models.CharField(null=True, blank=True, max_length=200,default="")
    profile_image = models.FileField(upload_to='profile',default="") 
    实名 = models.CharField(null=False, blank=False, max_length=200,default="")
    status = models.CharField(null=True, blank=True, max_length=200,default="")
    def __str__(self):
        return self.name