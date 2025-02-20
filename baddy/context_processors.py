from django.conf import settings


def project_version(request):
    """
    A little helper to get the project version from the settings
    """
    return {"PROJECT_VERSION": settings.VERSION}


def debug_flag(request):
    """Returns the DEBUG flag from the settings."""
    df = settings.DEBUG
    return {"DEBUG_FLAG": df}


def production_flag(request):
    """Returns the production flag from the settings."""
    prod = settings.DJANGO_ENV == "production"
    return {"PRODUCTION_FLAG": prod}
