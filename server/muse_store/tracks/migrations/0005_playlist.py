# Generated by Django 4.2.13 on 2024-06-13 11:24

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tracks", "0004_track_date_last_modified_track_date_uploaded"),
    ]

    operations = [
        migrations.CreateModel(
            name="Playlist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("date_last_modified", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="playlists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("tracks", models.ManyToManyField(to="tracks.track")),
            ],
        ),
    ]
