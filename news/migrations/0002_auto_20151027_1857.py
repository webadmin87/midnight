# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'NewsItem', 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name': 'NewsSection', 'verbose_name_plural': 'NewsSections'},
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'photos', verbose_name='Image', blank=True),
        ),
    ]
