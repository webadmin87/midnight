# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20151112_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='section',
            name='author',
            field=models.ForeignKey(verbose_name='Author', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
