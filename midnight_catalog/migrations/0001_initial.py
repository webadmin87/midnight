# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
import ckeditor.fields
import midnight_main.models
from django.conf import settings
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Param',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('measurement', models.CharField(max_length=32, verbose_name='Measurement', blank=True)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Param',
                'verbose_name_plural': 'Params',
            },
        ),
        migrations.CreateModel(
            name='ParamGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ParamGroup',
                'verbose_name_plural': 'ParamGroups',
            },
        ),
        migrations.CreateModel(
            name='ParamValue',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=2000, verbose_name='Value')),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('param', models.ForeignKey(verbose_name='Param', to='midnight_catalog.Param')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='catalog', blank=True)),
                ('price', models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=11, blank=True)),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(max_length=2000, verbose_name='Title', blank=True)),
                ('keywords', models.CharField(max_length=2000, verbose_name='Keywords', blank=True)),
                ('description', models.CharField(max_length=2000, verbose_name='Description', blank=True)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='products')),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(verbose_name='Product', to='midnight_catalog.Product')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('sort', models.IntegerField(verbose_name='Sort', default=500)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='catalog', blank=True)),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(max_length=2000, verbose_name='Title', blank=True)),
                ('keywords', models.CharField(max_length=2000, verbose_name='Keywords', blank=True)),
                ('description', models.CharField(max_length=2000, verbose_name='Description', blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(verbose_name='Author', blank=True, null=True, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(verbose_name='Parent', blank=True, null=True, related_name='children', to='midnight_catalog.Section')),
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
            field=mptt.fields.TreeManyToManyField(verbose_name='Sections', to='midnight_catalog.Section'),
        ),
        migrations.AddField(
            model_name='paramvalue',
            name='product',
            field=models.ForeignKey(verbose_name='Product', to='midnight_catalog.Product'),
        ),
        migrations.AddField(
            model_name='param',
            name='group',
            field=models.ForeignKey(verbose_name='ParamGroup', to='midnight_catalog.ParamGroup'),
        ),
    ]
