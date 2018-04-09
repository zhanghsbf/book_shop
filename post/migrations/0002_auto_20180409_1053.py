# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='origin_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(),
        ),
    ]
