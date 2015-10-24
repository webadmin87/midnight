# -*- coding: utf-8 -*-

from django.db import models
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from midnight.base_models import Base, BaseTree
from sorl.thumbnail import ImageField


class Page(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_(u'MetaTitle'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Description'))

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:

        verbose_name = _(u'Page')

        verbose_name_plural = _(u'Pages')


class IncludeArea(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    class Meta:

        verbose_name = _(u'IncludeArea')

        verbose_name_plural = _(u'IncludeAreas')


class Menu(BaseTree):

    TARGET_CHOICES = (
        ('_self', _(u'Self window')),
        ('_blank', _(u'Blank window')),
    )

    title = models.CharField(max_length=255, verbose_name=_(u'Title'))

    link = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Link'))

    slug = models.SlugField(max_length=255, blank=True, verbose_name=_(u'Slug'))

    target = models.CharField(max_length=32, blank=True, verbose_name=_(u'Target'), choices=TARGET_CHOICES)

    cls = models.CharField(max_length=255, blank=True, verbose_name=_(u'Cls'))

    sort = models.IntegerField(default=500, verbose_name=_(u'Sort'))

    def __unicode__(self):
        return u'%s' % (self.title)

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _(u'Menu')

        verbose_name_plural = _(u'Menu')


class PhotoAlbum(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    class Meta:

        verbose_name = _(u'PhotoAlbum')

        verbose_name_plural = _(u'PhotoAlbum')


class Photo(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    image = ImageField(upload_to='photos')

    album = models.ForeignKey(PhotoAlbum)

    class Meta:

        verbose_name = _(u'Photo')

        verbose_name_plural = _(u'Photo')