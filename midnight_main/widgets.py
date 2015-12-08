from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail


class AdminImageWidget(AdminFileWidget):
    """
    Поле загрузки файла с превью загруженного изображения
    """
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value,'80x80')
            output.append('<img src="{}">'.format(t.url))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
