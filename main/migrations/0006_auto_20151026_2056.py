# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_photo_sort'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='photoalbum',
            options={'verbose_name': 'PhotoAlbum', 'verbose_name_plural': 'PhotoAlbums'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(verbose_name='PhotoAlbum', to='main.PhotoAlbum'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'photos', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='sort',
            field=models.IntegerField(default=500, verbose_name='Sort'),
        ),
    ]
