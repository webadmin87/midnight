from django import template
from main.models import IncludeArea

register = template.Library()


@register.simple_tag()
def show_area(slug):

    try:
        area = IncludeArea.objects.published().get(slug=slug)
        return area.text
    except IncludeArea.DoesNotExist:
        return ""

