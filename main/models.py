# -*- coding: utf-8 -*-

from django.db import models
from redactor.fields import RedactorField
from django.utils.translation import ugettext_lazy as _
from midnight.base_models import Base


class Page(Base):

    title = models.CharField(max_length=255)

    slug = models.SlugField(max_length=255, unique=True)

    text = RedactorField()

    class Meta:

        verbose_name = _(u'Page')

        verbose_name_plural = _(u'Pages')