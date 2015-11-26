from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.conf import settings

from midnight_catalog.models import Section
from midnight_main.services import mark_current_menus

register = template.Library()


@register.simple_tag()
def param_value(param_values, slug):
    for val in param_values:
        if val.param.slug == slug:
            return val.value
    return None


@register.simple_tag()
def param_title(param_values, slug):
    for val in param_values:
        if val.param.slug == slug:
            return val.param.title
    return None


@register.filter()
def currency(money):
    decimals = getattr(settings, 'MIDNIGHT_CATALOG_DECIMALS', 2)
    money = round(float(money), decimals)
    symbol = getattr(settings, 'MIDNIGHT_CATALOG_CURRENCY', 'руб')
    if decimals > 0:
        formatted = (str("%0."+str(decimals)+"f") % money)[-decimals-1:]
    else:
        formatted = ""
    return "%s%s %s" % (intcomma(int(money)), formatted, symbol)


def catalog_sections(context, slug=None, **kwargs):
    if slug is None:
        sections = Section.objects.published().all()
    else:
        section = Section.objects.get(slug=slug)
        sections = section.get_descendants().all()
    mark_current_menus(sections, context['request'].path_info)
    return {'sections': sections, 'data': kwargs}

register.inclusion_tag(file_name='midnight_catalog/tags/catalog_sections.html', takes_context=True, name='catalog_sections')(catalog_sections)
