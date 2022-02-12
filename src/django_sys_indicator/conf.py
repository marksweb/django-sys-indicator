from django.conf import settings

DEFAULT_COLOURS = {
    # Format here is colour, border colour
    'red': ('#c50000', '#daa'),
    'blue': ('#006fc4', '#aad'),
    'green': ('#009e00', '#ada'),
    'purple': ('#800080', '#dad'),
    'orange': ('#ff7700', '#ffb57d'),
}

SYSTEM_INDICATOR_ENABLED = getattr(settings, 'SYSTEM_INDICATOR_ENABLED', False)
SYSTEM_INDICATOR_LABEL = getattr(settings, 'SYSTEM_INDICATOR_LABEL', 'localhost')
SYSTEM_INDICATOR_COLORS = getattr(settings, 'SYSTEM_INDICATOR_COLORS', DEFAULT_COLOURS)
SYSTEM_INDICATOR_COLOR = getattr(settings, 'SYSTEM_INDICATOR_COLOR', 'green')
SYSTEM_INDICATOR_EXCLUSIONS = getattr(settings, 'SYSTEM_INDICATOR_EXCLUSIONS', [])
