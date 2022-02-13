from django.urls import reverse

import pytest

from .views import home

CUSTOM_LABEL = 'Indicator test'


@pytest.fixture()
def enable_indicator(settings):
    settings.SYSTEM_INDICATOR_ENABLED = True


@pytest.fixture()
def enable_indicator_with_custom_label(settings):
    settings.SYSTEM_INDICATOR_ENABLED = True
    settings.SYSTEM_INDICATOR_LABEL = CUSTOM_LABEL


def test_home_view(client):
    """Ensure system indicator is disabled by default in a standard URL path"""
    url = reverse("home")
    request = client.get(url)
    response = home(request)
    assert response.status_code == 200


def test_with_indicator_enabled(enable_indicator, client):
    url = reverse('home')
    request = client.get(url)
    response = home(request)
    assert response.status_code == 200


def test_with_indicator_text(enable_indicator_with_custom_label, client):
    url = reverse('home')
    request = client.get(url)
    response = home(request)
    assert response.status_code == 200
