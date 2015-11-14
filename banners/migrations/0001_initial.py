# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('file', models.FileField(verbose_name='File', upload_to='banners')),
                ('link', models.CharField(verbose_name='Link', blank=True, max_length=2000)),
                ('target', models.CharField(verbose_name='Target', blank=True, choices=[('_self', 'Self window'), ('_blank', 'Blank window')], max_length=32)),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='BannerPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.SlugField(verbose_name='Slug', max_length=255, unique=True)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'BannerPlace',
                'verbose_name_plural': 'BannerPlaces',
            },
        ),
        migrations.AddField(
            model_name='banner',
            name='place',
            field=models.ForeignKey(verbose_name='BannerPlace', to='banners.BannerPlace'),
        ),
    ]
