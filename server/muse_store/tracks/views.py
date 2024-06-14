from typing import Any, override

from django.db.models.manager import BaseManager
from rest_framework.exceptions import NotAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Playlist, Track
from .serializers import (
    MyPlaylistSerializer,
    MyTrackSerializer,
    PlaylistSerializer,
    TrackSerializer,
)


class TrackViewSet(ReadOnlyModelViewSet):
    """All tracks ever uploaded to Muse Store.

    Here you can list all tracks or retrieve info about specific one.
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class MyTrackViewSet(ModelViewSet):
    """Your tracks uploaded to Muse Store.

    Here you can get your tracks, edit them or upload new ones.
    """

    serializer_class = MyTrackSerializer

    @override
    def get_queryset(self) -> BaseManager[Track]:  # pyright: ignore[reportIncompatibleMethodOverride]
        return Track.objects.all()

    @override
    def get_serializer(self, *args: Any, **kwargs: Any) -> MyTrackSerializer:  # pyright: ignore[reportIncompatibleMethodOverride]
        self.check_logged_in()
        return super().get_serializer(
            *args,
            **kwargs,
            uploader=self.request.user,
        )

    @override
    def filter_queryset(
        self,
        queryset: BaseManager[Track],
    ) -> BaseManager[Track]:
        self.check_logged_in()
        return queryset.filter(uploader=self.request.user)

    def check_logged_in(self) -> None:
        if not self.request.user.is_authenticated:
            raise NotAuthenticated


class PlaylistViewSet(ModelViewSet):
    """All playlists ever created on Muse Store.

    Here you can list all playlists or get information about specific ones.
    """

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
