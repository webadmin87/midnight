# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('midnight_news', '0003_auto_20151122_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
                ('author', models.ForeignKey(blank=True, related_name='+', null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'NewsComments',
                'verbose_name': 'NewsComment',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.BooleanField(default=False, verbose_name='Comments'),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='obj',
            field=models.ForeignKey(to='midnight_news.News'),
        ),
        migrations.AddField(
            model_name='newscomment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, related_name='children', null=True, verbose_name='Parent', to='midnight_news.NewsComment'),
        ),
    ]
