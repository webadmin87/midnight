# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
