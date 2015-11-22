# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='param',
            name='measurement',
            field=models.CharField(max_length=32, blank=True, verbose_name='Measurement'),
        ),
    ]
