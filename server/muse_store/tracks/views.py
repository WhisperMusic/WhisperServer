from typing import Any, override

from django.db.models.manager import BaseManager
from rest_framework.exceptions import NotAuthenticated
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
    def get_serializer(self, *args: Any, **kwargs: Any) -> TrackSerializer:  # type: ignore[reportIncompatibleMethodOverride]
        self.check_logged_in()
        return super().get_serializer(
            *args, **kwargs, uploader=self.request.user,
        )

    @override
    def filter_queryset(
        self, queryset: BaseManager[Track],
    ) -> BaseManager[Track]:
        self.check_logged_in()
        return queryset.filter(uploader=self.request.user)

    def check_logged_in(self) -> None:
        if not self.request.user.is_authenticated:
            raise NotAuthenticated
