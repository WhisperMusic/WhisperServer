from django.db import models


class TrackModel(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"
