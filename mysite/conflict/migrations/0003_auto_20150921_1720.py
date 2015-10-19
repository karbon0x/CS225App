# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conflict', '0002_auto_20150920_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mod',
            name='reason',
            field=models.CharField(default='Blank', max_length=1000),
        ),
    ]
