from __future__ import annotations

from django.template.loader import render_to_string

from .conf import settings


def django_sys_indicator_tag() -> str:
    template_name = 'django_sys_indicator/system_indicator.html'

    try:
        color, border_color = settings.SYSTEM_INDICATOR_COLORS[
            settings.SYSTEM_INDICATOR_COLOR
        ]
    except KeyError:
        # Invalid colour chosen
        color, border_color = settings.SYSTEM_INDICATOR_COLORS['red']
    return render_to_string(
        template_name,
        {
            'label': settings.SYSTEM_INDICATOR_LABEL,
            'color': color,
            'border_color': border_color,
        }
    )
