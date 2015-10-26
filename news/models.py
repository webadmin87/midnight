from django.db import models
from midnight.base_models import BaseTree, Base
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _


class Section(BaseTree):

    title = models.CharField(max_length=255, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    sort = models.IntegerField(default=500, verbose_name=_(u'Sort'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Description'))

    def __unicode__(self):
        return u'%s' % (self.title)

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _(u'NewsItem')

        verbose_name_plural = _(u'News')


class News(Base):

    title = models.CharField(max_length=255, verbose_name=_(u'Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_(u'Slug'))

    date = models.DateField(verbose_name=_(u'Date'), blank=True)

    sections = models.ManyToManyField(Section, verbose_name=_(u'Sections'))

    image = models.FileField(blank=True, verbose_name=_(u'Image'))

    annotation = models.TextField(blank=True, verbose_name=_(u'Annotation'))

    text = RedactorField(blank=True, verbose_name=_(u'Text'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_(u'Description'))