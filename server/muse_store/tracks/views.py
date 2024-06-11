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

    def get_queryset(self) -> BaseManager[Track]:  # pyright: ignore[reportIncompatibleMethodOverride]
        user = self.request.user
        return Track.objects.filter(uploader=user).all()

    def list(self, request: HttpRequest) -> Response:
        if not request.user.is_authenticated:
            content = {"reason": "this view requires authentication"}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
