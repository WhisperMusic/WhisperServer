from typing import ClassVar

from rest_framework.serializers import HyperlinkedModelSerializer

from muse_store.tracks.models import TrackModel


class TrackModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TrackModel
        fields: ClassVar = ["title", "artist"]
