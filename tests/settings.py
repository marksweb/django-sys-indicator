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

ALLOWED_HOSTS: list[str] = ['*']

MIDDLEWARE: list[str] = ['django_sys_indicator.middleware.SystemIndicatorMiddleware']

ROOT_URLCONF = "tests.urls"
LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = False

if django.VERSION < (4, 0):
    USE_L10N = True

USE_TZ = True
