from django.urls import reverse
from django.utils.encoding import force_str

import pytest


@pytest.mark.django_db
def test_with_indicator_enabled(client, settings):
    settings.SYSTEM_INDICATOR_ENABLED = True
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert "content: 'localhost'" not in force_str(response.content)


@pytest.mark.django_db
def test_with_indicator_text(client, settings):
    label = 'Indicator test'
    settings.SYSTEM_INDICATOR_ENABLED = True
    settings.SYSTEM_INDICATOR_LABEL = label
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert f"content: '{label}'" in force_str(response.content)
