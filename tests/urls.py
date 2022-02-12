from django.urls import path

from tests import views

urlpatterns = [
    path("home/", views.home, name='home'),
]
