# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_main', '0002_auto_20151122_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagecomment',
            options={'verbose_name_plural': 'PageComments', 'verbose_name': 'PageComment'},
        ),
    ]
