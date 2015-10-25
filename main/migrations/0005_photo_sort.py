# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151024_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='sort',
            field=models.IntegerField(default=500),
        ),
    ]
