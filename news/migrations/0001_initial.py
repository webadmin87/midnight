# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import mptt.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('date', models.DateField(verbose_name='Date', blank=True)),
                ('image', models.FileField(upload_to=b'', verbose_name='Image', blank=True)),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', redactor.fields.RedactorField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(max_length=2000, verbose_name='Title', blank=True)),
                ('keywords', models.CharField(max_length=2000, verbose_name='Keywords', blank=True)),
                ('description', models.CharField(max_length=2000, verbose_name='Description', blank=True)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('metatitle', models.CharField(max_length=2000, verbose_name='Title', blank=True)),
                ('keywords', models.CharField(max_length=2000, verbose_name='Keywords', blank=True)),
                ('description', models.CharField(max_length=2000, verbose_name='Description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='Parent', blank=True, to='news.Section', null=True)),
            ],
            options={
                'verbose_name': 'NewsItem',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='sections',
            field=models.ManyToManyField(to='news.Section', verbose_name='Sections'),
        ),
    ]
