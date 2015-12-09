from midnight_banners.models import BannerPlace
from midnight_banners.renderers import get_renderer
from django import template

register = template.Library()


@register.simple_tag()
def one_banner(slug):
    """
    Служит для отображения одного случайного баннера из указанного баннерного места

    Пример использования::

        {% one_banner 'place_slug' %}

    :param slug: символьный код баннерного места
    :return:
    """
    place = BannerPlace.objects.published().get(slug=slug)
    banner = place.banner_set.published().order_by('?').first()
    renderer = get_renderer(banner)
    return renderer(banner)


def list_banners(slug, **kwargs):
    """
    Отображает все баннеры из указанного баннерного места

    Пример использования::

        {% list_banners 'place_slug' class='banners-class' %}

    :param slug: символьный код баннерного места
    :param kwargs: html атрибуты оборачивающего тега
    :return:
    """
    place = BannerPlace.objects.published().get(slug=slug)
    banners = place.banner_set.published().order_by('sort').all()
    rendered = []
    for banner in banners:
        renderer = get_renderer(banner)
        rendered.append(renderer(banner))
    return {'rendered': rendered, 'banners': banners, 'data': kwargs}

register.inclusion_tag(file_name='midnight_banners/tags/list_banners.html', name='list_banners')(list_banners)