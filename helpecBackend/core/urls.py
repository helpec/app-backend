from django.urls import path, include
from rest_framework.authtoken import views as rest_framework_views

from .views import HomePage

urlpatterns = [
    path("", HomePage.as_view(), name="home-view"),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("accounts/", include("helpecBackend.hp_account.urls")),
]
