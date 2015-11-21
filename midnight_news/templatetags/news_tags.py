from django import template
from midnight_news.models import News, Section

register = template.Library()


def show_news_line(slug=None, limit=3, **kwargs):

    if slug is None:
        section = None
        q = News.objects.published()
    else:
        section = Section.objects.get(slug=slug)
        q = News.objects.published().filter(sections__slug=slug)

    models = q.prefetch_related('sections').order_by('-date', '-id').all()[:limit]

    return {'models': models, 'section': section, 'data': kwargs}

register.inclusion_tag(file_name='news/tags/show_news_line.html', name='show_news_line')(show_news_line)
