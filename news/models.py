from django.db import models
from main.models import BaseTree, Base
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from mptt.fields import TreeManyToManyField


class Section(BaseTree):

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_('Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_('Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _('NewsSection')

        verbose_name_plural = _('NewsSections')


class News(Base):

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    date = models.DateField(verbose_name=_('Date'), blank=True)

    sections = TreeManyToManyField(Section, verbose_name=_('Sections'))

    image = ImageField(upload_to='news', verbose_name=_('Image'), blank=True)

    annotation = models.TextField(blank=True, verbose_name=_('Annotation'))

    text = RedactorField(blank=True, verbose_name=_('Text'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_('Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_('Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('NewsItem')

        verbose_name_plural = _('News')
