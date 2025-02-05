from django import template
from django.contrib.auth.models import User

register = template.Library()


@register.filter(name="has_group")
def has_group(user: User, group_name: str):
    """Check if a user belongs to a specific group."""
    if user.is_superuser:
        return True
    return user.groups.filter(name=group_name).exists()
