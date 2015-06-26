# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150521_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.CharField(default=datetime.datetime(2015, 6, 26, 5, 41, 7, 989323, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 40, 48, 593606)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ppost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 40, 48, 587035)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 40, 48, 590127)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 5, 40, 48, 584479)),
            preserve_default=True,
        ),
    ]
