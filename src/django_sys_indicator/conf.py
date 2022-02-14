from __future__ import annotations

from typing import Sequence

from django.conf import settings as dj_settings

DEFAULT_COLOURS = {
    # Format here is colour, border colour
    'red': ('#c50000', '#daa'),
    'blue': ('#006fc4', '#aad'),
    'green': ('#009e00', '#ada'),
    'purple': ('#800080', '#dad'),
    'orange': ('#ff7700', '#ffb57d'),
}


class Settings:
    """Lazy settings"""

    @property
    def SYSTEM_INDICATOR_ENABLED(self) -> bool:  # noqa: N802
        return getattr(dj_settings, "SYSTEM_INDICATOR_ENABLED", False)

    @property
    def SYSTEM_INDICATOR_COLOR(self) -> str:  # noqa: N802
        return getattr(dj_settings, "SYSTEM_INDICATOR_COLOR", 'green')

    @property
    def SYSTEM_INDICATOR_LABEL(self) -> str:  # noqa: N802
        return getattr(dj_settings, "SYSTEM_INDICATOR_LABEL", 'localhost')

    @property
    def SYSTEM_INDICATOR_COLORS(self) -> dict:  # noqa: N802
        return getattr(dj_settings, "SYSTEM_INDICATOR_COLORS", DEFAULT_COLOURS)

    @property
    def SYSTEM_INDICATOR_EXCLUSIONS(self) -> Sequence[str]:  # noqa: N802
        return getattr(dj_settings, "SYSTEM_INDICATOR_EXCLUSIONS", [])


settings = Settings()
