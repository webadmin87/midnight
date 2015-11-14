from banners.models import BannerPlace
from banners.renderers import get_renderer
from django import template

register = template.Library()


@register.simple_tag()
def one_banner(slug):
    place = BannerPlace.objects.published().get(slug=slug)
    banner = place.banner_set.published().order_by('?').first()
    renderer = get_renderer(banner)
    return renderer(banner)


def list_banners(slug, **kwargs):
    place = BannerPlace.objects.published().get(slug=slug)
    banners = place.banner_set.published().order_by('sort').all()
    rendered = []
    for banner in banners:
        renderer = get_renderer(banner)
        rendered.append(renderer(banner))
    return {'rendered': rendered, 'banners': banners, 'data': kwargs}

register.inclusion_tag(file_name='banners/tags/list_banners.html', name='list_banners')(list_banners)