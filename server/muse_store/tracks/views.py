from rest_framework.viewsets import ModelViewSet

from muse_store.tracks.models import Track
from muse_store.tracks.serializers import TrackModelSerializer


class TrackModelViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackModelSerializer
    # TODO: Add permission classes to viewset
