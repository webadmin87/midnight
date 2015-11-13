# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151112_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='comments',
            field=models.BooleanField(verbose_name='Comments', default=False),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='email',
            field=models.EmailField(verbose_name='Email', blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='text',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='pagecomment',
            name='username',
            field=models.CharField(verbose_name='Username', max_length=255),
        ),
    ]
