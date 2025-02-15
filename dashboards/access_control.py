from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

from dashboards.models import Dashboard


def has_dashboard_access(user, dashboard_slug: str) -> bool:
    """
    Helper function to check if a user has access to a dashboard.
    :param user: User to check access for
    :param dashboard_slug: Slug of the dashboard to check access for
    :return:  True if the user has access to the dashboard, False otherwise
    """

    # Staff and superusers have access to all dashboards
    if user.is_superuser or user.is_staff:
        return True

    # Check the users groups to see if they have access to the dashboard
    return Dashboard.objects.filter(slug=dashboard_slug, allowed_groups__in=user.groups.all()).exists()
