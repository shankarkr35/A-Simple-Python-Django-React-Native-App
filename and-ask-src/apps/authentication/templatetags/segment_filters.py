# segment_filters.py
from django import template

register = template.Library()

@register.filter
def get_url_segment(request, position):
    try:
        return request.path.split('/')[position]
    except IndexError:
        return ''
