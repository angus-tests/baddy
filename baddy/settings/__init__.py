import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load environment variables from .env
load_dotenv(BASE_DIR / ".env")

# Get the environment from an environment variable
DJANGO_ENV = os.getenv("DJANGO_ENV", "development").lower()

# Dynamically import the correct settings module
if DJANGO_ENV == "production":
    from baddy.settings.production import *
else:
    from baddy.settings.development import *

# Import admin settings
from baddy.settings.admin import *  # noqa
