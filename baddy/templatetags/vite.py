# myapp/templatetags/vite.py
from django import template
from django.templatetags.static import static

from baddy.context_processors import get_vite_asset

register = template.Library()


@register.simple_tag
def vite_asset(filename):
    """Returns the resolved Vite asset path with static helper."""
    hashed_filename = get_vite_asset(filename)
    return static(f'dist/{hashed_filename}')  # Prefix with static path
