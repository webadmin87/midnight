from django.shortcuts import render
from news.models import News
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request, slug=None):

    models = News.objects.published().all()

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

    return render(request, 'news/news/index.html', {'news': news})
