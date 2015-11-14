from django.db import models
from main.models import Base
from django.utils.translation import ugettext_lazy as _


class BannerPlace(Base):

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_('Slug'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('BannerPlace')

        verbose_name_plural = _('BannerPlaces')


class Banner(Base):

    TARGET_CHOICES = (
        ('_self', _('Self window')),
        ('_blank', _('Blank window')),
    )

    title = models.CharField(max_length=500, verbose_name=_('Title'))

    file = models.FileField(upload_to='banners', verbose_name=_('File'))

    link = models.CharField(max_length=2000, blank=True, verbose_name=_('Link'))

    target = models.CharField(max_length=32, blank=True, verbose_name=_('Target'), choices=TARGET_CHOICES)

    width = models.IntegerField(verbose_name=_('Width'))

    height = models.IntegerField(verbose_name=_('Height'))

    text = models.TextField(blank=True, verbose_name=_('Text'))

    place = models.ForeignKey(BannerPlace, verbose_name=_('BannerPlace'))

    sort = models.IntegerField(default=500, verbose_name=_('Sort'))

    def __str__(self):
        return self.title

    class Meta:

        verbose_name = _('Banner')

        verbose_name_plural = _('Banners')
