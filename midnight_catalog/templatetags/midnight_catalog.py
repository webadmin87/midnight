from django import template

register = template.Library()


@register.simple_tag()
def param_value(param_values, slug):
    for val in param_values:
        if val.param.slug == slug:
            return val.value
    return None
