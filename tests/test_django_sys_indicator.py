from django.conf import settings
from django.test import Client
from django.urls import reverse


def test_home_view():
    """Ensure system indicator is disabled by default in a standard URL path"""
    url = reverse("home")
    client = Client()
    response = client.get(url)
    assert response.status_code == 200
    assert settings.SYSTEM_INDICATOR_LABEL not in response.content.decode(response.charset)
