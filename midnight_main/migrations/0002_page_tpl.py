# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('midnight_main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='tpl',
            field=models.CharField(verbose_name='Template', default='midnight_main/templates/midnight_main/pages/pages.html', max_length=255, choices=[('midnight_main/templates/midnight_main/pages/pages.html', 'Simple page'), ('midnight_main/templates/midnight_main/pages/guestbook.html', 'Guestbook')]),
        ),
    ]
