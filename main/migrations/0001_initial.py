# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import django.contrib.auth.models
import mptt.fields
import main.models
import django.core.validators
from django.conf import settings
import django.utils.timezone
import sorl.thumbnail.fields


def create_super_user(*args):
    main.models.AppUser.objects.create_superuser(username='admin', password='admin', email='webadmin87@gmil.com')


def create_pages(*args):
    author = main.models.AppUser.objects.first()
    main.models.Page.objects.create(title="Главная", slug=main.models.Page.MAIN_SLUG, text="Это главная страница", author=author)


def create_menu(*args):
    author = main.models.AppUser.objects.first()
    menu = main.models.Menu.objects.create(title='Главное меню', slug='main', author=author)
    main.models.Menu.objects.create(title='Главная', link='/', target='_self', parent=menu, author=author)


def create_ia(*args):
    author = main.models.AppUser.objects.first()
    main.models.IncludeArea.objects.create(title='Левая колонка', slug='left', text='Текст в левой клонке', author=author)


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=30, unique=True, error_messages={'unique': 'A user with that username already exists.'}, verbose_name='username', help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status', help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active', help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=10, blank=True, verbose_name='Phone')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='users', verbose_name='Image')),
                ('groups', models.ManyToManyField(related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, verbose_name='groups', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.', blank=True, verbose_name='user permissions', to='auth.Permission')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', redactor.fields.RedactorField(blank=True, verbose_name='Text')),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'IncludeAreas',
                'verbose_name': 'IncludeArea',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.CharField(max_length=2000, blank=True, verbose_name='Link')),
                ('slug', models.SlugField(max_length=255, blank=True, verbose_name='Slug')),
                ('target', models.CharField(max_length=32, blank=True, choices=[('_self', 'Self window'), ('_blank', 'Blank window')], verbose_name='Target')),
                ('cls', models.CharField(max_length=255, blank=True, verbose_name='Cls')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(null=True, verbose_name='Parent', blank=True, related_name='children', to='main.Menu')),
            ],
            options={
                'verbose_name_plural': 'Menu',
                'verbose_name': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', redactor.fields.RedactorField(blank=True, verbose_name='Text')),
                ('sort', models.IntegerField(default=500, verbose_name='Sort')),
                ('comments', models.BooleanField(default=False, verbose_name='Comments')),
                ('metatitle', models.CharField(max_length=2000, blank=True, verbose_name='MetaTitle')),
                ('keywords', models.CharField(max_length=2000, blank=True, verbose_name='Keywords')),
                ('description', models.CharField(max_length=2000, blank=True, verbose_name='Description')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
                ('parent', mptt.fields.TreeForeignKey(null=True, verbose_name='Parent', blank=True, related_name='children', to='main.Page')),
            ],
            options={
                'verbose_name_plural': 'Pages',
                'verbose_name': 'Page',
            },
            bases=(main.models.BreadCrumbsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PageComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, blank=True, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Comment')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
                ('obj', models.ForeignKey(to='main.Page')),
                ('parent', mptt.fields.TreeForeignKey(null=True, verbose_name='Parent', blank=True, related_name='children', to='main.PageComment')),
            ],
            options={
                'verbose_name_plural': 'PageComment',
                'verbose_name': 'PageComment',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('text', redactor.fields.RedactorField(blank=True, verbose_name='Text')),
                ('author', models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PhotoAlbums',
                'verbose_name': 'PhotoAlbum',
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(to='main.PhotoAlbum', verbose_name='PhotoAlbum'),
        ),
        migrations.AddField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(null=True, verbose_name='Author', blank=True, to=settings.AUTH_USER_MODEL),
        ),

        migrations.RunPython(create_super_user),

        migrations.RunPython(create_pages),

        migrations.RunPython(create_menu),

        migrations.RunPython(create_ia)

    ]

