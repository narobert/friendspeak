# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150626_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 42, 30, 891497)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ppost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 42, 30, 881654)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 42, 30, 887141)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 42, 30, 877095)),
            preserve_default=True,
        ),
    ]
