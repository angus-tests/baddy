from .base import *  # noqa

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# Security
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-1nze18c1fv*tq2%0#z%bo4uagwis5h27sco#w9efukqoi(__iz')

ALLOWED_HOSTS = ["*"]

# SQLite for Dev
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Auth Validators
AUTH_PASSWORD_VALIDATORS = []

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.23',
)


CORS_ALLOW_ALL_ORIGINS = True

