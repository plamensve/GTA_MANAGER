from django import template

register = template.Library()


@register.filter
def placeholder(value, text_to_be_place):
    if hasattr(value, 'field') and hasattr(value.field.widget, 'attrs'):
        value.field.widget.attrs['placeholder'] = text_to_be_place
    return value

