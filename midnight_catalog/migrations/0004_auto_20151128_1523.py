# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_catalog', '0003_param_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paramvalue',
            options={'verbose_name_plural': 'ParamValues', 'verbose_name': 'ParamValue'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, max_digits=11, decimal_places=2, verbose_name='Price'),
        ),
    ]
