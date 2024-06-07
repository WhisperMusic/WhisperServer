from rest_framework.viewsets import ModelViewSet

from muse_store.tracks.models import Track
from muse_store.tracks.serializers import TrackSerializer


class TrackModelViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    # TODO: Add permission classes to viewset
