from django.test import override_settings
from django.urls import reverse

from .views import home


def test_home_view(client):
    """Ensure system indicator is disabled by default in a standard URL path"""
    url = reverse("home")
    request = client.get(url)
    response = home(request)
    assert response.status_code == 200


def test_with_indicator_enabled(client, settings):
    with override_settings(SYSTEM_INDICATOR_ENABLED=True):
        url = reverse('home')
        request = client.get(url)
        response = home(request)
        assert response.status_code == 200


def test_with_indicator_text(client, settings):
    label = 'Indicator test'
    with override_settings(SYSTEM_INDICATOR_ENABLED=True, SYSTEM_INDICATOR_LABEL=label):
        url = reverse('home')
        request = client.get(url)
        response = home(request)
        assert response.status_code == 200
