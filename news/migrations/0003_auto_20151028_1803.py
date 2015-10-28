# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151027_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'news', verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='sections',
            field=mptt.fields.TreeManyToManyField(to='news.Section', verbose_name='Sections'),
        ),
    ]
