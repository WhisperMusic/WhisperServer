from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from .router import router

schema_view = get_swagger_view(title="Whisper REST API")

urlpatterns = [
    *router.urls,
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("docs/", schema_view),
]
