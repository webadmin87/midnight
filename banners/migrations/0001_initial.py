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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('file', models.FileField(upload_to='banners', verbose_name='File')),
                ('link', models.CharField(max_length=2000, blank=True, verbose_name='Link')),
                ('target', models.CharField(verbose_name='Target', choices=[('_self', 'Self window'), ('_blank', 'Blank window')], blank=True, max_length=32)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='BannerPlace',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
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
