from django import template
from midnight_news.models import News, Section

register = template.Library()


def show_news_line(slug=None, limit=3, **kwargs):
    """
    Отображает список последних новостей

    Пример использования::

        {% show_news_line 'news_section_slug' 3 class='news-class' %}

    :param slug: символьный код категории новостей, если не задан фильтрация по категории не происходит
    :param limit: количество выводимых новостей
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """

    if slug is None:
        section = None
        q = News.objects.published()
    else:
        section = Section.objects.get(slug=slug)
        q = News.objects.published().filter(sections__slug=slug)

    models = q.prefetch_related('sections').order_by('-date', '-id').all()[:limit]

    return {'models': models, 'section': section, 'data': kwargs}

register.inclusion_tag(file_name='midnight_news/tags/show_news_line.html', name='show_news_line')(show_news_line)
