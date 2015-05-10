# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pcomment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 10, 2, 56, 27, 30445))),
                ('profilecomment', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pdislike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('color', models.IntegerField(default=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('color', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ppost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 10, 2, 56, 27, 24082))),
                ('profilepost', models.CharField(max_length=1000)),
                ('hascomments', models.BooleanField(default=False)),
                ('clicked', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('user1', models.ForeignKey(related_name='user1', to=settings.AUTH_USER_MODEL)),
                ('user2', models.ForeignKey(related_name='user2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('locale', models.CharField(max_length=1000)),
                ('age', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wcomment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 10, 2, 56, 27, 27305))),
                ('wallcomment', models.CharField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wdislike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('color', models.IntegerField(default=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wlike',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('color', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wpost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name=b'#', primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 5, 10, 2, 56, 27, 21445))),
                ('wallpost', models.CharField(max_length=1000)),
                ('hascomments', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='wlike',
            name='wall',
            field=models.ForeignKey(to='blog.Wpost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wdislike',
            name='wall',
            field=models.ForeignKey(to='blog.Wpost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wcomment',
            name='wall',
            field=models.ForeignKey(to='blog.Wpost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plike',
            name='profile',
            field=models.ForeignKey(to='blog.Ppost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='plike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdislike',
            name='profile',
            field=models.ForeignKey(to='blog.Ppost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pdislike',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pcomment',
            name='profile',
            field=models.ForeignKey(to='blog.Ppost'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pcomment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
