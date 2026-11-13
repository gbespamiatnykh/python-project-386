"""URL routes for the api application."""

from django.urls import re_path

from api import views

urlpatterns = [
    # The TypeSpec contract exposes GET /api/health (no trailing slash);
    # accept both spellings so the real backend matches the contract exactly.
    re_path(r"^health/?$", views.health, name="health"),
]
