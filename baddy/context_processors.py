import json
import os

from django.conf import settings


def project_version(request):
    """
    A little helper to get the project version from the settings
    """
    return {"PROJECT_VERSION": settings.VERSION}


def debug_flag(request):
    df = settings.DEBUG
    return {"DEBUG_FLAG": df}


def production_flag(request):
    prod = settings.DJANGO_ENV == "production"
    return {"PRODUCTION_FLAG": prod}


def get_vite_asset(file_name):
    """Reads Vite manifest to get the hashed asset file."""
    manifest_path = os.path.join(settings.BASE_DIR, 'static', 'dist', '.vite/manifest.json')
    with open(manifest_path, 'r') as manifest_file:
        manifest = json.load(manifest_file)

    # The `file_name` should be the original name without hash
    return manifest.get(file_name, {}).get('file', file_name)
