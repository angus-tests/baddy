import logging
import os

logger = logging.getLogger("gunicorn")

# Get the environment from an environment variable
DJANGO_ENV = os.getenv("DJANGO_ENV", "development").lower()

# Dynamically import the correct settings module
if DJANGO_ENV == "production":
    from baddy.settings.production import *
else:
    logger.info("Using development settings")
    from baddy.settings.development import *
