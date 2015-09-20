# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('conflict', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user_mod',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user_mod',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user_mod',
            name='state',
        ),
        migrations.RemoveField(
            model_name='user_mod',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='user_mod',
            name='decision',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_mod',
            name='reason',
            field=models.CharField(max_length=1000, default=datetime.datetime(2015, 9, 20, 12, 58, 56, 38947, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Reports',
        ),
    ]
