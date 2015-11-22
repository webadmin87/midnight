# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import ckeditor.fields
import mptt.fields
import sorl.thumbnail.fields
import midnight_main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('measurement', models.CharField(verbose_name='Measurement', max_length=32)),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Param',
                'verbose_name_plural': 'Params',
            },
        ),
        migrations.CreateModel(
            name='ParamGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ParamGroup',
                'verbose_name_plural': 'ParamGroups',
            },
        ),
        migrations.CreateModel(
            name='ParamValue',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(verbose_name='Value', max_length=2000)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('param', models.ForeignKey(to='midnight_catalog.Param', verbose_name='Param')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', max_length=255)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', blank=True, upload_to='catalog')),
                ('price', models.DecimalField(decimal_places=2, verbose_name='Price', blank=True, max_digits=11)),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(verbose_name='Title', blank=True, max_length=2000)),
                ('keywords', models.CharField(verbose_name='Keywords', blank=True, max_length=2000)),
                ('description', models.CharField(verbose_name='Description', blank=True, max_length=2000)),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='products')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(to='midnight_catalog.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug', max_length=255)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', blank=True, upload_to='catalog')),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(verbose_name='Title', blank=True, max_length=2000)),
                ('keywords', models.CharField(verbose_name='Keywords', blank=True, max_length=2000)),
                ('description', models.CharField(verbose_name='Description', blank=True, max_length=2000)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(related_name='+', null=True, blank=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', null=True, blank=True, verbose_name='Parent', to='midnight_catalog.Section')),
            ],
            options={
                'verbose_name': 'CatalogSection',
                'verbose_name_plural': 'CatalogSections',
            },
            bases=(midnight_main.models.BreadCrumbsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='product',
            name='sections',
            field=mptt.fields.TreeManyToManyField(to='midnight_catalog.Section', verbose_name='Sections'),
        ),
        migrations.AddField(
            model_name='paramvalue',
            name='product',
            field=models.ForeignKey(to='midnight_catalog.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='param',
            name='group',
            field=models.ForeignKey(to='midnight_catalog.ParamGroup', verbose_name='ParamGroup'),
        ),
    ]
