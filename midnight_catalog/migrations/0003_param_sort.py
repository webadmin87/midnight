# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_catalog', '0002_auto_20151125_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='sort',
            field=models.IntegerField(verbose_name='Sort', default=500),
        ),
    ]
