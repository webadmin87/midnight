# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import mptt.fields
import main.models
from django.conf import settings
import sorl.thumbnail.fields
from news.models import Section, News
import datetime


def create_news(*args):
    author = main.models.AppUser.objects.first()
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('date', models.DateField(blank=True, verbose_name='Date')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='news', verbose_name='Image')),
                ('annotation', models.TextField(blank=True, verbose_name='Annotation')),
                ('text', redactor.fields.RedactorField(blank=True, verbose_name='Text')),
                ('metatitle', models.CharField(max_length=2000, blank=True, verbose_name='Title')),
                ('keywords', models.CharField(max_length=2000, blank=True, verbose_name='Keywords')),
                ('description', models.CharField(max_length=2000, blank=True, verbose_name='Description')),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News',
                'verbose_name': 'NewsItem',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('metatitle', models.CharField(max_length=2000, blank=True, verbose_name='Title')),
                ('keywords', models.CharField(max_length=2000, blank=True, verbose_name='Keywords')),
                ('description', models.CharField(max_length=2000, blank=True, verbose_name='Description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(null=True, verbose_name='Parent', blank=True, related_name='children', to='news.Section')),
            ],
            options={
                'verbose_name_plural': 'NewsSections',
                'verbose_name': 'NewsSection',
            },
            bases=(main.models.BreadCrumbsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='news',
            name='sections',
            field=mptt.fields.TreeManyToManyField(to='news.Section', verbose_name='Sections'),
        ),

        migrations.RunPython(create_news)

    ]

