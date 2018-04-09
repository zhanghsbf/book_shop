# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('body', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('origin_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('view_times', models.IntegerField(default=1)),
                ('category', models.ForeignKey(to='post.Category')),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='post.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
