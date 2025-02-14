from django.conf import settings


def project_version(request):
    """
    A little helper to get the project version from the settings
    """
    return {"PROJECT_VERSION": settings.VERSION}
