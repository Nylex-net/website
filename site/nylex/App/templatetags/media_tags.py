from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def media_url(file_path):
    """
    Custom template tag to generate media URLs.
    """
    media_url = settings.MEDIA_URL
    return f"{media_url}{file_path}"