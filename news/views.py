from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from midnight.components import MetaSeo
from news.models import News, Section
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


def index(request, slug=None):

    section = None

    if slug is None:
        q = News.objects.published()
        meta = MetaSeo()
        meta.metatitle = _('News')
    else:
        section = Section.objects.get(slug=slug)

        if section is None:
            raise Http404('Section with slug "%s" not found' % slug)

        meta = MetaSeo(section)

        q = News.objects.published().filter(sections__slug=slug)

    q = q.order_by('-date', '-id')

    models = q.all()

    pager = Paginator(models, settings.NEWS_PAGE_SIZE)

    page = request.GET.get('page')

    try:
        news = pager.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = pager.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = pager.page(pager.num_pages)

    return render(request, 'news/news/index.html', {'news': news, 'section': section, 'meta': meta})


def detail(request, slug='main'):

    item = get_object_or_404(News, slug=slug)

    text = Template(item.text).render(Context())

    meta = MetaSeo(item)

    return render(request, 'news/news/detail.html', {'item': item, 'text': text, 'meta': meta})
