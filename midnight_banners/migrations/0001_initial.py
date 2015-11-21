# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('file', models.FileField(upload_to='banners', verbose_name='File')),
                ('link', models.CharField(verbose_name='Link', max_length=2000, blank=True)),
                ('target', models.CharField(verbose_name='Target', max_length=32, blank=True, choices=[('_self', 'Self window'), ('_blank', 'Blank window')])),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
            ],
            options={
                'verbose_name_plural': 'Banners',
                'verbose_name': 'Banner',
            },
        ),
        migrations.CreateModel(
            name='BannerPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
            ],
            options={
                'verbose_name_plural': 'BannerPlaces',
                'verbose_name': 'BannerPlace',
            },
        ),
    ]
