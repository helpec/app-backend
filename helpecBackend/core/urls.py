from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from helpecBackend.core import views

router = routers.DefaultRouter()
router.register(r"contact", views.ContactViewSet)
router.register(r"occurrence", views.OccurrenceViewSet)

schema_view = get_swagger_view(title="Helpec Backend API")

urlpatterns = [
    path("", schema_view),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path("accounts/", include(router.urls)),
]
