# segment_tags.py
from django import template

register = template.Library()

@register.simple_tag
def get_url_segment(request, position):
    try:
        return request.path.split('/')[position]
    except IndexError:
        return ''

@register.filter
def extract_url_segment(request, position):
    try:
        return request.path.split('/')[position]
    except IndexError:
        return ''
