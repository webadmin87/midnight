from django import template
from main.models import Menu

register = template.Library()


def show_menu(slug, **kwargs):

    try:
        menu = Menu.objects.published().get(slug=slug)
        return {'menu': menu, 'data': kwargs}
    except Menu.DoesNotExist:
        return None

register.inclusion_tag(file_name='main/menu/show_menu.html', name='show_menu')(show_menu)

