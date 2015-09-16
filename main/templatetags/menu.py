from django import template
from main.models import Menu

register = template.Library()

@register.inclusion_tag('main/menu/tpl.html')
def show_menu(slug, **kwargs):

    menu = Menu.objects.get(slug=slug)

    return {'menu': menu, 'data': kwargs}
