from django import template
from django.contrib.auth.models import User

from apps.dashboards.access_control import has_dashboard_access

register = template.Library()


@register.filter(name="can_view_dashboard")
def can_view_dashboard(user: User, dashboard_name: str):
    """
    A template filter to check if a user can view a dashboard
    """
    return has_dashboard_access(user, dashboard_name)
