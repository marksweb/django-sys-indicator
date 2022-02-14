from __future__ import annotations

from pathlib import Path

import django

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "NOTHERE"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "src" / "django_sys_indicator" / "templates"],
        "OPTIONS": {"context_processors": []},
    },
]

ALLOWED_HOSTS: list[str] = ['*']

MIDDLEWARE: list[str] = ['django_sys_indicator.middleware.SystemIndicatorMiddleware']

LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = False

if django.VERSION < (4, 0):
    USE_L10N = True

USE_TZ = True
