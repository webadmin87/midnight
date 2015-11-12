# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, blank=True)),
                ('text', models.TextField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'verbose_name': 'PageComment',
                'verbose_name_plural': 'PageComment',
            },
        ),
        migrations.AlterField(
            model_name='appuser',
            name='image',
            field=sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='users', blank=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='target',
            field=models.CharField(verbose_name='Target', max_length=32, choices=[('_self', 'Self window'), ('_blank', 'Blank window')], blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='photos'),
        ),
        migrations.AddField(
            model_name='pagecomment',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='pagecomment',
            name='obj',
            field=models.ForeignKey(to='main.Page'),
        ),
        migrations.AddField(
            model_name='pagecomment',
            name='parent',
            field=mptt.fields.TreeForeignKey(verbose_name='Parent', to='main.PageComment', related_name='children', blank=True, null=True),
        ),
    ]
