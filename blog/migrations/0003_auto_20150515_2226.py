# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150511_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 22, 26, 14, 569976, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 22, 26, 26, 769306, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 22, 26, 31, 848960, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 22, 26, 4, 582356)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ppost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 22, 26, 4, 576842)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 22, 26, 4, 579862)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 15, 22, 26, 4, 574224)),
            preserve_default=True,
        ),
    ]
