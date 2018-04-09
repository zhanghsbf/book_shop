# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('address', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('generate_date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(related_name='buyer', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='post.Post')),
                ('seller', models.ForeignKey(related_name='seller', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
