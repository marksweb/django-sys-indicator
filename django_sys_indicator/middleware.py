from django.template.loader import render_to_string
from django.utils.encoding import force_str

from .conf import (
    SYSTEM_INDICATOR_COLOR, SYSTEM_INDICATOR_COLORS, SYSTEM_INDICATOR_ENABLED, SYSTEM_INDICATOR_EXCLUSIONS,
    SYSTEM_INDICATOR_LABEL,
)


class SystemIndicatorMiddleware:
    """
    Middleware which inserts the system indicator into the response if:
     - it's enabled in settings, and
     - this is a page-response (not JSON etc.) and contains a full page (we
       look for closing </head>, so HTML snippets won't be modified by this
    """
    template_name = 'django_sys_indicator/system_indicator.html'

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if not SYSTEM_INDICATOR_ENABLED:
            # indicator disabled
            return response

        # check for response types to ignore
        content_encoding = response.get('Content-Encoding', '')
        content_type = response.get('Content-Type', '').split(';')[0]

        is_streaming = getattr(response, 'streaming', False)
        is_gzip = 'gzip' in content_encoding
        is_invalid = content_type not in ('text/html', 'application/xhtml+xml')

        if any([is_streaming, is_gzip, is_invalid]):
            # system indicator shouldn't be inserted
            return response

        path = request.path
        for exclusion in SYSTEM_INDICATOR_EXCLUSIONS:
            if exclusion.match(path):
                # system indicator shouldn't be inserted
                return response

        # extract the HTML content from the response
        html = force_str(response.content)
        if html.find('</head>') < 0:
            # no closing </head>...assuming this isn't a standard page response
            return response

        # render the system indicator markup (this is done as a CSS style
        # rule internally)
        label = SYSTEM_INDICATOR_LABEL
        color, border_color = SYSTEM_INDICATOR_COLORS[
            SYSTEM_INDICATOR_COLOR
        ]
        system_indicator_html = render_to_string(
            self.template_name,
            {
                'label': label,
                'color': color,
                'border_color': border_color,
            }
        ) + '</head>'

        # insert the system identifier style rule just before the closing
        # </head> tag (at most once!)
        html = html.replace('</head>', system_indicator_html, 1)

        # update the response with the modified HTML content
        response.content = force_str(html)
        if response.get('Content-Length', None):
            response['Content-Length'] = len(response.content)

        return response
