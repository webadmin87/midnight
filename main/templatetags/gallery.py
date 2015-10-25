from django import template
from main.models import PhotoAlbum

register = template.Library()


@register.inclusion_tag('main/gallery/tpl.html')
def show_gallery(slug, size="100x100", crop="center", **kwargs):

    try:
        album = PhotoAlbum.objects.published().get(slug=slug)
        photos = album.photo_set.published().order_by('sort').all()
        return {'album': album, 'photos': photos, 'size': size, 'crop': crop, 'data': kwargs}
    except PhotoAlbum.DoesNotExist:
        return None
