# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-03-27 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.CharField(default='', max_length=100, verbose_name='描述'),
        ),
    ]
