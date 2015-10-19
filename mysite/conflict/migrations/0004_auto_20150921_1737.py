# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('conflict', '0003_auto_20150921_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_mod',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
