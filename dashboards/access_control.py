from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User

DASHBOARD_PERMISSIONS = {
    "dataset_dashboard": "dfts_team",
    "sdx_health_dashboard": "sdx_team",
    "secret_dashboard": "superusers",
}


def has_dashboard_access(user: User | AbstractBaseUser, dashboard_name: str) -> bool:
    """Check if the user has access to a specific dashboard."""
    if user.is_superuser:
        return True

    required_group = DASHBOARD_PERMISSIONS.get(dashboard_name)
    if not required_group:
        return False  # Dashboard not found in permissions

    return user.groups.filter(name=required_group).exists()
