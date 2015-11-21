# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('midnight_banners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerplace',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='banner',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='banner',
            name='place',
            field=models.ForeignKey(to='midnight_banners.BannerPlace', verbose_name='BannerPlace'),
        ),
    ]
