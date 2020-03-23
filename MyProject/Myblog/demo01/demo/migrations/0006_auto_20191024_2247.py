# Generated by Django 2.2.6 on 2019-10-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='Email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.FileField(default='', upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='person',
            name='个性签名',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='实名',
            field=models.CharField(default='', max_length=200),
        ),
    ]
