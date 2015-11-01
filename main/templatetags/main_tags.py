from django import template
from main.models import Menu, PhotoAlbum, IncludeArea

register = template.Library()


def show_menu(slug, **kwargs):

    try:
        menu = Menu.objects.published().get(slug=slug)
        return {'menu': menu, 'data': kwargs}
    except Menu.DoesNotExist:
        return None

register.inclusion_tag(file_name='main/tags/show_menu.html', name='show_menu')(show_menu)


def show_gallery(slug, size="100x100", crop="center", **kwargs):

    try:
        album = PhotoAlbum.objects.published().get(slug=slug)
        photos = album.photo_set.published().order_by('sort').all()
        return {'album': album, 'photos': photos, 'size': size, 'crop': crop, 'data': kwargs}
    except PhotoAlbum.DoesNotExist:
        return None

register.inclusion_tag(file_name='main/tags/show_gallery.html', name='show_gallery')(show_gallery)


@register.simple_tag()
def show_area(slug):

    try:
        area = IncludeArea.objects.published().get(slug=slug)
        return area.text
    except IncludeArea.DoesNotExist:
        return ""
