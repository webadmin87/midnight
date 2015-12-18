# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_main', '0003_auto_20151207_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='tpl',
            field=models.CharField(verbose_name='Template', choices=[('midnight_main/pages/pages.html', 'Simple page'), ('midnight_main/pages/main.html', 'Main page'), ('midnight_main/pages/guestbook.html', 'Guestbook')], default='midnight_main/pages/pages.html', max_length=255),
        ),
    ]
