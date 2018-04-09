# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0003_auto_20180408_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(),
        ),
    ]
