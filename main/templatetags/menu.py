from django import template
from main.models import Menu

register = template.Library()


@register.inclusion_tag('main/menu/tpl.html')
def show_menu(slug, **kwargs):

    try:
        menu = Menu.objects.published().get(slug=slug)
        return {'menu': menu, 'data': kwargs}
    except Menu.DoesNotExist:
        return None

