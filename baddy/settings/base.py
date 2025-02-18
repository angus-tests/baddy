import os
import tomllib
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Installed Apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "baddy",
    "dashboards",
    "accounts",
    "corsheaders"
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "baddy.context_processors.project_version",
                "baddy.context_processors.debug_flag",
                "baddy.context_processors.production_flag",
            ],
        },
    },
]

# Static Files
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

if os.getenv("DJANGO_ENV") == "development":
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


ROOT_URLCONF = "baddy.urls"
WSGI_APPLICATION = "baddy.wsgi.application"

# Authentication
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


# Internationalization
LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Markdown Config
MARKDOWNIFY = {
    "default": {
        "MARKDOWN_EXTENSIONS": [
            "markdown.extensions.fenced_code",
            "markdown.extensions.codehilite",
        ],
    }
}


# Version from pyproject.toml
POETRY_TOML = os.path.join(BASE_DIR, "pyproject.toml")


def get_version():
    try:
        with open(POETRY_TOML, "rb") as f:
            data = tomllib.load(f)
            return data["tool"]["poetry"]["version"]
    except (FileNotFoundError, KeyError):
        return "N/A"


VERSION = get_version()
