from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from midnight_main.components import MetaSeo
from midnight_main.services import get_by_page, get_object_comments, get_comment_init
from midnight_news.forms import NewsCommentForm
from midnight_news.models import News, Section, NewsComment


def index(request, slug=None):

    section = None

    if slug is None:
        q = News.objects.published()
        meta = MetaSeo()
        meta.metatitle = _('News')
        crumbs = [{'label': _('News')}]
    else:
        section = Section.objects.get(slug=slug)

        if section is None:
            raise Http404('Section with slug "%s" not found' % slug)

        crumbs = section.get_breadcrumbs()

        meta = MetaSeo(section)

        q = News.objects.published().filter(sections__slug=slug)

    q = q.prefetch_related('sections').order_by('-date', '-id')

    q = q.all()

    news = get_by_page(q, request.GET.get('page'), getattr(settings, 'MIDNIGHT_NEWS_PAGE_SIZE', 20))

    return render(request, 'midnight_news/news/index.html', {'news': news, 'section': section, 'meta': meta, 'crumbs': crumbs})


def detail(request, section_slug, slug):

    item = get_object_or_404(News, slug=slug, active=True)

    section = get_object_or_404(Section, slug=section_slug, active=True)

    crumbs = section.get_breadcrumbs(True) + [{'label': item.title}]

    text = Template(item.text).render(Context())

    meta = MetaSeo(item)

    comments = get_object_comments(NewsComment, item.id)

    comments_form = NewsCommentForm(initial=get_comment_init(request, item))

    return render(request, 'midnight_news/news/detail.html', {'item': item, 'text': text, 'meta': meta, 'crumbs': crumbs, 'comments': comments, 'comments_form': comments_form})
