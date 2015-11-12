# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='news', blank=True),
        ),
    ]
