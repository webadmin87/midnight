from django import template
from main.models import PhotoAlbum

register = template.Library()


def show_gallery(slug, size="100x100", crop="center", **kwargs):

    try:
        album = PhotoAlbum.objects.published().get(slug=slug)
        photos = album.photo_set.published().order_by('sort').all()
        return {'album': album, 'photos': photos, 'size': size, 'crop': crop, 'data': kwargs}
    except PhotoAlbum.DoesNotExist:
        return None

register.inclusion_tag(file_name='main/gallery/show_gallery.html', name='show_gallery')(show_gallery)
