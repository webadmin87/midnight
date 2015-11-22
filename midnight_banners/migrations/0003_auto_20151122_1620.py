# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_banners', '0002_auto_20151121_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bannerplace',
            name='author',
            field=models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
