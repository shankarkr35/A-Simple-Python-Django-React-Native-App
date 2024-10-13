from django import template

register = template.Library()

@register.simple_tag
def get_url_part(request, position):
    try:
        # Split the path and get the segment you need
        # path_segments = request.path.split('/')
        # segment = path_segments[3]  # 'edit-fleet' is the third segment in this example
        # id = path_segments[4]  # '2' is the fourth segment in this example
        return request.path.split('/')[position]
    except IndexError:
        return ''