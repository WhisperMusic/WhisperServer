from typing import override

from django.db.models.manager import BaseManager
from django.http import HttpRequest
from rest_framework import status
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
        user = self.request.user
        return Track.objects.filter(uploader=user).all()

    def check_logged_in(self) -> Response | None:
        if not self.request.user.is_authenticated:
            content = {"detail": "This view requires authentication."}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        return None

    @override
    def list(self, request: HttpRequest) -> Response:
        respoonse = self.check_logged_in()

        if respoonse is not None:
            return respoonse

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
