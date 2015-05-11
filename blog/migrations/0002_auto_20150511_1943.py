# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.CharField(default=datetime.datetime(2015, 5, 11, 19, 43, 10, 615056, tzinfo=utc), max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 42, 52, 319853)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ppost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 42, 52, 312973)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wcomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 42, 52, 315938)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 11, 19, 42, 52, 310514)),
            preserve_default=True,
        ),
    ]
