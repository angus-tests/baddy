from django import template

from baddy.context_processors import get_vite_asset

register = template.Library()


@register.simple_tag
def vite_asset(filename):
    """Returns the resolved Vite asset path."""
    return get_vite_asset(filename)
