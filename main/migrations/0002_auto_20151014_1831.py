# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncludeArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('text', redactor.fields.RedactorField(verbose_name='Text', blank=True)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'IncludeArea',
                'verbose_name_plural': 'IncludeAreas',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name='Parent', blank=True, to='main.Menu', null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug', blank=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='target',
            field=models.CharField(blank=True, max_length=32, verbose_name='Target', choices=[(b'_self', 'Self window'), (b'_blank', 'Blank window')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='page',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
    ]
