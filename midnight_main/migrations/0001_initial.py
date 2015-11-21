# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import django.contrib.auth.models
from django.conf import settings
import ckeditor.fields
import midnight_main.models
import django.utils.timezone
import django.core.validators
import mptt.fields


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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}, unique=True, verbose_name='username', max_length=30, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30, blank=True)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30, blank=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=254, blank=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(verbose_name='Phone', max_length=10, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='users', verbose_name='Image', blank=True)),
                ('groups', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', verbose_name='groups', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', blank=True, related_query_name='user', verbose_name='user permissions', to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='IncludeArea',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'IncludeAreas',
                'verbose_name': 'IncludeArea',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('link', models.CharField(verbose_name='Link', max_length=2000, blank=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', blank=True)),
                ('target', models.CharField(verbose_name='Target', max_length=32, blank=True, choices=[('_self', 'Self window'), ('_blank', 'Blank window')])),
                ('cls', models.CharField(verbose_name='Cls', max_length=255, blank=True)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, null=True, to='midnight_main.Menu', verbose_name='Parent')),
            ],
            options={
                'verbose_name_plural': 'Menu',
                'verbose_name': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('comments', models.BooleanField(default=False, verbose_name='Comments')),
                ('metatitle', models.CharField(verbose_name='MetaTitle', max_length=2000, blank=True)),
                ('keywords', models.CharField(verbose_name='Keywords', max_length=2000, blank=True)),
                ('description', models.CharField(verbose_name='Description', max_length=2000, blank=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, null=True, to='midnight_main.Page', verbose_name='Parent')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(verbose_name='Username', max_length=255)),
                ('email', models.EmailField(verbose_name='Email', max_length=255, blank=True)),
                ('text', models.TextField(verbose_name='Comment')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
                ('obj', models.ForeignKey(to='midnight_main.Page')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, null=True, to='midnight_main.PageComment', verbose_name='Parent')),
            ],
            options={
                'verbose_name_plural': 'PageComment',
                'verbose_name': 'PageComment',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(verbose_name='Title', max_length=500)),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True)),
                ('text', ckeditor.fields.RichTextField(verbose_name='Text', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author')),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, verbose_name='Author'),
        ),

        migrations.RunPython(create_super_user),

        migrations.RunPython(create_pages),

        migrations.RunPython(create_menu),

        migrations.RunPython(create_ia)

    ]
