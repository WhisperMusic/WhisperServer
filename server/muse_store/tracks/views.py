from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast, override

from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from .models import Playlist, Track
from .serializers import (
    MyPlaylistSerializer,
    PlaylistSerializer,
    TrackSerializer,
)

if TYPE_CHECKING:
    from collections.abc import Sequence  # noqa: F401

    from django.db.models import QuerySet  # noqa: F401
    from django.db.models.manager import BaseManager
    from rest_framework.request import Request


class TrackViewSet(ReadOnlyModelViewSet):
    """All tracks ever uploaded to Muse Store.

    Here you can list all tracks or retrieve info about specific one.
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class MyTrackViewSet(GenericViewSet, ListModelMixin):
    @override
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # self.request.user cannot be AnonymousUser 'cause of permissions
        user = cast(User, self.request.user)

        queryset = user.tracks.only("pk")  # type: Sequence | QuerySet
        page = self.paginate_queryset(queryset)

        if page is not None:
            queryset = page
            make_response = self.get_paginated_response
        else:
            make_response = Response

        return make_response([track.pk for track in queryset])

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
