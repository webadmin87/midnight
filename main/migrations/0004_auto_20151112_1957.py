# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20151112_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='includearea',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
