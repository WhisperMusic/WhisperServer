from django.urls import include, path

from . import schema
from .router import router

urlpatterns = [
    *router.urls,
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    *schema.urls,
]
