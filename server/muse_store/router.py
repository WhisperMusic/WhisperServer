from rest_framework.routers import DefaultRouter

from muse_store.tracks.views import (
    MyPlaylistViewSet,
    MyTrackViewSet,
    PlaylistViewSet,
    TrackViewSet,
)
from muse_store.users.views import GroupViewSet, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("groups", GroupViewSet)
router.register("tracks", TrackViewSet)
router.register("me/tracks", MyTrackViewSet, basename="my-track")
router.register("playlists", PlaylistViewSet)
router.register("me/playlists", MyPlaylistViewSet, basename="my-playlist")
