# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='post',
        ),
        migrations.RemoveField(
            model_name='order',
            name='seller',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(to='buy.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='post',
            field=models.ForeignKey(to='post.Post'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='seller',
            field=models.ForeignKey(related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
