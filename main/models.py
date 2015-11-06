# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User, UserManager, AbstractUser
from django.conf import settings


class AppUser(AbstractUser):

    phone = models.CharField(blank=True, max_length=10, verbose_name=_(u'Phone'))

    image = ImageField(upload_to='users', verbose_name=_(u'Image'), blank=True)

    objects = UserManager()


class Base(models.Model):

    active = models.BooleanField(default=True, verbose_name=_(u'Active'))

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'Author'))

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class BaseTree(MPTTModel):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name=_(u'Parent'))

    active = models.BooleanField(default=True, verbose_name=_(u'Active'))

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u'Author'))

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    def get_path(self):
        if hasattr(self, 'slug'):
            return '/'.join([item.slug for item in self.get_ancestors(include_self=True)])
        else:
            return None

    def has_childs(self):
        count = self.children.count()
        return count > 0

    class Meta:
        abstract = True


class Page(BaseTree):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    sort = models.IntegerField(default=500, verbose_name=_(u'Sort'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_(u'MetaTitle'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Description'))

    def get_absolute_url(self):
        return reverse('main:page_detail', kwargs={'path': self.get_path()})

    def __unicode__(self):
        return u'%s' % (self.title)

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _(u'Page')

        verbose_name_plural = _(u'Pages')


class IncludeArea(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    def __unicode__(self):
        return u'%s' % (self.title)

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

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:

        verbose_name = _(u'PhotoAlbum')

        verbose_name_plural = _(u'PhotoAlbums')


class Photo(Base):

    title = models.CharField(max_length=500, verbose_name=_(u'Title'))

    image = ImageField(upload_to='photos', verbose_name=_(u'Image'))

    album = models.ForeignKey(PhotoAlbum, verbose_name=_(u'PhotoAlbum'))

    sort = models.IntegerField(default=500, verbose_name=_(u'Sort'))

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:

        verbose_name = _(u'Photo')

        verbose_name_plural = _(u'Photos')
