from django.shortcuts import render, get_object_or_404
from django.template import Template, Context
from news.models import News, Section
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request, slug=None):

    section = None

    if slug is None:
        models = News.objects.published().all()
    else:
        section = Section.objects.get(slug=slug)
        models = News.objects.published().filter(sections__slug=slug).all()

    pager = Paginator(models, 1)

    page = request.GET.get('page')

    try:
        news = pager.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = pager.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = pager.page(pager.num_pages)

    return render(request, 'news/news/index.html', {'news': news, 'section': section, 'meta': section})


def detail(request, slug='main'):

    p = get_object_or_404(News, slug=slug)

    text = Template(p.text).render(Context())

    return render(request, 'news/news/detail.html', {'item': p, 'text': text})
