from django.urls import include, path
from rest_framework.routers import DefaultRouter

from muse_store.tracks.views import TracksViewSet
from muse_store.users.views import GroupViewSet, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("tracks", TracksViewSet)

urlpatterns = router.urls
urlpatterns.append(
    path("auth", include("rest_framework.urls", namespace="rest_framework")),
)
