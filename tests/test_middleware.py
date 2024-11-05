from __future__ import annotations

from django.http import HttpRequest
from django.http import HttpResponse
from django.test import RequestFactory
from django.test import SimpleTestCase
from django.test import override_settings

from django_sys_indicator.conf import settings
from django_sys_indicator.middleware import SystemIndicatorMiddleware


class SystemIndicatorMiddlewareTests(SimpleTestCase):
    request_factory = RequestFactory()

    def setUp(self):
        self.request = self.request_factory.get("/")
        self.response = HttpResponse("<html><head></head><body></body></html>")

        def get_response(request: HttpRequest) -> HttpResponse:
            return self.response

        self.middleware = SystemIndicatorMiddleware(get_response)

    @override_settings(SYSTEM_INDICATOR_ENABLED=True)
    def test_content_length(self):
        self.response["Content-Length"] = 6553

        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        assert settings.SYSTEM_INDICATOR_LABEL in content

    @override_settings(SYSTEM_INDICATOR_ENABLED=True)
    def test_invalid_content(self):
        self.response = HttpResponse("<html><body></body></html>")

        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        assert settings.SYSTEM_INDICATOR_LABEL not in content

    @override_settings(SYSTEM_INDICATOR_ENABLED=False)
    def test_not_enabled(self):
        response = self.middleware(self.request)

        assert response.content == b"<html><head></head><body></body></html>"

    @override_settings(SYSTEM_INDICATOR_ENABLED=True)
    def test_enabled(self):
        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        color, border_color = settings.SYSTEM_INDICATOR_COLORS[
            settings.SYSTEM_INDICATOR_COLOR
        ]

        assert settings.SYSTEM_INDICATOR_LABEL in content
        assert border_color in content
        assert color in content

    @override_settings(SYSTEM_INDICATOR_ENABLED=True, SYSTEM_INDICATOR_COLOR="orange")
    def test_enabled_orange(self):
        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        color, border_color = settings.SYSTEM_INDICATOR_COLORS[
            settings.SYSTEM_INDICATOR_COLOR
        ]

        assert settings.SYSTEM_INDICATOR_LABEL in content
        assert border_color in content
        assert color in content

    @override_settings(SYSTEM_INDICATOR_ENABLED=True, SYSTEM_INDICATOR_COLOR="black")
    def test_invalid_colour(self):
        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        # Invalid colour results in red as a default
        color, border_color = settings.SYSTEM_INDICATOR_COLORS["red"]

        assert settings.SYSTEM_INDICATOR_LABEL in content
        assert border_color in content
        assert color in content

    @override_settings(SYSTEM_INDICATOR_ENABLED=True, SYSTEM_INDICATOR_LABEL=123)
    def test_int_label(self):
        response = self.middleware(self.request)
        content = response.content.decode(response.charset)
        color, border_color = settings.SYSTEM_INDICATOR_COLORS[
            settings.SYSTEM_INDICATOR_COLOR
        ]

        # cast to string here because of the assert against the string content
        assert str(settings.SYSTEM_INDICATOR_LABEL) in content
        assert border_color in content
        assert color in content
