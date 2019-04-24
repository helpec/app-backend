from django.urls import path, include
from rest_framework import routers

from helpecBackend.core import views

router = routers.DefaultRouter()
router.register(r"contact", views.ContactViewSet)
router.register(r"occurrence", views.OccurrenceViewSet)


urlpatterns = [
    path("", views.HomePage.as_view(), name="home-view"),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("accounts/", include(router.urls)),
]
