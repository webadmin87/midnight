# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import midnight_main.models
import django.utils.timezone
import mptt.fields
import django.core.validators
import ckeditor.fields
import sorl.thumbnail.fields
import django.contrib.auth.models
from django.conf import settings


def create_super_user(*args):
    midnight_main.models.AppUser.objects.create_superuser(username='admin', password='admin', email='webadmin87@gmil.com')


def create_pages(*args):
    author = midnight_main.models.AppUser.objects.first()
    midnight_main.models.Page.objects.create(title="Главная", slug=midnight_main.models.Page.MAIN_SLUG, text="Это главная страница", author=author)


def create_menu(*args):
    author = midnight_main.models.AppUser.objects.first()
    menu = midnight_main.models.Menu.objects.create(title='Главное меню', slug='main', author=author)
    midnight_main.models.Menu.objects.create(title='Главная', link='/', target='_self', parent=menu, author=author)


def create_ia(*args):
    author = midnight_main.models.AppUser.objects.first()
    midnight_main.models.IncludeArea.objects.create(title='Левая колонка', slug='left', text='Текст в левой клонке', author=author)


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], max_length=30, unique=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(blank=True, verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='last name', max_length=30)),
                ('email', models.EmailField(blank=True, verbose_name='email address', max_length=254)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, verbose_name='Phone', max_length=10)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='users', verbose_name='Image')),
                ('groups', models.ManyToManyField(blank=True, verbose_name='groups', related_query_name='user', related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(blank=True, verbose_name='user permissions', related_query_name='user', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IncludeArea',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Text')),
                ('author', models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'IncludeAreas',
                'verbose_name': 'IncludeArea',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.CharField(blank=True, verbose_name='Link', max_length=2000)),
                ('slug', models.SlugField(blank=True, verbose_name='Slug', max_length=255)),
                ('target', models.CharField(blank=True, verbose_name='Target', choices=[('_self', 'Self window'), ('_blank', 'Blank window')], max_length=32)),
                ('cls', models.CharField(blank=True, verbose_name='Cls', max_length=255)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, verbose_name='Parent', related_name='children', to='midnight_main.Menu')),
            ],
            options={
                'verbose_name_plural': 'Menu',
                'verbose_name': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Text')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('comments', models.BooleanField(default=False, verbose_name='Comments')),
                ('tpl', models.CharField(default='midnight_main/pages/pages.html', max_length=255, verbose_name='Template', choices=[('midnight_main/pages/pages.html', 'Simple page'), ('midnight_main/pages/guestbook.html', 'Guestbook')])),
                ('metatitle', models.CharField(blank=True, verbose_name='MetaTitle', max_length=2000)),
                ('keywords', models.CharField(blank=True, verbose_name='Keywords', max_length=2000)),
                ('description', models.CharField(blank=True, verbose_name='Description', max_length=2000)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, verbose_name='Parent', related_name='children', to='midnight_main.Page')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'verbose_name': 'Page',
            },
            bases=(midnight_main.models.BreadCrumbsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PageComment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(blank=True, verbose_name='Email', max_length=255)),
                ('text', models.TextField(verbose_name='Comment')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('author', models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
                ('obj', models.ForeignKey(to='midnight_main.Page')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, verbose_name='Parent', related_name='children', to='midnight_main.PageComment')),
            ],
            options={
                'verbose_name_plural': 'PageComment',
                'verbose_name': 'PageComment',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='photos', verbose_name='Image')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
            ],
            options={
                'verbose_name_plural': 'Photos',
                'verbose_name': 'Photo',
            },
        ),
        migrations.CreateModel(
            name='PhotoAlbum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Text')),
                ('author', models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PhotoAlbums',
                'verbose_name': 'PhotoAlbum',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(to='midnight_main.PhotoAlbum', verbose_name='PhotoAlbum'),
        ),
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Author', to=settings.AUTH_USER_MODEL),
        ),

        migrations.RunPython(create_super_user),

        migrations.RunPython(create_pages),

        migrations.RunPython(create_menu),

        migrations.RunPython(create_ia)

    ]
