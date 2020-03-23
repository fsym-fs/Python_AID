from django.contrib import admin
from demo.models import Aritcle,Comment,UserProfile,Person
# Register your models here.
admin.site.register(Aritcle)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Person)
