import os
import uuid


def swf_renderer(banner, cls="banners-swf"):
    tag_id = uuid.uuid4().hex[:6].lower()
    return '<div class="%s" data-path="%s" data-width="%s" data-height="%s" id="%s"></div>' % (cls, banner.file.url, banner.width, banner.height, tag_id)


def img_renderer(banner):
    img = '<img src="%s" width="%s" height="%s" alt="%s" />' % (banner.file.url, banner.width, banner.height, banner.title)
    if banner.link:
        return '<a href="%s" target="%s">%s</a>' % (banner.link, banner.target, img)
    else:
        return img


def get_renderer(banner):
    filename, file_extension = os.path.splitext(banner.file.name)
    if file_extension.lower() == '.swf':
        return swf_renderer
    else:
        return img_renderer
