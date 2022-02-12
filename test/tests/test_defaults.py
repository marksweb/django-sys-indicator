from django.urls import reverse
from django.utils.encoding import force_str

import pytest


@pytest.mark.django_db
def test_home_view(client):
    """Ensure system indicator is disabled by default in a standard URL path"""
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert "content: 'localhost'" not in force_str(response.content)


@pytest.mark.django_db
def test_admin_view(client):
    """Ensure system indicator is disabled by default in admin"""
    url = reverse('admin:login')
    response = client.get(url)
    assert response.status_code == 200
    assert "content: 'localhost'" not in force_str(response.content)
