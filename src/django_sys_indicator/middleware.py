from __future__ import annotations

import re
from typing import Callable

from django.http import HttpRequest, HttpResponse

from django_sys_indicator.conf import settings
from django_sys_indicator.utils import django_sys_indicator_tag

insert_before_re = re.compile(r"</head>", flags=re.IGNORECASE)


class SystemIndicatorMiddleware:
    """
    Middleware which inserts the system indicator into the response if:
     - it's enabled in settings, and
     - this is a page-response (not JSON etc.) and contains a full page (we
       look for closing </head>, so HTML snippets won't be modified by this
    """
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        response = self.get_response(request)

        # check for response types to ignore
        content_encoding = response.get('Content-Encoding', '')
        content_type = response.get('Content-Type', '').split(';')[0]

        if (
            not settings.SYSTEM_INDICATOR_ENABLED
            or getattr(response, "streaming", False)
            or 'gzip' in content_encoding
            or content_type not in ('text/html', 'application/xhtml+xml')
        ):
            return response

        content = response.content.decode(response.charset)
        # Find last match
        found = False
        for match in insert_before_re.finditer(content):  # noqa: B007
            found = True
        if not found:
            return response

        head = content[:match.start()]
        tag = match[0]
        tail = content[match.end():]

        response.content = head + django_sys_indicator_tag() + tag + tail
        if "Content-Length" in response:
            response["Content-Length"] = len(response.content)

        return response
