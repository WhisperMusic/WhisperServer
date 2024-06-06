from rest_framework.viewsets import ModelViewSet

from muse_store.tracks.models import TrackModel
from muse_store.tracks.serializers import TrackModelSerializer


class TrackModelViewSet(ModelViewSet):
    queryset = TrackModel.objects.all()
    serializer_class = TrackModelSerializer
    # TODO: Add permission classes to viewset
