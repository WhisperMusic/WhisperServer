from typing import Any, override

from django.db.models.manager import BaseManager
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import BaseSerializer
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

    queryset = Track.objects.all()
    serializer_class = MyTrackSerializer

    @override
    def get_serializer(
        self,
        *args: Any,
        **kwargs: Any,
    ) -> BaseSerializer[Any]:
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
        return queryset.filter(uploader=self.request.user)

    permission_classes = [IsAuthenticated]


class PlaylistViewSet(ReadOnlyModelViewSet):
    """All playlists ever created on Muse Store.

    Here you can list all playlists or get information about specific ones.
    """

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class MyPlaylistViewSet(ModelViewSet):
    """Playlists on Muse Store created by you.

    Here you can get your playlists, edit them or create new ones.
    """

    queryset = Playlist.objects.all()
    serializer_class = MyPlaylistSerializer

    @override
    def get_serializer(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        *args: Any,
        **kwargs: Any,
    ) -> MyPlaylistSerializer:
        return super().get_serializer(
            *args,
            **kwargs,
            creator=self.request.user,
        )

    @override
    def filter_queryset(
        self,
        queryset: BaseManager[Playlist],
    ) -> BaseManager[Playlist]:
        return queryset.filter(creator=self.request.user)

    permission_classes = [IsAuthenticated]
