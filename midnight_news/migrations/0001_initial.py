# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
import ckeditor.fields
import midnight_main.models
import mptt.fields
from midnight_news.models import Section, News


def create_news(*args):
    author = midnight_main.models.AppUser.objects.first()
    section = Section.objects.create(title="Новости компании", slug="company", author=author)
    news = News.objects.create(title='Поздравляем!', slug='welcome', annotation='Вы успешно установили систему.', text='Вы успешно установили систему.', date=datetime.date.today())
    news.sections.add(section)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('date', models.DateField(verbose_name='Date', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='news', verbose_name='Image', blank=True)),
                ('annotation', models.TextField(verbose_name='Annotation', blank=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('metatitle', models.CharField(verbose_name='Title', max_length=2000, blank=True)),
                ('keywords', models.CharField(verbose_name='Keywords', max_length=2000, blank=True)),
                ('description', models.CharField(verbose_name='Description', max_length=2000, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'News',
                'verbose_name': 'NewsItem',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('metatitle', models.CharField(verbose_name='Title', max_length=2000, blank=True)),
                ('keywords', models.CharField(verbose_name='Keywords', max_length=2000, blank=True)),
                ('description', models.CharField(verbose_name='Description', max_length=2000, blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, null=True, to='midnight_news.Section', verbose_name='Parent')),
            ],
            options={
                'verbose_name_plural': 'NewsSections',
                'verbose_name': 'NewsSection',
            },
            bases=(midnight_main.models.BreadCrumbsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='news',
            name='sections',
            field=mptt.fields.TreeManyToManyField(verbose_name='Sections', to='midnight_news.Section'),
        ),

        migrations.RunPython(create_news)

    ]
