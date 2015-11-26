from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.conf import settings

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

