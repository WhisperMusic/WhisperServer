from typing import ClassVar, Self

from django.db import models
from django.db.models.manager import BaseManager


class TrackModel(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    objects: ClassVar[BaseManager[Self]]

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"
