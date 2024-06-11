from rest_framework.viewsets import ReadOnlyModelViewSet

from muse_store.tracks.models import Track
from muse_store.tracks.serializers import TrackSerializer


class TracksViewSet(ReadOnlyModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
