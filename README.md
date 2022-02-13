# django-sys-indicator

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/marksweb/django-sys-indicator/main.svg)](https://results.pre-commit.ci/latest/github/marksweb/django-sys-indicator/main)
[![GitHub license](https://img.shields.io/github/license/marksweb/django-sys-indicator)](https://github.com/marksweb/django-sys-indicator/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/marksweb/django-sys-indicator)](https://github.com/marksweb/django-sys-indicator/issues)


A visual indicator of what environment/system you're using in django.

![system indicator examples](https://django-sys-indicator.s3.eu-west-2.amazonaws.com/screenshots/django-sys-indicator.jpg "Django system indicator")

To install:

* Add ``'django_sys_indicator.apps.DjangoSysIndicatorConfig'`` to your `INSTALLED_APPS`
* Add ``'django_sys_indicator.middleware.SystemIndicatorMiddleware'`` to you `MIDDLEWARE`


Configuration settings and their defaults

```python
SYSTEM_INDICATOR_ENABLED = False
SYSTEM_INDICATOR_LABEL = 'localhost'
SYSTEM_INDICATOR_COLORS = {
    # Format here is colour, border colour
    'red': ('#c50000', '#daa'),
    'blue': ('#006fc4', '#aad'),
    'green': ('#009e00', '#ada'),
    'purple': ('#800080', '#dad'),
    'orange': ('#ff7700', '#ffb57d'),
}
SYSTEM_INDICATOR_COLOR = 'red'
SYSTEM_INDICATOR_EXCLUSIONS = []
```

To exclude paths, include regex in ``SYSTEM_INDICATOR_EXCLUSIONS``::

```python
import re

SYSTEM_INDICATOR_EXCLUSIONS = [
    re.compile('^/[^/]+/admin/.*$'),
]
```

Example of a localhost indicator in admin;

![system indicator admin example](https://django-sys-indicator.s3.eu-west-2.amazonaws.com/screenshots/indicator-admin-header.png "Django system indicator")
