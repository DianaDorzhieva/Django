from django import template

register = template.Library()



@register.simple_tag
def mediapath(image_path):
    if image_path:
        return f"/media/{image_path}"
    return '#'
