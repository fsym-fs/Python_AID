# Generated by Django 2.2.6 on 2019-10-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20191022_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='best_comment',
            field=models.BooleanField(default=False),
        ),
    ]
