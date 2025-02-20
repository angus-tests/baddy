# myapp/templatetags/vite.py
import json
import os

from django import template
from django.templatetags.static import static

from django.conf import settings


register = template.Library()


def get_vite_asset(file_name):
    """Reads Vite manifest to get the hashed asset file."""
    manifest_path = os.path.join(
        settings.BASE_DIR, "static", "dist", ".vite/manifest.json"
    )
    try:
        with open(manifest_path, "r") as manifest_file:
            manifest = json.load(manifest_file)
    except FileNotFoundError:
        return file_name

    # The `file_name` should be the original name without hash
    return manifest.get(file_name, {}).get("file", file_name)


@register.simple_tag
def vite_asset(filename):
    """Returns the resolved Vite asset path with static helper."""
    hashed_filename = get_vite_asset(filename)
    return static(f"dist/{hashed_filename}")  # Prefix with static path
