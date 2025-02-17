import os

# Get the environment from an environment variable
DJANGO_ENV = os.getenv("DJANGO_ENV", "development").lower()

# Dynamically import the correct settings module
if DJANGO_ENV == "production":
    from baddy.settings.production import *
else:
    from baddy.settings.development import *
