from typing import cast, override

from django.db.models.manager import BaseManager
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from muse_store.tracks.models import Track
from muse_store.tracks.serializers import TrackSerializer


class TracksViewSet(ReadOnlyModelViewSet):
    """General tracks viewset.

    This viewset provides read-only views for listing and retrieving tracks.
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class MyTracksViewSet(ModelViewSet):
    serializer_class = TrackSerializer

    @override
    def get_queryset(self) -> BaseManager[Track]:  # pyright: ignore[reportIncompatibleMethodOverride]
        return Track.objects.all()

    @override
    def filter_queryset(
        self, queryset: BaseManager[Track],
    ) -> BaseManager[Track]:
        self.check_logged_in()
        return queryset.filter(uploader=self.request.user)

    def check_logged_in(self) -> None:
        if not self.request.user.is_authenticated:
            raise NotAuthenticated

    @override
    def retrieve(
        self, request: Request, pk: str | None = None,
    ) -> Response:
        self.check_logged_in()
        queryset = Track.objects.all()
        track = get_object_or_404(queryset, pk=pk)

        if track.uploader != request.user:
            msg = "This track is owned not by you"
            raise PermissionDenied(msg)

        serializer = self.get_serializer(track)
        return Response(serializer.data)

    @override
    def create(self, request: Request) -> Response:
        self.check_logged_in()
        serializer = cast(
            TrackSerializer,
            self.get_serializer(data=request.data, uploader=request.user),
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers,
        )
