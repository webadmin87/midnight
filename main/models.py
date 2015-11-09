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

    phone = models.CharField(blank=True, max_length=10, verbose_name=_('Phone'))

    image = ImageField(upload_to='users', verbose_name=_('Image'), blank=True)

    objects = UserManager()


class Base(models.Model):

    active = models.BooleanField(default=True, verbose_name=_('Active'))

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Author'))

    created_at = models.DateTimeField(auto_now_add=True)

    update_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True


class BaseTree(MPTTModel):

    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name=_('Parent'))

    active = models.BooleanField(default=True, verbose_name=_('Active'))

    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Author'))

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


class BreadCrumbsMixin(object):
    def get_breadcrumbs(self, self_url=False):
        crumbs = [{'label': item.title, 'url': item.get_absolute_url()} for item in self.get_ancestors()]
        if self_url:
            crumbs += [{'label': self.title, 'url': self.get_absolute_url()}]
        else:
            crumbs += [{'label': self.title}]
        return crumbs


class Page(BreadCrumbsMixin, BaseTree):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    text = RedactorField(blank=True, verbose_name=_('Text'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_('MetaTitle'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_('Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_('Description'))

    def get_absolute_url(self):
        return reverse('main:page_detail', kwargs={'path': self.get_path()})

    def __str__(self):
        return self.title

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _('Page')

        verbose_name_plural = _('Pages')


class IncludeArea(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    text = RedactorField(blank=True, verbose_name=_('Text'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('IncludeArea')

        verbose_name_plural = _('IncludeAreas')


class Menu(BaseTree):

    TARGET_CHOICES = (
        ('_self', _('Self window')),
        ('_blank', _('Blank window')),
    )

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    link = models.CharField(max_length=2000, blank=True, verbose_name=_('Link'))

    slug = models.SlugField(max_length=255, blank=True, verbose_name=_('Slug'))

    target = models.CharField(max_length=32, blank=True, verbose_name=_('Target'), choices=TARGET_CHOICES)

    cls = models.CharField(max_length=255, blank=True, verbose_name=_('Cls'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    def __str__(self):
        return self.title

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _('Menu')

        verbose_name_plural = _('Menu')


class PhotoAlbum(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    text = RedactorField(blank=True, verbose_name=_('Text'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('PhotoAlbum')

        verbose_name_plural = _('PhotoAlbums')


class Photo(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    image = ImageField(upload_to='photos', verbose_name=_('Image'))

    album = models.ForeignKey(PhotoAlbum, verbose_name=_('PhotoAlbum'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('Photo')

        verbose_name_plural = _('Photos')
