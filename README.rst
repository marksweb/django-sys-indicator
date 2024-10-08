django-sys-indicator
====================

.. image:: https://results.pre-commit.ci/badge/github/marksweb/django-sys-indicator/main.svg
   :target: https://results.pre-commit.ci/latest/github/marksweb/django-sys-indicator/main
   :alt: pre-commit.ci status

.. image:: https://img.shields.io/github/license/marksweb/django-sys-indicator
   :target: https://github.com/marksweb/django-sys-indicator/blob/main/LICENSE

.. image:: https://img.shields.io/github/issues/marksweb/django-sys-indicator
   :target: https://github.com/marksweb/django-sys-indicator/issues


A visual indicator of what environment/system you're using in django.

.. image:: https://django-sys-indicator.s3.eu-west-2.amazonaws.com/screenshots/django-sys-indicator.jpg
   :alt: system indicator examples


To install:

* Add ``"django_sys_indicator.apps.DjangoSysIndicatorConfig"`` to your ``INSTALLED_APPS``

* Add ``"django_sys_indicator.middleware.SystemIndicatorMiddleware"`` to your ``MIDDLEWARE``


Configuration settings and their defaults

.. code-block::

  SYSTEM_INDICATOR_ENABLED = False
  SYSTEM_INDICATOR_LABEL = "localhost"
  SYSTEM_INDICATOR_COLORS = {
      # Format here is colour, border colour
      "red": ("#c50000", "#daa"),
      "blue": ("#006fc4", "#aad"),
      "green": ("#009e00", "#ada"),
      "purple": ("#800080", "#dad"),
      "orange": ("#ff7700", "#ffb57d"),
  }

  SYSTEM_INDICATOR_COLOR = "red"

  SYSTEM_INDICATOR_EXCLUSIONS = []


To exclude paths, include regex in ``SYSTEM_INDICATOR_EXCLUSIONS``

.. code-block::

   import re

   SYSTEM_INDICATOR_EXCLUSIONS = [
       re.compile("^/[^/]+/admin/.\*$"),
   ]

Example of a localhost indicator in admin;

.. image:: https://django-sys-indicator.s3.eu-west-2.amazonaws.com/screenshots/indicator-admin-header.png
   :alt: system indicator admin example
