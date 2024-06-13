from typing import Any, ClassVar

from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Playlist, Track


class TrackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields: ClassVar = ["url", "title", "artist", "audio", "uploader"]


class MyTrackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Track
        fields: ClassVar = ["url", "title", "artist", "audio"]

    def __init__(
        self,
        *args: Any,
        uploader: User | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.uploader = uploader

    def create(self, validated_data: dict) -> Track:
        if self.uploader is None:
            raise ValueError

        validated_data["uploader"] = self.uploader
        return Track.objects.create(**validated_data)


class PlaylistSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        fields: ClassVar = [
            "url",
            "title",
            "tracks",
            "creator",
            "date_created",
            "date_last_modified",
        ]
