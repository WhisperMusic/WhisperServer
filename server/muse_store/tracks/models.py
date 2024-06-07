from typing import ClassVar, Self

from django.contrib.auth.models import User
from django.db import models
from django.db.models.manager import BaseManager


class Track(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)

    audio = models.FileField(upload_to="audio/")

    uploader = models.ForeignKey(User, models.CASCADE)

    objects: ClassVar[BaseManager[Self]]

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"
