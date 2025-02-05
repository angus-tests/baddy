from django import template
from django.contrib.auth.models import User

from dashboards.access_control import has_dashboard_access

register = template.Library()


@register.filter(name="can_view_dashboard")
def can_view_dashboard(user: User, dashboard_name: str):
    """Check if a user belongs to a specific group."""
    return has_dashboard_access(user, dashboard_name)
