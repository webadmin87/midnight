from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from mptt.fields import TreeManyToManyField
from sorl.thumbnail import ImageField
from midnight_main.models import Base, BreadCrumbsMixin, BaseTree
from django.utils.translation import ugettext_lazy as _


class Section(BreadCrumbsMixin, BaseTree):

    is_current = False

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    image = ImageField(upload_to='catalog', verbose_name=_('Image'), blank=True)

    annotation = models.TextField(blank=True, verbose_name=_('Annotation'))

    text = RichTextField(blank=True, verbose_name=_('Text'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_('Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_('Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_('Description'))

    def get_absolute_url(self):
        return reverse('midnight_catalog:catalog_list', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class MPTTMeta:

        order_insertion_by = ['sort']

    class Meta:

        verbose_name = _('CatalogSection')

        verbose_name_plural = _('CatalogSections')


class Product(Base):

    title = models.CharField(max_length=255, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    sections = TreeManyToManyField(Section, verbose_name=_('Sections'))

    image = ImageField(upload_to='catalog', verbose_name=_('Image'), blank=True)

    price = models.DecimalField(verbose_name=_('Price'), default=0, max_digits=11, decimal_places=2)

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    annotation = models.TextField(blank=True, verbose_name=_('Annotation'))

    text = RichTextField(blank=True, verbose_name=_('Text'))

    metatitle = models.CharField(max_length=2000, blank=True, verbose_name=_('Title'))

    keywords = models.CharField(max_length=2000, blank=True, verbose_name=_('Keywords'))

    description = models.CharField(max_length=2000, blank=True, verbose_name=_('Description'))

    def get_absolute_url(self):
        return reverse('midnight_catalog:catalog_detail', kwargs={'section_slug': self.sections.all()[0].slug, 'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('Product')

        verbose_name_plural = _('Products')


class ProductPhoto(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    image = ImageField(upload_to='products', verbose_name=_('Image'))

    product = models.ForeignKey(Product, verbose_name=_('Product'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('Photo')

        verbose_name_plural = _('Photos')


class ParamGroup(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('ParamGroup')

        verbose_name_plural = _('ParamGroups')


class Param(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    measurement = models.CharField(max_length=32, verbose_name=_('Measurement'), blank=True)

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    group = models.ForeignKey(ParamGroup, verbose_name=_('ParamGroup'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('Param')

        verbose_name_plural = _('Params')


class ParamValue(Base):

    product = models.ForeignKey(Product, verbose_name=_('Product'))

    param = models.ForeignKey(Param, verbose_name=_('Param'))

    value = models.CharField(max_length=2000, verbose_name=_('Value'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    def __str__(self):
        return _("ParamValue")

    class Meta:

        verbose_name = _('ParamValue')

        verbose_name_plural = _('ParamValues')


