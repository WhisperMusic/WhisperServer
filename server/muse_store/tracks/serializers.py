from typing import ClassVar

from rest_framework.serializers import HyperlinkedModelSerializer

from muse_store.tracks.models import Track


class TrackModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields: ClassVar = ["title", "artist"]
