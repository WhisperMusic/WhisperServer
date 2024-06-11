from typing import Any, override

from django.db.models.manager import BaseManager
from rest_framework.exceptions import NotAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from muse_store.tracks.models import Track
from muse_store.tracks.serializers import MyTrackSerializer, TrackSerializer


class TracksViewSet(ReadOnlyModelViewSet):
    """All tracks ever uploaded to Muse Store.

    Here you can list all tracks or retrieve info about specific one.
    """

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

class MyTracksViewSet(ModelViewSet):
    """Your tracks uploaded to Muse Store.

    Here you can get your tracks, edit them or upload new ones.
    """
    serializer_class = MyTrackSerializer

    @override
    def get_queryset(self) -> BaseManager[Track]:  # pyright: ignore[reportIncompatibleMethodOverride]
        return Track.objects.all()

    @override
    def get_serializer(self, *args: Any, **kwargs: Any) -> MyTrackSerializer:  # type: ignore[reportIncompatibleMethodOverride]
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
