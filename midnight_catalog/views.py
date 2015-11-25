from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from midnight_main.components import MetaSeo
from midnight_main.services import get_by_page
from .models import *


def index(request, slug=None):

    section = None

    if slug is None:
        q = Product.objects.published()
        meta = MetaSeo()
        meta.metatitle = _('Catalog')
        crumbs = [{'label': _('Catalog')}]
    else:
        section = Section.objects.get(slug=slug)

        if section is None:
            raise Http404('Section with slug "%s" not found' % slug)

        crumbs = section.get_breadcrumbs()

        meta = MetaSeo(section)

        q = Product.objects.published().filter(sections__slug=slug)

    q = q.prefetch_related('sections').order_by('-id')

    q = q.all()

    products = get_by_page(q, request.GET.get('page'), getattr(settings, 'MIDNIGHT_CATALOG_PAGE_SIZE', 20))

    return render(request, 'midnight_catalog/catalog/index.html', {'products': products, 'section': section, 'meta': meta, 'crumbs': crumbs})


def detail(request, section_slug, slug):

    item = Product.objects.published()\
        .prefetch_related(Prefetch("paramvalue_set", queryset=ParamValue.objects.published().prefetch_related("param")))\
        .filter(slug=slug).first()

    if not item:
        raise Http404('Item with slug "%s" not found' % slug)

    section = get_object_or_404(Section, slug=section_slug, active=True)

    crumbs = section.get_breadcrumbs(True) + [{'label': item.title}]

    text = Template(item.text).render(Context())

    meta = MetaSeo(item)

    return render(request, 'midnight_catalog/catalog/detail.html', {'item': item, 'text': text, 'meta': meta, 'crumbs': crumbs})

