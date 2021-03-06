# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='includearea',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photoalbum',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
