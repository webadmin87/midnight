# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('midnight_catalog', '0004_auto_20151128_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Comment')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(blank=True, verbose_name='Author', null=True, to=settings.AUTH_USER_MODEL, related_name='+')),
            ],
            options={
                'verbose_name_plural': 'ProductComments',
                'verbose_name': 'ProductComment',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.BooleanField(default=False, verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='obj',
            field=models.ForeignKey(to='midnight_catalog.Product'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, verbose_name='Parent', null=True, to='midnight_catalog.ProductComment', related_name='children'),
        ),
    ]
